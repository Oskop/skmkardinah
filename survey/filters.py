from django.contrib import admin
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import QuerySet, lookups
from django.template.loader import render_to_string
from django.utils.translation import gettext_lazy as _
from django_pandas.io import read_frame
from survey.models import SurveiKepuasanMasyarakat
import pandas as pd
import numpy as np
import pdfkit
# import base64
from babel.dates import format_date
from datetime import date, datetime
from pathlib import Path
import pytz


pdfkit_config = pdfkit.configuration(
    wkhtmltopdf="C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")
indonesia_zone = pytz.timezone("Asia/Jakarta")


def export_to_html(request, queryset):
    return


def export_to_pdf_survey(request, queryset):
    df = read_frame(queryset.order_by('created_at'), fieldnames=(
                'created_at', 'fasilitas_rate', 'perawat_rate', 
                'dokter_rate', 'farmasi_rate', 'komentar'),
                column_names=[
                    'Tanggal', 'Fasilitas rate', 'Perawat rate',
                    'Dokter rate', 'Farmasi rate', 'Komentar'
                ])
    # df.index = np.arange(1, len(df) + 1)
    dari, ke = None, None
    df['Tanggal'] = [
            x.astimezone(indonesia_zone).to_pydatetime(
            ).date().strftime('%Y-%m-%d') for x in df['Tanggal']]
    # for i in range(df.shape[0]):
    #     df.iloc[i, 0] = format_date(
    #         df.iloc[i, 0].astimezone(indonesia_zone).to_pydatetime().date(),
    #         format='medium', locale='id_ID')
    df.insert(0, "No", [x+1 for x in range(df.shape[0])])
    for lk in queryset.query.where.children:
        if isinstance(
            lk,lookups.GreaterThanOrEqual
        ) or isinstance(lk, lookups.GreaterThan):
            dari = format_date(lk.rhs.date(), 'full', locale='id')
        elif isinstance(
            lk, lookups.LessThan
        ) or isinstance(lk, lookups.LessThanOrEqual):
            ke = format_date(lk.rhs.date(), 'full', locale='id')
    thepath = 'survey/templates/datasets/rawdataset.html'
    df.loc[len(df.index)] = [
        "",
        "Rata-rata",
        df.loc[:, 'Fasilitas rate'].mean(), # fasilitas
        df.loc[:, 'Perawat rate'].mean(),
        df.loc[:, 'Dokter rate'].mean(),
        df.loc[:, 'Farmasi rate'].mean(),
        ""
    ]
    Path(thepath).parent.mkdir(exist_ok=True)
    df.to_html(
        'survey/Templates/datasets/rawdataset.html',
        index=False
    )
    logo_path = "survey/static/survey/assets_frontend/img/kardinah.png"
    # data_base64 = ""
    # if Path(logo_path).exists():
    #     data = open(logo_path, 'rb').read() # read bytes from file
    #     data_base64 = base64.b64encode(data)  # encode to base64 (bytes)
    #     data_base64 = data_base64.decode()    # convert bytes to string
    context = {
        'dari': dari, 'ke': ke,
        'logo_kardinah': Path(logo_path).absolute().__str__()
    }
    out = render_to_string(
        request=request,
        template_name="datasets/report_template.html",
        context=context)
    pdfnya = pdfkit.from_string(
        out, configuration=pdfkit_config,
        options={"enable-local-file-access": ""})
    filename = "Laporan Survey"
    if (dari is not None and ke is not None) and (
        dari != "" and ke != ""):
        filename += f" {dari} - {ke}.pdf"
    return pdfnya, filename


class ReportExportFilter(admin.SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = _("Laporan")

    # Parameter for the filter that will be used in the URL query.
    parameter_name = "lapor"

    def lookups(self, request, model_admin):
        thelist = [
            ('01', 'PDF',),
        ]
        return thelist

    def queryset(self, request, 
                 queryset: QuerySet[SurveiKepuasanMasyarakat]):
        if self.value() == '01':
            return export_to_pdf_survey(
                request=request, queryset=queryset)
        else:
            return queryset
