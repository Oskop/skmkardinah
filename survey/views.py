from django.shortcuts import render
from django.http import request
from django.http import JsonResponse

# Create your views here.
def survey_index(request: request.HttpRequest):
    return render(request=request, template_name="frontend/index.html")


def current_survey_environment_by_norm(request: request.HttpRequest):
    response = {"success": False, "error": "", "data": []}
    if request.method == 'GET':
        request.POST.get('norm')
    else:
        response['error'] = "method not allowed"
    return JsonResponse(response)


def survey_input(request: request.HttpRequest):
    response = {"success": "", "error": "", "data": []}
    if request.method == 'POST':
        request.POST.get('norm')
    return JsonResponse(response)