from survey.models import Pasien, Kamar, PemakaianKamar, Registrasi
from django.db.models import QuerySet


def get_pemakaiankamar_by(pasien: Pasien):
    error = ""
    reg: QuerySet[Registrasi] = Registrasi.objects.filter(
        norm=pasien.nocm).order_by('-tglregistrasi')
    if reg.count() != 0:
        pemakaiankamar: QuerySet[PemakaianKamar] = reg[0].pemakaiankamar_set.all(
        ).order_by('-tglmasuk')
        if pemakaiankamar.count() !=0:
            return pemakaiankamar, error
        else:
            error = "Pasien belum memasuki ruangan!"
    else:
        error = "Pasien belum melakukan registrasi!"
    return None, error