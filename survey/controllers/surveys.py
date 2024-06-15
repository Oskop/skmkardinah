from survey.models import SurveiKepuasanMasyarakat, Registrasi


def input_survey(post):
    success, error = False, None
    if post.get('id_registrasi', None):
        try:
            registrasi = Registrasi.objects.get(id=post['id_registrasi'])
            thesurvey = SurveiKepuasanMasyarakat(
                id_registrasi=registrasi,
                fasilitas_rate=post.get('fasilitas_rate', 0),
                perawat_rate=post.get('perawat_rate', 0),
                dokter_rate=post.get('dokter_rate', 0),
                farmasi_rate=post.get('farmasi_rate', 0),
                komentar=post.get('komentar', None),
            )
            thesurvey.save()
            if thesurvey.id is not None:
                success = True
        except Registrasi.DoesNotExist:
            error = "Id Registrasi tidak ditemukan"
    else:
        error = "id_registrasi tidak terkirim"
    return success, error