from django.urls import path
from survey.views import survey_index
from survey.apps import SurveyConfig

urlpatterns = [
    path("home/", survey_index)
]