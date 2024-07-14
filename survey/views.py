from django.shortcuts import render
from django.contrib import messages
from django.http.request import HttpRequest
from django.http import (JsonResponse, HttpResponseRedirect)
from survey.controllers.pasiens import get_pasien_by_norm
from survey.controllers.kamars import get_pemakaiankamar_by
from survey.controllers.surveys import (input_survey, skm_stt)

# Create your views here.
def survey_index(request: HttpRequest):
    return render(request=request, template_name="frontend/index.html")


def current_survey_environment_by_norm(request: HttpRequest, norm: str = None):
    response = {"success": False, "error": "", "data": {}}
    if norm:
        if request.method == 'GET':
            pasien = get_pasien_by_norm(norm=norm)
            if not isinstance(pasien, str):
                kamar, error = get_pemakaiankamar_by(pasien)
                if kamar:
                    response["data"].update(
                        {"ruangan":
                            kamar.id_tempattidur.id_kamar.id_ruangan.nama})
                    response["data"].update({"norm": pasien.nocm})
                    response["data"].update({"pasien": pasien.nama})
                    response["data"].update({"noregistrasi":
                                            kamar.id_registrasi_id})
                    response["success"] = True
                else:
                    response["error"] = error
            else:
                response["error"] = "Pasien tidak ditemukan"
        else:
            response['error'] = "Metode tidak diizinkan"
    else:
        response["error"] = "NoRM Tidak Terkirim!"
    return JsonResponse(response)


def survey_input(request: HttpRequest, id_registrasi = None):
    response = {"success": False, "error": "", "data": []}
    if id_registrasi != 0:
        if request.method == 'POST':
            success, message = input_survey(id_registrasi, request.POST, request.FILES)
            if success:
                response["success"] = True
            else:
                response["error"] = message
        else:
            response["error"] = "Tidak diizinkan"
    else:
        response["error"] = "Nomor Registrasi Pasien tidak terkirim"
    return JsonResponse(response)


def stt_survey(request: HttpRequest, id_skm: int = None):
    response = {"success": False, "error": "", "data": []}
    if id_skm != 0 and id_skm is not None:
        if request.method == 'GET':
            success, message = skm_stt(id_skm=id_skm)
            if success:
                messages.success(request, "Berhasil mengubah suara ke teks")
            else:
                messages.error(request, message)
        else:
            messages.error(request, "Tidak diizinkan")
    else:
        messages.warning(request, "Nomor Registrasi Pasien tidak terkirim")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))