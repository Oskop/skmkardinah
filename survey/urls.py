from django.urls import path
from survey.views import (
    survey_index, survey_input,
    current_survey_environment_by_norm,
    stt_survey)
from survey.apps import SurveyConfig

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
]