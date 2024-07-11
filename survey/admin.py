from django.contrib import admin
from survey import models
# Register your models here.

admin.site.register([
    models.Instalasi, models.Kamar, models.Kecamatan,
    models.KelasPelayanan, models.Kelurahan,
    models.Kotakab,
    models.Provinsi,
    models.Ruangan,
    models.TempatTidur])


@admin.register(models.Pasien)
class PasienAdmin(admin.ModelAdmin):
    list_display = [x.attname.replace(
        'demr.Pasien.', ''
    ) for x in models.Pasien._meta.fields]
    # list_filter = (('mode', DateTimeRangeFilter),)
    search_fields = [x.attname.replace(
        'satusehat.Pasien.', ''
    ) for x in models.Pasien._meta.fields if (
        '_id' not in x.attname)]
    list_per_page = 10


@admin.register(models.Registrasi)
class RegistrasiAdmin(admin.ModelAdmin):
    list_display = [x.attname.replace(
        'demr.Registrasi.', ''
    ) for x in models.Registrasi._meta.fields]
    # list_filter = (('mode', DateTimeRangeFilter),)
    search_fields = [x.attname.replace(
        'satusehat.Registrasi.', ''
    ) for x in models.Registrasi._meta.fields if (
        '_id' not in x.attname)]
    list_per_page = 10


@admin.register(models.PemakaianKamar)
class PemakaianKamarAdmin(admin.ModelAdmin):
    list_display = [x.attname.replace(
        'demr.PemakaianKamar.', ''
    ) for x in models.PemakaianKamar._meta.fields]
    # list_filter = (('mode', DateTimeRangeFilter),)
    search_fields = [x.attname.replace(
        'satusehat.PemakaianKamar.', ''
    ) for x in models.PemakaianKamar._meta.fields if (
        '_id' not in x.attname)]
    list_per_page = 10

    
@admin.register(models.SurveiKepuasanMasyarakat)
class SurveiKepuasanMasyarakatAdmin(admin.ModelAdmin):
    list_display = [x.attname.replace(
        'demr.SurveiKepuasanMasyarakat.', ''
    ) for x in models.SurveiKepuasanMasyarakat._meta.fields]
    # list_filter = (('mode', DateTimeRangeFilter),)
    search_fields = [x.attname.replace(
        'satusehat.SurveiKepuasanMasyarakat.', ''
    ) for x in models.SurveiKepuasanMasyarakat._meta.fields if (
        '_id' not in x.attname)]
    list_per_page = 10
