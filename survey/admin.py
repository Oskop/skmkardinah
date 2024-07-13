from django.contrib import admin
from survey import models
# Register your models here.

admin.site.register([
    models.Instalasi, models.Kamar, models.Kecamatan,
    models.KelasPelayanan, models.Kelurahan,
    models.Kotakab,
    models.Provinsi,
    models.TempatTidur])


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

    
@admin.register(models.SurveiKepuasanMasyarakat)
class SurveiKepuasanMasyarakatAdmin(admin.ModelAdmin):
    list_display = [x.attname.replace(
        'survey.SurveiKepuasanMasyarakat.', ''
    ) for x in models.SurveiKepuasanMasyarakat._meta.fields]
    # list_filter = (('mode', DateTimeRangeFilter),)
    search_fields = [x.attname.replace(
        'survey.SurveiKepuasanMasyarakat.', ''
    ) for x in models.SurveiKepuasanMasyarakat._meta.fields if (
        '_id' not in x.attname)]
    list_per_page = 10
