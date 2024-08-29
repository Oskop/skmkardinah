from ninja.router import Router
from django.http import HttpRequest
from babel.dates import format_datetime

from survey.models import (
    Instalasi,
    JenisPegawai,
    Kamar,
    KelasPelayanan,
    Layanan,
    Pegawai,
    Pasien,
    Pelayanan,
    Registrasi,
    PemakaianKamar,
    Ruangan,
    TempatTidur,
)

skm_api_router = Router()

@skm_api_router.get(
        '/instalasi', url_name='skm_api_instalasi_get_all')
def daftar_instalasi(request: HttpRequest):
    response = {'success': True, 'error': '', 'data': [
        {"id": e.id, "nama": e.nama}
        for e in Instalasi.objects.all()
    ]}
    return response


@skm_api_router.get(
        '/instalasi/{id_instalasi}', url_name='skm_api_instalasi_get_id')
def item_instalasi(request: HttpRequest, id_instalasi: str):
    response = {'success': False, 'error': '', 'data': None}
    instalasi = Instalasi.objects.filter(id=id_instalasi)
    if len(instalasi) == 1:
        response['data'] = [
            {"id": e.id, "nama": e.nama}
            for e in instalasi
        ]
        response['success'] = True
    else:
        response['error'] = "instalasi tidak ditemukan"
    return response


@skm_api_router.get(
        '/jenispegawai', url_name='skm_api_jenispegawai_get_all')
def daftar_jenispegawai(request: HttpRequest):
    response = {'success': True, 'error': '', 'data': [
        {"id": e.id, "nama": e.nama}
        for e in JenisPegawai.objects.all()
    ]}
    return response


@skm_api_router.get(
        '/jenispegawai/{id_jenispegawai}',
        url_name='skm_api_jenispegawai_get_id')
def item_jenispegawai(request: HttpRequest, id_jenispegawai: str):
    response = {'success': False, 'error': '', 'data': None}
    jenispegawai = JenisPegawai.objects.filter(id=id_jenispegawai)
    if len(jenispegawai) == 1:
        response['data'] = [
            {"id": e.id, "nama": e.nama}
            for e in jenispegawai
        ]
        response['success'] = True
    else:
        response['error'] = "Jenis Pegawai tidak ditemukan"
    return response


@skm_api_router.get(
        '/kamar', url_name='skm_api_kamar_get_all')
def daftar_kamar(request: HttpRequest):
    response = {'success': True, 'error': '', 'data': [
        {"id": e.id, "nama": e.nama}
        for e in Kamar.objects.all()
    ]}
    return response


@skm_api_router.get(
        '/kamar/{id_kamar}',
        url_name='skm_api_kamar_get_id')
def item_kamar(request: HttpRequest, id_kamar: str):
    response = {'success': False, 'error': '', 'data': None}
    kamar = Kamar.objects.filter(id=id_kamar)
    if len(kamar) == 1:
        response['data'] = [
            {"id": e.id, "nama": e.nama}
            for e in kamar
        ]
        response['success'] = True
    else:
        response['error'] = "Kamar tidak ditemukan"
    return response


@skm_api_router.get(
        '/kelaspelayanan', url_name='skm_api_kelaspelayanan_get_all')
def daftar_kelaspelayanan(request: HttpRequest):
    response = {'success': True, 'error': '', 'data': [
        {"id": e.id, "nama": e.nama}
        for e in KelasPelayanan.objects.all()
    ]}
    return response


@skm_api_router.get(
        '/kelaspelayanan/{id_kelaspelayanan}',
        url_name='skm_api_kelaspelayanan_get_id')
def item_kelaspelayanan(request: HttpRequest, id_kelaspelayanan: str):
    response = {'success': False, 'error': '', 'data': None}
    kelaspelayanan = KelasPelayanan.objects.filter(
        id=id_kelaspelayanan)
    if len(kelaspelayanan) == 1:
        response['data'] = [
            {"id": e.id, "nama": e.nama}
            for e in kelaspelayanan
        ]
        response['success'] = True
    else:
        response['error'] = "Kelas Pelayanan tidak ditemukan"
    return response


@skm_api_router.get(
        '/layanan', url_name='skm_api_layanan_get_all')
def daftar_layanan(request: HttpRequest):
    response = {'success': True, 'error': '', 'data': [
        {"id": e.id, "nama": e.nama}
        for e in Layanan.objects.all()
    ]}
    return response


@skm_api_router.get(
        '/layanan/{id_layanan}',
        url_name='skm_api_layanan_get_id')
def item_layanan(request: HttpRequest, id_layanan: str):
    response = {'success': False, 'error': '', 'data': None}
    layanan = Layanan.objects.filter(
        id=id_layanan)
    if len(layanan) == 1:
        response['data'] = [
            {"id": e.id, "nama": e.nama}
            for e in layanan
        ]
        response['success'] = True
    else:
        response['error'] = "Layanan tidak ditemukan"
    return response


@skm_api_router.get(
        '/pegawai', url_name='skm_api_pegawai_get_all')
def daftar_pegawai(request: HttpRequest):
    response = {'success': True, 'error': '', 'data': [
        {"id": e.id, "nama": e.nama}
        for e in Pegawai.objects.all()
    ]}
    return response


@skm_api_router.get(
        '/pegawai/{id_pegawai}',
        url_name='skm_api_pegawai_get_id')
def item_pegawai(request: HttpRequest, id_pegawai: str):
    response = {'success': False, 'error': '', 'data': None}
    pegawai = Pegawai.objects.filter(
        id=id_pegawai)
    if len(pegawai) == 1:
        response['data'] = [
            {"id": e.id, "nama": e.nama}
            for e in pegawai
        ]
        response['success'] = True
    else:
        response['error'] = "Pegawai tidak ditemukan"
    return response


# @skm_api_router.get(
#         '/pasien', url_name='skm_api_pasien_get_all')
# def daftar_pasien(request: HttpRequest):
#     response = {'success': True, 'error': '', 'data': [
#         {"id": e.id, "nama": e.nama}
#         for e in Pasien.objects.all()
#     ]}
#     return response


@skm_api_router.get(
        '/pasien/{norm}',
        url_name='skm_api_pasien_get_norm')
def item_pasien(request: HttpRequest, norm: str):
    response = {'success': False, 'error': '', 'data': None}
    pasien = Pasien.objects.filter(
        nocm=norm)
    if len(pasien) == 1:
        response['data'] = [
            {"id": e.id, "norm": e.nocm, "nama": e.nama}
            for e in pasien
        ]
        response['success'] = True
    else:
        response['error'] = "Pasien tidak ditemukan"
    return response


@skm_api_router.get(
        '/pelayanan', url_name='skm_api_pelayanan_get_all')
def daftar_pelayanan(request: HttpRequest):
    response = {'success': True, 'error': '', 'data': [
        {"id": e.id, "id_registrasi": e.id_registrasi_id,
         "tgllayanan": format_datetime(e.tgllayanan, 'full', locale='id_ID'),
         "id_pegawai": e.id_pegawai_id, "pegawai": e.id_pegawai.nama,
         "id_layanan": e.id_layanan_id, "layanan": e.id_layanan.nama,
         "id_pemakaiankamar": e.id_pemakaiankamar_id,
         "pemakaiankamar": str(
            f"Tempat Tidur: {e.id_pemakaiankamar.id_tempattidur.nama}, <br>" +
            f"Kamar: {e.id_pemakaiankamar.id_tempattidur.id_kamar.nama}, <br>"
            + f"Ruangan: {e.id_pemakaiankamar.id_tempattidur.id_kamar.id_ruangan.nama}"),
        } for e in Pelayanan.objects.all()
    ]}
    return response


@skm_api_router.get(
        '/pelayanan/{id_pelayanan}',
        url_name='skm_api_pelayanan_get_id')
def item_pelayanan(request: HttpRequest, id_pelayanan: int):
    response = {'success': False, 'error': '', 'data': None}
    pelayanan = Pelayanan.objects.filter(
        id=id_pelayanan)
    if len(pelayanan) == 1:
        response['data'] = [
            {"id": e.id, "id_registrasi": e.id_registrasi_id,
             "tgllayanan": format_datetime(e.tgllayanan, 'full', locale='id_ID'),
             "id_pegawai": e.id_pegawai_id, "pegawai": e.id_pegawai.nama,
             "id_layanan": e.id_layanan_id, "layanan": e.id_layanan.nama,
             "id_pemakaiankamar": e.id_pemakaiankamar_id,
             "pemakaiankamar": str(
                 f"Tempat Tidur: {e.id_pemakaiankamar.id_tempattidur.nama}, <br>"
                 + f"Kamar: {e.id_pemakaiankamar.id_tempattidur.id_kamar.nama}, <br>"
                 + f"Ruangan: {e.id_pemakaiankamar.id_tempattidur.id_kamar.id_ruangan.nama}"),
            } for e in pelayanan 
        ]
        response['success'] = True
    else:
        response['error'] = "Pelayanan tidak ditemukan"
    return response


@skm_api_router.get(
        '/registrasi', url_name='skm_api_registrasi_get_all')
def daftar_registrasi(request: HttpRequest):
    response = {'success': True, 'error': '', 'data': [
        {"id": e.id, "norm": e.norm_id, "nama": e.norm.nama,
         "id_kelas": e.id_kelas_id, "kelaspelayanan": e.id_kelas.nama,
         "tglregistrasi": format_datetime(
             e.tglregistrasi, 'full', locale='id_ID'),
         "tglpulang": format_datetime(
             e.tglpulang, 'full', locale='id_ID'),
        }
        for e in Registrasi.objects.all()
    ]}
    return response


@skm_api_router.get(
        '/registrasi/{id_registrasi}',
        url_name='skm_api_registrasi_get_id')
def item_registrasi(request: HttpRequest, id_registrasi: int):
    response = {'success': False, 'error': '', 'data': None}
    registrasi = Registrasi.objects.filter(
        id=id_registrasi)
    if len(registrasi) == 1:
        response['data'] = [
            {"id": e.id, "norm": e.norm_id, "nama": e.norm.nama,
             "id_kelas": e.id_kelas_id, "kelaspelayanan": e.id_kelas.nama,
             "tglregistrasi": format_datetime(
                 e.tglregistrasi, 'full', locale='id_ID'),
             "tglpulang": format_datetime(
                 e.tglpulang, 'full', locale='id_ID'),
            } for e in registrasi
        ]
        response['success'] = True
    else:
        response['error'] = "Registrasi tidak ditemukan"
    return response


@skm_api_router.get(
        '/pemakaiankamar', url_name='skm_api_pemakaiankamar_get_all')
def daftar_pemakaiankamar(request: HttpRequest):
    response = {'success': True, 'error': '', 'data': [
        {"id": e.id, 
         "tglmasuk": format_datetime(e.tglmasuk, 'full', locale='id_ID'),
         "tglkeluar": format_datetime(e.tglkeluar, 'full', locale='id_ID'),
         "id_tempattidur": e.id_tempattidur_id,
         "tempattidur": str(
            f"Tempat Tidur: {e.id_tempattidur.nama}, <br>" +
            f"Kamar: {e.id_tempattidur.id_kamar.nama}, <br>"
            + f"Ruangan: {e.id_tempattidur.id_kamar.id_ruangan.nama}"),
        }
        for e in PemakaianKamar.objects.all()
    ]}
    return response


@skm_api_router.get(
        '/pemakaiankamar/{id_pemakaiankamar}',
        url_name='skm_api_pemakaiankamar_get_id')
def item_pemakaiankamar(request: HttpRequest, id_pemakaiankamar: int):
    response = {'success': False, 'error': '', 'data': None}
    pemakaiankamar = PemakaianKamar.objects.filter(
        id=id_pemakaiankamar)
    if len(pemakaiankamar) == 1:
        response['data'] = [{"id": e.id, 
         "tglmasuk": format_datetime(e.tglmasuk, 'full', locale='id_ID'),
         "tglkeluar": format_datetime(e.tglkeluar, 'full', locale='id_ID'),
         "id_tempattidur": e.id_tempattidur_id,
         "tempattidur": str(
            f"Tempat Tidur: {e.id_tempattidur.nama}, <br>" +
            f"Kamar: {e.id_tempattidur.id_kamar.nama}, <br>"
            + f"Ruangan: {e.id_tempattidur.id_kamar.id_ruangan.nama}"),
        }
        for e in pemakaiankamar]
        response['success'] = True
    else:
        response['error'] = "Pemakaian Kamar tidak ditemukan"
    return response


@skm_api_router.get(
        '/ruangan', url_name='skm_api_ruangan_get_all')
def daftar_ruangan(request: HttpRequest):
    response = {'success': True, 'error': '', 'data': [
        {"id": e.id, "nama": e.nama}
        for e in Ruangan.objects.all()
    ]}
    return response


@skm_api_router.get(
        '/ruangan/{id_ruangan}',
        url_name='skm_api_ruangan_get_id')
def item_ruangan(request: HttpRequest, id_ruangan: str):
    response = {'success': False, 'error': '', 'data': None}
    ruangan = Ruangan.objects.filter(
        id=id_ruangan)
    if len(ruangan) == 1:
        response['data'] = [
            {"id": e.id, "nama": e.nama}
            for e in ruangan
        ]
        response['success'] = True
    else:
        response['error'] = "Ruangan tidak ditemukan"
    return response


@skm_api_router.get(
        '/tempattidur', url_name='skm_api_tempattidur_get_all')
def daftar_tempattidur(request: HttpRequest):
    response = {'success': True, 'error': '', 'data': [
        {"id": e.id, "nama": e.nama}
        for e in TempatTidur.objects.all()
    ]}
    return response


@skm_api_router.get(
        '/tempattidur/{id_tempattidur}',
        url_name='skm_api_tempattidur_get_id')
def item_tempattidur(request: HttpRequest, id_tempattidur: str):
    response = {'success': False, 'error': '', 'data': None}
    tempattidur = TempatTidur.objects.filter(
        id=id_tempattidur)
    if len(tempattidur) == 1:
        response['data'] = [
            {"id": e.id, "nama": e.nama}
            for e in tempattidur
        ]
        response['success'] = True
    else:
        response['error'] = "Tempat Tidur tidak ditemukan"
    return response