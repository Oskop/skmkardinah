from django.contrib import admin
from survey import models
# Register your models here.

admin.site.register([
    models.Instalasi, models.Kamar, models.Kecamatan,
    models.KelasPelayanan, models.Kelurahan,
    models.Kotakab, models.Pasien, models.PemakaianKamar,
    models.Provinsi, models.Registrasi,
    models.Ruangan, models.SurveiKepuasanMasyarakat,
    models.TempatTidur])
