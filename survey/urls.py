from django.urls import path
from survey.views import (
    survey_index, survey_input,
    current_survey_environment_by_norm)
from survey.apps import SurveyConfig

urlpatterns = [
    path("home/", survey_index, name="survey-home"),
    path("kirim/", survey_input, name="survey-kirim"),
    path("kirim/<int:id_registrasi>", survey_input, name="survey-kirim-with-id"),
    path("riwayatpelayanan/", 
         current_survey_environment_by_norm,
         name="survey-riwayat-pelayanan"),
    path("riwayatpelayanan/<str:norm>", 
         current_survey_environment_by_norm,
         name="survey-riwayat-pelayanan-with-norm"),
]