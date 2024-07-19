from django.contrib.auth.models import Group
from django.contrib import admin
from django.utils import timezone
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import QuerySet
from django.utils.html import format_html
from survey import models
from survey.forms import (
    PasienForms, RegistrasiForms, PemakaianKamarForms,
    SurveiKepuasanMasyarakatForms)
from survey.controllers.surveys import get_voice_file
from survey.filters import (
    ReportExportFilter, export_to_pdf_survey)
from rangefilter.filters import DateTimeRangeFilter
from admincharts.admin import AdminChartMixin
from admincharts.utils import months_between_dates
from django_object_actions import (
    DjangoObjectActions, action, takes_instance_or_queryset)
# Register your models here.

admin.site.register([
    models.Instalasi, models.Kamar, models.Kecamatan,
    models.KelasPelayanan, models.Kelurahan,
    models.Kotakab,
    models.Provinsi,
    models.TempatTidur])

admin.site.unregister(Group)


@admin.register(models.Ruangan)
class RuanganAdmin(admin.ModelAdmin):
    # list_display = [x.attname.replace(
    #     'survey.Ruangan.', ''
    # ) for x in models.Ruangan._meta.fields]
    list_display = ['id', 'nama', 'id_instalasi']
    # list_filter = (('mode', DateTimeRangeFilter),)
    search_fields = [x.attname.replace(
        'survey.Ruangan.', ''
    ) for x in models.Ruangan._meta.fields if (
        '_id' not in x.attname)]
    list_per_page = 10

@admin.register(models.Pasien)
class PasienAdmin(admin.ModelAdmin):
    # list_display = [x.attname.replace(
    #     'demr.Pasien.', ''
    # ) for x in models.Pasien._meta.fields if (
    #     'id_tmp_lahir_id' not in x.attname)] + [
    #         'get_tempat_lahir',
    #     ]
    list_display = [
        'nik', 'nocm', 'nama', 'id_tmp_lahir', 'tgl_lahir',
        'alamat', 'rt', 'rw', 'get_alamat_dom']
    # list_filter = (('mode', DateTimeRangeFilter),)
    search_fields = [x.attname.replace(
        'survey.Pasien.', ''
    ) for x in models.Pasien._meta.fields if (
        '_id' not in x.attname)]
    form = PasienForms
    
    # @admin.display(ordering='id_tmp_lahir__nama',
    #                description='Tempat Lahir')
    # def get_tempat_lahir(self, obj: models.Pasien):
    #     return str(obj.id_tmp_lahir)

    @admin.display(ordering='id_kelurahan__nama',
                   description='Domisili Daerah')
    def get_alamat_dom(self, obj: models.Pasien):
        return str(
            f"{obj.id_kelurahan}, " + f"{obj.id_kelurahan.id_kecamatan}, "
            + f"{obj.id_kelurahan.id_kecamatan.id_kotakab}, "
            + f"{obj.id_kelurahan.id_kecamatan.id_kotakab.id_provinsi}")

    list_per_page = 10


@admin.register(models.Registrasi)
class RegistrasiAdmin(admin.ModelAdmin):
    # list_display = [x.attname.replace(
    #     'survey.Registrasi.', ''
    # ) for x in models.Registrasi._meta.fields]
    list_display = ['id', 'norm', 'id_kelas', 'tglregistrasi', 'tglpulang']
    # list_filter = (('mode', DateTimeRangeFilter),)
    search_fields = [x.attname.replace(
        'survey.Registrasi.', ''
    ) for x in models.Registrasi._meta.fields if (
        '_id' not in x.attname)]
    list_per_page = 10
    form = RegistrasiForms


@admin.register(models.PemakaianKamar)
class PemakaianKamarAdmin(admin.ModelAdmin):
    # list_display = [x.attname.replace(
    #     'survey.PemakaianKamar.', ''
    # ) for x in models.PemakaianKamar._meta.fields]
    # list_filter = (('mode', DateTimeRangeFilter),)
    list_display = [
        "id_registrasi", "tglmasuk", "get_tempattidur", "tglkeluar"]
    search_fields = [x.attname.replace(
        'survey.PemakaianKamar.', ''
    ) for x in models.PemakaianKamar._meta.fields if (
        '_id' not in x.attname)]
    
    @admin.display(ordering='id_tempattidur__id',
                   description='Tempat Tidur')
    def get_tempattidur(self, obj: models.PemakaianKamar):
        return str(
            f"Kasur {obj.id_tempattidur.nama}, " + f"Kamar {obj.id_tempattidur.id_kamar}, "
            + f"Ruangan {obj.id_tempattidur.id_kamar.id_ruangan}")
    
    list_per_page = 10

    form = PemakaianKamarForms

@admin.register(models.SurveiKepuasanMasyarakat)
class SurveiKepuasanMasyarakatAdmin(
    AdminChartMixin, admin.ModelAdmin, 
    # DjangoObjectActions
    ):
    
    # actions = [laporan,]
    change_list_template = "chartjs/djangoobjecttools_change_list.html"


    # def changelist_view(self, request, extra_context=None):
    #     extra_context = extra_context or {}
    #     # extra_context.update(
    #     #     {
    #     #         "objectactions": [
    #     #             self._get_tool_dict(action)
    #     #             for action in self.get_changelist_actions(request)
    #     #         ],
    #     #         "tools_view_name": self.tools_view_name,
    #     #     }
    #     # )
    #     response = super().changelist_view(request, extra_context=extra_context)

    #     # This could be a redirect and not have context_data
    #     if not hasattr(response, "context_data"):
    #         return response

    #     if "cl" in response.context_data:
    #         changelist = response.context_data["cl"]
    #         chart_queryset = self.get_list_chart_queryset(changelist)
    #         response.context_data["adminchart_queryset"] = chart_queryset
    #         response.context_data[
    #             "adminchart_chartjs_config"
    #         ] = self.get_list_chart_config(chart_queryset)
    #     else:
    #         response.context_data["adminchart_queryset"] = None
    #         response.context_data["adminchart_chartjs_config"] = None

    #     return response


    # This will help you to disbale add functionality
    def has_add_permission(self, request):
        return False

    # This will help you to disable delete functionaliyt
    def has_delete_permission(self, request, obj=None):
        return False
    
    # Chartsj
    def get_list_chart_data(
            self, queryset: QuerySet[models.SurveiKepuasanMasyarakat]):
        if not queryset:
            return {}

        # Cannot reorder the queryset at this point
        earliest = min([x.created_at for x in queryset])

        labels = []
        farmasi_totals = []
        perawat_totals = []
        dokter_totals = []
        fasilitas_totals = []
        for b in months_between_dates(earliest, timezone.now()):
            labels.append(b.strftime("%b %Y"))
            farmasi_totals.append(
                sum(
                    [
                        x.farmasi_rate
                        for x in queryset
                        if x.created_at.year == b.year and x.created_at.month == b.month
                    ]
                )
            )
            fasilitas_totals.append(
                sum(
                    [
                        x.fasilitas_rate
                        for x in queryset
                        if x.created_at.year == b.year and x.created_at.month == b.month
                    ]
                )
            )
            perawat_totals.append(
                sum(
                    [
                        x.perawat_rate
                        for x in queryset
                        if x.created_at.year == b.year and x.created_at.month == b.month
                    ]
                )
            )
            dokter_totals.append(
                sum(
                    [
                        x.dokter_rate
                        for x in queryset
                        if x.created_at.year == b.year and x.created_at.month == b.month
                    ]
                )
            )

        return {
            "labels": labels,
            "datasets": [
                {"label": "Fasilitas", "data": fasilitas_totals, "backgroundColor": "#B4B4B4"},
                {"label": "Perawat", "data": perawat_totals, "backgroundColor": "#EB4FD8"},
                {"label": "Dokter", "data": dokter_totals, "backgroundColor": "#4472C4"},
                {"label": "Farmasi", "data": farmasi_totals, "backgroundColor": "#F07F46"},
            ],
        }
    
    def get_list_chart_queryset(self, changelist):
        return changelist.queryset
    
    
    list_display = [x.attname.replace(
        'survey.SurveiKepuasanMasyarakat.', ''
    ) for x in models.SurveiKepuasanMasyarakat._meta.fields]
    list_display = [
        'id', 'get_registrasi',
        'fasilitas_rate', 'perawat_rate', 'dokter_rate', 'farmasi_rate',
        'komentar', 'get_voice', 'created_at', 'get_stt']
    list_filter = (('created_at', DateTimeRangeFilter),
                   ReportExportFilter)
    search_fields = [x.attname.replace(
        'survey.SurveiKepuasanMasyarakat.', ''
    ) for x in models.SurveiKepuasanMasyarakat._meta.fields if (
        '_id' not in x.attname)]
    @admin.display(ordering='id_registrasi__id',
                   description='Registrasi Pasien')
    def get_registrasi(self, obj: models.SurveiKepuasanMasyarakat):
        return str(
            f"{obj.id_registrasi.id} "
            + f"{obj.id_registrasi.norm.nocm} "
            + f"{obj.id_registrasi.norm.nama}, "
            # + f"Kelas {obj.id_tempattidur.id_kamar.id_ruangan}"
            )
    
    @admin.display(ordering='komentar',
                   description='Komentar Suara')
    def get_voice(self, obj: models.SurveiKepuasanMasyarakat):
        # print('obj.komentar_suara.name is not None', obj.komentar_suara.name != "", len(obj.komentar_suara.name))
        if (isinstance(obj.komentar_suara.name, str
                       ) and obj.komentar_suara.name != ""
            ) and obj.komentar_suara.name is not None:
            return format_html(f'<audio controls name="media">'
                            +f'<source src="{obj.komentar_suara.url}" '
                            +'></audio>')
        else:
            return "Tidak ada file komentar suara"
        

    @admin.display(ordering='komentar',
                   description='Aksi')
    def get_stt(self, obj: models.SurveiKepuasanMasyarakat):
        return format_html(str(
            f'<a href="{reverse("survey-stt-with-id", args=[obj.id,])}"'
            +' class="button btn btn-primary">SkT</a>'
        ))
    list_per_page = 10
    
    form = SurveiKepuasanMasyarakatForms
    actions = ["laporan_survey_pdf",]

    @admin.action(description="Laporan Survey")
    def laporan_survey_pdf(self, request, queryset):
        print('ada redirect atau tidak?')
        print(export_to_pdf_survey(request, queryset))
        return HttpResponseRedirect('/')


    # @action(
    #     label="Unduh Laporan (pdf)",  # optional
    #     description="Laporan Survey dalam format PDF" # optional
    # )
    
    # change_actions = ('laporan', )
    # changelist_actions = ('laporan_survey_pdf', )
