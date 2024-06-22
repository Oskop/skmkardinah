from django.urls import path
from survey.views import survey_index, survey_input
from survey.apps import SurveyConfig

urlpatterns = [
    path("home/", survey_index),
    path("kirim/", survey_input),
]