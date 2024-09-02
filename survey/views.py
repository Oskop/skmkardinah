from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from django.http.request import HttpRequest
from django.http import (
    JsonResponse, HttpResponseRedirect, HttpResponse)
from survey.controllers.pasiens import get_pasien_by_norm
from survey.controllers.kamars import get_pemakaiankamar_by
from survey.controllers.pelayanans import (
    get_dokters_from_pelayanan, get_perawattimes_from_pelayanan)
from survey.controllers.surveys import (
    input_survey, skm_stt, laporan_export_pdf,
    laporan_export_pdf_rev,
    handle_voice_direct, input_survey_rev)

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
                dokters, errordokter = get_dokters_from_pelayanan(pasien)
                timess, errortimess = get_perawattimes_from_pelayanan(pasien)
                ruangans = [k.id_tempattidur.id_kamar.id_ruangan.nama 
                            for k in kamar]
                if len(kamar) != 0:
                    response["data"].update(
                        {"ruangan": ruangans})
                    if len(dokters) != 0:
                        response["data"].update(
                            {"dokters": dokters})
                    else:
                        response["error"] = errordokter
                    if len(timess) != 0:
                        response["data"].update(
                            {"perawattimes": timess})
                    else:
                        response["error"] += f"\n {errortimess}"
                    response["data"].update({"norm": pasien.nocm})
                    response["data"].update({"pasien": pasien.nama})
                    response["data"].update({"noregistrasi":
                                            kamar[0].id_registrasi_id})
                    response["data"].update({"jk": pasien.jk})
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


def survey_input_rev(request: HttpRequest, id_registrasi = None):
    response = {"success": False, "error": "", "data": []}
    if id_registrasi != 0:
        if request.method == 'POST':
            success, message = input_survey_rev(
                id_registrasi, request.POST, request.FILES)
            if success:
                response["success"] = True
            else:
                response["error"] = message
        else:
            response["error"] = "Tidak diizinkan"
    else:
        response["error"] = "Nomor Registrasi Pasien tidak terkirim"
    return JsonResponse(response)


def survey_stt_direct(request: HttpRequest):
    response = {"success": False, "error": "", "data": []}
    if request.method == 'POST':
        if request.POST.get('norm', '') != '' and request.FILES.get(
            'voice') is not None:
            result = handle_voice_direct(
                request.FILES.get('voice'),
                request.POST.get('norm', ''))
            if result:
                response["data"] = [result,]
                response["success"] = True
            else:
                response["error"] = "gagal"
        else:
            response["error"] = "Nomor Rekam Medis Pasien tidak terkirim"
    else:
        response["error"] = "Tidak diizinkan"
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


def laporan_export_endpoint(request: HttpRequest):
    if request.method == "GET":
        dari = request.GET.get('dari', '')
        ke = request.GET.get('ke', '')
        return laporan_export_pdf_rev(request, dari, ke)
    else:
        messages.error(request, "Metode tidak diperbolehkan")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))