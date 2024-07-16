from django.urls import path, re_path
from survey.views import (
    survey_index, survey_input,
    current_survey_environment_by_norm,
    stt_survey)
from survey.apps import SurveyConfig
from survey.select2 import (
    KelurahanAutocomplete, KotaKabAutocomplete)

urlpatterns = [
    path("home/", survey_index, name="survey-home"),
    path("kirim/", survey_input, name="survey-kirim"),
    path("kirim/<int:id_registrasi>", survey_input, name="survey-kirim-with-id"),
    path("stt/", stt_survey, name="survey-stt"),
    path("stt/<int:id_skm>", stt_survey, name="survey-stt-with-id"),
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
        r'kotakab-autocomplete/$',
        KotaKabAutocomplete.as_view(),
        name='kotakab-autocomplete',
    ),
]