from django.urls import path, re_path
from survey.views import (
    survey_index, survey_input, survey_input_rev,
    current_survey_environment_by_norm,
    stt_survey, laporan_export_endpoint,
    survey_stt_direct)
from survey.apps import SurveyConfig
from survey.select2 import (
    KelurahanAutocomplete, KecamatanAutocomplete,
    KotaKabAutocomplete, ProvinsiAutocomplete,
    InstalasiAutocomplete, RuanganAutocomplete,
    KamarAutocomplete, TempatTidurAutocomplete,
    PasienAutocomplete, KelasPelayananAutocomplete,
    RegistrasiAutocomplete,
)

urlpatterns = [
    path("home/", survey_index, name="survey-home"),
    path("kirim/", survey_input, name="survey-kirim"),
    path("kirim/<int:id_registrasi>", survey_input,
         name="survey-kirim-with-id"),
    path("kirim-rev/", survey_input_rev, name="survey-kirim-rev"),
    path("kirim-rev/<int:id_registrasi>", survey_input_rev, 
         name="survey-kirim-rev-with-id"),
    path("stt-direct/", survey_stt_direct, name="survey-stt-direct"),
    path("stt/", stt_survey, name="survey-stt"),
    path("stt/<int:id_skm>", stt_survey, name="survey-stt-with-id"),
    path("laporan/export/pdf", 
         laporan_export_endpoint,
         name="survey-laporan-export-pdf"),
    path("riwayatpelayanan/", 
         current_survey_environment_by_norm,
         name="survey-riwayat-pelayanan"),
    path("riwayatpelayanan/<str:norm>", 
         current_survey_environment_by_norm,
         name="survey-riwayat-pelayanan-with-norm"),
    
    re_path(
        r'kelurahan-autocomplete/$',
        KelurahanAutocomplete.as_view(),
        name='kelurahan-autocomplete',
    ),
    re_path(
        r'kecamatan-autocomplete/$',
        KecamatanAutocomplete.as_view(),
        name='kecamatan-autocomplete',
    ),
    re_path(
        r'kotakab-autocomplete/$',
        KotaKabAutocomplete.as_view(),
        name='kotakab-autocomplete',
    ),
    re_path(
        r'provinsi-autocomplete/$',
        ProvinsiAutocomplete.as_view(),
        name='provinsi-autocomplete',
    ),
    re_path(
        r'instalasi-autocomplete/$',
        InstalasiAutocomplete.as_view(),
        name='instalasi-autocomplete',
    ),
    re_path(
        r'ruangan-autocomplete/$',
        RuanganAutocomplete.as_view(),
        name='ruangan-autocomplete',
    ),
    re_path(
        r'kamar-autocomplete/$',
        KamarAutocomplete.as_view(),
        name='kamar-autocomplete',
    ),
    re_path(
        r'tempattidur-autocomplete/$',
        TempatTidurAutocomplete.as_view(),
        name='tempattidur-autocomplete',
    ),
    re_path(
        r'pasien-autocomplete/$',
        PasienAutocomplete.as_view(),
        name='pasien-autocomplete',
    ),
    re_path(
        r'kelaspelayanan-autocomplete/$',
        KelasPelayananAutocomplete.as_view(),
        name='kelaspelayanan-autocomplete',
    ),
    re_path(
        r'registrasi-autocomplete/$',
        RegistrasiAutocomplete.as_view(),
        name='registrasi-autocomplete',
    ),
]