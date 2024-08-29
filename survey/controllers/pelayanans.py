from survey.models import (
    Pelayanan, Pegawai, JenisPegawai,
    Pasien, Registrasi)
from django.db.models import QuerySet


def get_dokters_from_pelayanan(pasien: Pasien):
    error = ""
    dokters = []
    reg: QuerySet[Registrasi] = Registrasi.objects.filter(
        norm=pasien.nocm).order_by('-tglregistrasi')
    if reg.count() != 0:
        pelayanans: QuerySet[Pelayanan] = reg[0].pelayanan_set.all(
        ).order_by('-tgllayanan')
        if pelayanans.count() !=0:
            for pelayanan in pelayanans:
                if pelayanan.id_pegawai:
                    if pelayanan.id_pegawai.jenis_pegawai_id == '01':
                        if (pelayanan.id_pegawai_id,
                            pelayanan.id_pegawai.nama) not in dokters:
                            dokters.append((pelayanan.id_pegawai_id,
                                            pelayanan.id_pegawai.nama))
        else:
            error = "Pasien belum mendapatkan pelayanan!"
    else:
        error = "Pasien belum melakukan registrasi!"
    return dokters, error


def get_perawattimes_from_pelayanan(pasien: Pasien):
    error = ""
    pelayanantimes = []
    reg: QuerySet[Registrasi] = Registrasi.objects.filter(
        norm=pasien.nocm).order_by('-tglregistrasi')
    if reg.count() != 0:
        pelayanans: QuerySet[Pelayanan] = reg[0].pelayanan_set.all(
        ).order_by('-tgllayanan')
        if pelayanans.count() !=0:
            for pelayanan in pelayanans:
                if pelayanan.id_pegawai:
                    if pelayanan.id_pegawai.jenis_pegawai_id == '02':
                        pelayanantimes.append(
                            (pelayanan.id, pelayanan.tgllayanan.strftime(
                                '%Y-%m-%d %H:%M:%S')))
        else:
            error = "Pasien belum mendapatkan pelayanan dari perawat!"
    else:
        error = "Pasien belum melakukan registrasi!"
    return pelayanantimes, error