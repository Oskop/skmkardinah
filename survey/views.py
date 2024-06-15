from django.shortcuts import render
from django.http import request
from django.http import JsonResponse

from survey.controllers.pasiens import get_pasien_by_norm
from survey.controllers.kamars import get_pemakaiankamar_by
from survey.controllers.surveys import input_survey

# Create your views here.
def survey_index(request: request.HttpRequest):
    return render(request=request, template_name="frontend/index.html")


def current_survey_environment_by_norm(request: request.HttpRequest):
    response = {"success": False, "error": "", "data": {}}
    if request.method == 'GET':
        if request.POST.get('norm', None):
            pasien = get_pasien_by_norm(norm=request.POST.get('norm', None))
            if type(pasien) != "string" and pasien is not None:
                kamar, error = get_pemakaiankamar_by(pasien)
                if kamar:
                    response["data"].update(
                        {"ruangan":
                         kamar.id_tempattidur.id_kamar.id_ruangan.nama})
                    response["data"].update({"NoRM": pasien.nocm})
                    response["data"].update({"pasien": pasien.nama})
                    response["data"].update({"noregistrasi":
                                             kamar.id_registrasi_id})
            else:
                response["error"] += f"{pasien}<br>"
    else:
        response['error'] = "method not allowed"
    return JsonResponse(response)


def survey_input(request: request.HttpRequest):
    response = {"success": "", "error": "", "data": []}
    if request.method == 'POST':
        success, message = input_survey(request.POST)
        if success:
            response["success"] = True
        else:
            response["error"] = message
    else:
        response["error"] = "method not allowed"
    return JsonResponse(response)