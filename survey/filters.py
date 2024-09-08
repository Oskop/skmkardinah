from django.contrib import admin
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import QuerySet, lookups
from django.template.loader import render_to_string
from django.utils.translation import gettext_lazy as _
from django_pandas.io import read_frame
from survey.models import (
    SurveiKepuasanMasyarakat,
    SurveiKepuasanMasyarakatRev,
    Pegawai)
from admincharts.utils import months_between_dates
from django.utils import timezone
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


def get_quality_values(numb: float):
    if numb >= 4.5 and numb <= 5:
        return "Sangat Memuaskan"
    elif numb >= 3.5 and numb <= 4.4:
        return "Memuaskan"
    elif numb >= 3 and numb <= 3.4:
        return "Cukup Memuaskan"
    elif numb >= 2.5 and numb <= 2.9:
        return "Kurang Memuaskan"
    elif numb >= 0 and numb <= 2.4:
        return "Tidak Memuaskan"
    return "Tidak Diketahui"


def get_datasets_labels_from_queryset(queryset):
    # Cannot reorder the queryset at this point
    earliest = min([x.created_at for x in queryset])

    labels = []
    farmasi_totals = []
    perawat_totals = []
    dokter_totals = []
    fasilitas_totals = []
    all_total = []
    for b in months_between_dates(earliest, timezone.now()):
        labels.append(b.strftime("%b %Y"))
        farmasi_totals.append(
            sum(
                [
                    (x.etika_farmasi_rate
                     + x.penampilan_farmasi_rate
                     + x.kecepatan_farmasi_rate
                     + x.ketepatan_farmasi_rate
                     + x.informatif_farmasi_rate) / 5
                    for x in queryset
                    if x.created_at.year == b.year and x.created_at.month == b.month
                ]
            ) / queryset.filter(created_at__month=b.month, created_at__year=b.year).count()
        )
        fasilitas_totals.append(
            sum(
                [
                    (x.kelengkapan_fasilitas_rate
                     + x.kebersihan_fasilitas_rate
                     + x.kenyamanan_fasilitas_rate
                     + x.kamarmandi_fasilitas_rate
                     + x.kualitas_fasilitas_rate) / 5
                    for x in queryset
                    if x.created_at.year == b.year and x.created_at.month == b.month
                ]
            ) / queryset.filter(created_at__month=b.month, created_at__year=b.year).count()
        )
        perawat_totals.append(
            sum(
                [
                    (x.etika_perawat_rate
                     + x.penampilan_perawat_rate
                     + x.kecakapan_perawat_rate
                     + x.ketepatan_perawat_rate
                     + x.komunikatif_perawat_rate) / 5
                    for x in queryset
                    if x.created_at.year == b.year and x.created_at.month == b.month
                ]
            ) / queryset.filter(created_at__month=b.month, created_at__year=b.year).count()
        )
        dokter_totals.append(
            sum(
                [
                    (x.etika_dokter_rate
                     + x.penampilan_dokter_rate
                     + x.kecakapan_dokter_rate
                     + x.ketepatan_dokter_rate
                     + x.solutif_dokter_rate) / 5
                    for x in queryset
                    if x.created_at.year == b.year and x.created_at.month == b.month
                ]
            ) / queryset.filter(created_at__month=b.month, created_at__year=b.year).count()
        )
        all_total.append(
            sum(
                [
                    (x.etika_farmasi_rate
                     + x.penampilan_farmasi_rate
                     + x.kecepatan_farmasi_rate
                     + x.ketepatan_farmasi_rate
                     + x.informatif_farmasi_rate
                     + x.kelengkapan_fasilitas_rate
                     + x.kebersihan_fasilitas_rate
                     + x.kenyamanan_fasilitas_rate
                     + x.kamarmandi_fasilitas_rate
                     + x.kualitas_fasilitas_rate
                     + x.etika_perawat_rate
                     + x.penampilan_perawat_rate
                     + x.kecakapan_perawat_rate
                     + x.ketepatan_perawat_rate
                     + x.komunikatif_perawat_rate
                     + x.etika_dokter_rate
                     + x.penampilan_dokter_rate
                     + x.kecakapan_dokter_rate
                     + x.ketepatan_dokter_rate
                     + x.solutif_dokter_rate) / 20
                    for x in queryset
                    if x.created_at.year == b.year and x.created_at.month == b.month
                ]
            ) / queryset.filter(created_at__month=b.month, created_at__year=b.year).count()
        )
    return labels, farmasi_totals, perawat_totals, dokter_totals, fasilitas_totals, all_total


def export_to_html(request, queryset):
    return


# def export_to_pdf_survey(request, queryset):
#     df = read_frame(queryset.order_by('created_at'), fieldnames=(
#                 'created_at', 'fasilitas_rate', 'perawat_rate', 
#                 'dokter_rate', 'farmasi_rate', 'komentar'),
#                 column_names=[
#                     'Tanggal', 'Fasilitas rate', 'Perawat rate',
#                     'Dokter rate', 'Farmasi rate', 'Komentar'
#                 ])
#     # df.index = np.arange(1, len(df) + 1)
#     dari, ke = None, None
#     df['Tanggal'] = [
#             x.astimezone(indonesia_zone).to_pydatetime(
#             ).date().strftime('%Y-%m-%d') for x in df['Tanggal']]
#     # for i in range(df.shape[0]):
#     #     df.iloc[i, 0] = format_date(
#     #         df.iloc[i, 0].astimezone(indonesia_zone).to_pydatetime().date(),
#     #         format='medium', locale='id_ID')
#     df.insert(0, "No", [x+1 for x in range(df.shape[0])])
#     for lk in queryset.query.where.children:
#         if isinstance(
#             lk,lookups.GreaterThanOrEqual
#         ) or isinstance(lk, lookups.GreaterThan):
#             dari = format_date(lk.rhs.date(), 'full', locale='id')
#         elif isinstance(
#             lk, lookups.LessThan
#         ) or isinstance(lk, lookups.LessThanOrEqual):
#             ke = format_date(lk.rhs.date(), 'full', locale='id')
#     thepath = 'survey/templates/datasets/rawdataset.html'
#     df['Fasilitas rate'] = df['Fasilitas rate'].astype(np.int8)
#     df['Perawat rate'] = df['Perawat rate'].astype(np.int8)
#     df['Dokter rate'] = df['Dokter rate'].astype(np.int8)
#     df['Farmasi rate'] = df['Farmasi rate'].astype(np.int8)
#     df.loc[len(df.index)] = [
#         "",
#         "Rata-rata",
#         str(round(df.loc[:, 'Fasilitas rate'].mean(), 2)).replace('.', ','),
#         str(round(df.loc[:, 'Perawat rate'].mean(), 2)).replace('.', ','),
#         str(round(df.loc[:, 'Dokter rate'].mean(), 2)).replace('.', ','),
#         str(round(df.loc[:, 'Farmasi rate'].mean(), 2)).replace('.', ','),
#         ""
#     ]
#     Path(thepath).parent.mkdir(exist_ok=True)
#     df.to_html(
#         'survey/Templates/datasets/rawdataset.html',
#         index=False
#     )
#     logo_path = "survey/static/survey/assets_frontend/img/kardinah.png"
#     # data_base64 = ""
#     # if Path(logo_path).exists():
#     #     data = open(logo_path, 'rb').read() # read bytes from file
#     #     data_base64 = base64.b64encode(data)  # encode to base64 (bytes)
#     #     data_base64 = data_base64.decode()    # convert bytes to string
#     context = {
#         'dari': dari, 'ke': ke,
#         'logo_kardinah': Path(logo_path).absolute().__str__()
#     }
#     out = render_to_string(
#         request=request,
#         template_name="datasets/report_template.html",
#         context=context)
#     pdfnya = pdfkit.from_string(
#         out, configuration=pdfkit_config,
#         options={"enable-local-file-access": ""})
#     filename = "Laporan Survey"
#     if (dari is not None and ke is not None) and (
#         dari != "" and ke != ""):
#         filename += f" {dari} - {ke}.pdf"
#     return pdfnya, filename


def export_to_pdf_survey_rev(
        request, queryset: QuerySet[SurveiKepuasanMasyarakatRev]):
    df = read_frame(queryset.order_by('created_at'), fieldnames=(
                'created_at', 
                'etika_perawat_rate',
                'penampilan_perawat_rate',
                'kecakapan_perawat_rate',
                'ketepatan_perawat_rate',
                'komunikatif_perawat_rate',
                'etika_dokter_rate',
                'penampilan_dokter_rate',
                'kecakapan_dokter_rate',
                'ketepatan_dokter_rate',
                'solutif_dokter_rate',
                'etika_farmasi_rate',
                'penampilan_farmasi_rate',
                'kecepatan_farmasi_rate',
                'ketepatan_farmasi_rate',
                'informatif_farmasi_rate',
                'kelengkapan_fasilitas_rate',
                'kebersihan_fasilitas_rate',
                'kenyamanan_fasilitas_rate',
                'kamarmandi_fasilitas_rate',
                'kualitas_fasilitas_rate',
                ),
                column_names=[
                    'Tanggal',
                    'etika_perawat_rate',
                    'penampilan_perawat_rate',
                    'kecakapan_perawat_rate',
                    'ketepatan_perawat_rate',
                    'komunikatif_perawat_rate',
                    'etika_dokter_rate',
                    'penampilan_dokter_rate',
                    'kecakapan_dokter_rate',
                    'ketepatan_dokter_rate',
                    'solutif_dokter_rate',
                    'etika_farmasi_rate',
                    'penampilan_farmasi_rate',
                    'kecepatan_farmasi_rate',
                    'ketepatan_farmasi_rate',
                    'informatif_farmasi_rate',
                    'kelengkapan_fasilitas_rate',
                    'kebersihan_fasilitas_rate',
                    'kenyamanan_fasilitas_rate',
                    'kamarmandi_fasilitas_rate',
                    'kualitas_fasilitas_rate',
                ])
    # df.index = np.arange(1, len(df) + 1)
    df['etika_perawat_rate'] = df['etika_perawat_rate'].astype(np.int8)
    df['penampilan_perawat_rate'] = df['penampilan_perawat_rate'].astype(np.int8)
    df['kecakapan_perawat_rate'] = df['kecakapan_perawat_rate'].astype(np.int8)
    df['ketepatan_perawat_rate'] = df['ketepatan_perawat_rate'].astype(np.int8)
    df['komunikatif_perawat_rate'] = df['komunikatif_perawat_rate'].astype(np.int8)
    
    df['etika_dokter_rate'] = df['etika_dokter_rate'].astype(np.int8)
    df['penampilan_dokter_rate'] = df['penampilan_dokter_rate'].astype(np.int8)
    df['kecakapan_dokter_rate'] = df['kecakapan_dokter_rate'].astype(np.int8)
    df['ketepatan_dokter_rate'] = df['ketepatan_dokter_rate'].astype(np.int8)
    df['solutif_dokter_rate'] = df['solutif_dokter_rate'].astype(np.int8)

    df['etika_farmasi_rate'] = df['etika_farmasi_rate'].astype(np.int8)
    df['penampilan_farmasi_rate'] = df['penampilan_farmasi_rate'].astype(np.int8)
    df['kecepatan_farmasi_rate'] = df['kecepatan_farmasi_rate'].astype(np.int8)
    df['ketepatan_farmasi_rate'] = df['ketepatan_farmasi_rate'].astype(np.int8)
    df['informatif_farmasi_rate'] = df['informatif_farmasi_rate'].astype(np.int8)
    
    df['kelengkapan_fasilitas_rate'] = df['kelengkapan_fasilitas_rate'].astype(np.int8)
    df['kebersihan_fasilitas_rate'] = df['kebersihan_fasilitas_rate'].astype(np.int8)
    df['kenyamanan_fasilitas_rate'] = df['kenyamanan_fasilitas_rate'].astype(np.int8)
    df['kamarmandi_fasilitas_rate'] = df['kamarmandi_fasilitas_rate'].astype(np.int8)
    df['kualitas_fasilitas_rate'] = df['kualitas_fasilitas_rate'].astype(np.int8)


    if queryset.order_by('created_at').first():
        dari = format_date(queryset.order_by(
            'created_at').first().created_at.date(), 'full', locale='id')
    else:
        dari = '-'
    if queryset.order_by('created_at').last():
        ke = format_date(queryset.order_by(
            'created_at').last().created_at.date(), 'full', locale='id')
    else:
        ke = '-'
    tanggal = format_date(date.today(), format='long', locale='id_ID')
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

        if isinstance(
            lk, lookups.LessThan
        ) or isinstance(lk, lookups.LessThanOrEqual):
            ke = format_date(lk.rhs.date(), 'full', locale='id')
    
    if dari.strip() == ke.strip():
        ke = ' '
    else:
        dari = dari + " - "

    thepath = 'survey/templates/datasets/rawdataset.html'
    df['Rating Fasilitas'] = (
        df['kelengkapan_fasilitas_rate']
        + df['kebersihan_fasilitas_rate']
        + df['kenyamanan_fasilitas_rate']
        + df['kamarmandi_fasilitas_rate']
        + df['kualitas_fasilitas_rate']) / 5
    df['Rating Perawat'] = (
        df['etika_perawat_rate']
        + df['penampilan_perawat_rate']
        + df['kecakapan_perawat_rate']
        + df['ketepatan_perawat_rate']
        + df['komunikatif_perawat_rate']) / 5
    df['Rating Dokter'] = (
        df['etika_dokter_rate']
        + df['penampilan_dokter_rate']
        + df['kecakapan_dokter_rate']
        + df['ketepatan_dokter_rate']
        + df['solutif_dokter_rate']) / 5
    df['Rating Farmasi'] = (
        df['etika_farmasi_rate']
        + df['penampilan_farmasi_rate']
        + df['kecepatan_farmasi_rate']
        + df['ketepatan_farmasi_rate']
        + df['informatif_farmasi_rate']) / 5
    df['Rating Total'] = (
        df['kelengkapan_fasilitas_rate']
        + df['kebersihan_fasilitas_rate']
        + df['kenyamanan_fasilitas_rate']
        + df['kamarmandi_fasilitas_rate']
        + df['kualitas_fasilitas_rate']
        + df['etika_perawat_rate']
        + df['penampilan_perawat_rate']
        + df['kecakapan_perawat_rate']
        + df['ketepatan_perawat_rate']
        + df['komunikatif_perawat_rate']
        + df['etika_dokter_rate']
        + df['penampilan_dokter_rate']
        + df['kecakapan_dokter_rate']
        + df['ketepatan_dokter_rate']
        + df['solutif_dokter_rate']
        + df['etika_farmasi_rate']
        + df['penampilan_farmasi_rate']
        + df['kecepatan_farmasi_rate']
        + df['ketepatan_farmasi_rate']
        + df['informatif_farmasi_rate']) / 20
    dfnew = df[['No', 'Tanggal', 'Rating Fasilitas', 'Rating Perawat', 
               'Rating Dokter', 'Rating Farmasi', 'Rating Total']].copy()
    rata_rata_fasilitas = round(dfnew.loc[:, 'Rating Fasilitas'].mean(), 2)
    rata_rata_perawat = round(dfnew.loc[:, 'Rating Perawat'].mean(), 2)
    rata_rata_dokter = round(dfnew.loc[:, 'Rating Dokter'].mean(), 2)
    rata_rata_farmasi = round(dfnew.loc[:, 'Rating Farmasi'].mean(), 2)
    rata_rata_total = round(dfnew.loc[:, 'Rating Total'].mean(), 2)
    dfnew.loc[len(dfnew.index)] = [
        "",
        "Rata-rata",
        str(rata_rata_fasilitas).replace('.', ','),
        str(rata_rata_perawat).replace('.', ','),
        str(rata_rata_dokter).replace('.', ','),
        str(rata_rata_farmasi).replace('.', ','),
        str(rata_rata_total).replace('.', ','),
    ]
    dfnew.loc[len(dfnew.index)] = [
        "",
        "Tingkat Kepuasan",
        get_quality_values(rata_rata_fasilitas),
        get_quality_values(rata_rata_perawat),
        get_quality_values(rata_rata_dokter),
        get_quality_values(rata_rata_farmasi),
        get_quality_values(rata_rata_total),
    ]
    Path(thepath).parent.mkdir(exist_ok=True)
    dfnew.to_html(
        'survey/Templates/datasets/rawdataset_rev.html',
        index=False,
        classes="mystyle"
    )
    logo_path = "survey/static/survey/assets_frontend/img/kardinah.png"
    # data_base64 = ""
    # if Path(logo_path).exists():
    #     data = open(logo_path, 'rb').read() # read bytes from file
    #     data_base64 = base64.b64encode(data)  # encode to base64 (bytes)
    #     data_base64 = data_base64.decode()    # convert bytes to string
    direktur = Pegawai.objects.filter(
        jenis_pegawai='00').order_by('-created_at')
    if len(direktur) != 0:
        direktur = direktur[0].nama
    else:
        direktur = "Kosong"
    context = {
        'dari': dari, 'ke': ke, 'tanggal': tanggal, 'direktur': direktur,
        'logo_kardinah': Path(logo_path).absolute().__str__()
    }
    out = render_to_string(
        request=request,
        template_name="datasets/report_template_rev.html",
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
                 queryset: QuerySet[SurveiKepuasanMasyarakatRev]):
        if self.value() == '01':
            return export_to_pdf_survey_rev(
                request=request, queryset=queryset)
        else:
            return queryset
