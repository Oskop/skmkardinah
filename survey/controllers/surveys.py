from survey.models import SurveiKepuasanMasyarakat, Registrasi
from survey.controllers.sherpa import predict_voice_text, ogg_to_wav
from survey.filters import export_to_pdf_survey
from django.core.files import File
from django.http import HttpResponse
from django.http.request import HttpRequest
import pathlib
from datetime import datetime
import base64


STT_TOKEN = '[[stt]]'


def get_voice_file(
        skm: SurveiKepuasanMasyarakat = None,
        id_skm: int = None, encoded: bool = True):
    assert skm is not None or id_skm is not None, str(
        "skm or id_skm parameter must be set!")
    if skm is None and id_skm is not None:
        skm = SurveiKepuasanMasyarakat.objects.get(id=id_skm)
    enc = None
    parent_dir = 'media/'
    voice_directory = 'survey/voices/'
    destination_dir = parent_dir + voice_directory
    filename = str(f"__{skm.id}__{skm.id_registrasi_id}"
                   + f"__{skm.id_registrasi.norm_id}")
    destination_folder = pathlib.Path(destination_dir)
    if destination_folder.exists():
        files = list(destination_folder.glob(f'*{filename}*'))
        try:
            filename = next(str(f) for f in files if str(f).endswith('.wav'))
        except StopIteration:
            try:
                filename = next(
                    str(f) for f in files if str(f).endswith('.ogg'))
            except StopIteration:
                filename = None
        if filename and encoded:
            enc = base64.b64encode(
                open(filename, "rb").read())
        elif filename and encoded is False:
            return filename
    return enc


def skm_stt(skm: SurveiKepuasanMasyarakat = None,
            id_skm: int = None):
    assert skm is not None or id_skm is not None, str(
        "skm or id_skm parameter must be set!")
    success, message = False, ""
    if skm is None and id_skm is not None:
        try:
            skm = SurveiKepuasanMasyarakat.objects.get(id=id_skm)
        except SurveiKepuasanMasyarakat.DoesNotExist:
            message = "Survey tidak ditemukan"
    if (isinstance(skm.komentar_suara.name, str
                       ) and skm.komentar_suara.name != ""
            ) and skm.komentar_suara.name is not None:
        result, success = predict_voice_text(skm.komentar_suara.path)
        if success:
            if len(skm.komentar.split(STT_TOKEN)) > 1:
                skm.komentar = skm.komentar.split(STT_TOKEN)[0]
            skm.komentar += f" {STT_TOKEN}{result}{STT_TOKEN}"
            skm.save()
            success = True
        else:
            message = "perubahan suara ke teks gagal"
    else:
        message = "file komentar suara tidak ada"
    return success, message


def handle_voice_direct(f, norm):
    parent_dir = 'media/'
    voice_directory = 'survey/voices/'
    destination_dir = parent_dir + voice_directory
    pathlib.Path(destination_dir).mkdir(parents=True, exist_ok=True)
    basefilename = str(
        str(datetime.now().timestamp())
        + '__' + norm)
    filename = f"{basefilename}.ogg"
    with open(str(destination_dir) + filename, "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    if pathlib.Path(str(destination_dir) + filename).exists():
        output_wav = filename[:-3] + "wav"
        if ogg_to_wav(
            str(destination_dir) + filename,
            str(destination_dir) + output_wav):
            result, success = predict_voice_text(
                str(destination_dir) + output_wav)
            if success:
                return result
    return None


def handle_voice_file(skm: SurveiKepuasanMasyarakat, f, stt = False):
    message = ""
    parent_dir = 'media/'
    voice_directory = 'survey/voices/'
    destination_dir = parent_dir + voice_directory
    pathlib.Path(destination_dir).mkdir(parents=True, exist_ok=True)
    basefilename = str(f"{skm.id}__{skm.id_registrasi_id}"
                   + f"__{skm.id_registrasi.norm_id}")
    filename = str(f"{datetime.now().isoformat().replace(':', '..')}__"
                   + basefilename + ".ogg")
    print(str(destination_dir) + filename)
    with open(str(destination_dir) + filename, "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    if pathlib.Path(str(destination_dir) + filename).exists():
        message = f"voice {filename} [raw] saved."
    output_wav = filename[:-3] + "wav"
    if ogg_to_wav(str(destination_dir) + filename, 
                  str(destination_dir) + output_wav):
        skm.komentar_suara = File(
            pathlib.Path(str(destination_dir) + output_wav).open(mode='rb'),
            name=basefilename + '.wav')
        skm.save()
        pathlib.Path(str(destination_dir) + output_wav).unlink(missing_ok=True)
        if skm.komentar_suara.name:
            message = "file upload successful"
        if stt:
            result, success = predict_voice_text(skm.komentar_suara.path)
            print(result, success)
            if success:
                skm.komentar += f" {STT_TOKEN}{result}{STT_TOKEN}"
                skm.save()
                message = f"STT {output_wav} done = {result}"
        else:
            message = f"STT {output_wav} failed!"
    else:
        message = f"convert to {output_wav} failed!"
    return message


def input_survey(id_registrasi, post, files):
    success, error = False, None
    if id_registrasi:
        try:
            registrasi = Registrasi.objects.get(id=id_registrasi)
            thesurvey = SurveiKepuasanMasyarakat(
                id_registrasi=registrasi,
                fasilitas_rate=post.get('fasilitas-rating', 0),
                perawat_rate=post.get('perawat-rating', 0),
                dokter_rate=post.get('dokter-rating', 0),
                farmasi_rate=post.get('farmasi-rating', 0),
                komentar=post.get('komentar', None),
            )
            thesurvey.save()
            print("saving survey without file")
            if thesurvey.id is not None:
                success = True
                print("survey saved without file")
                print(files.get('voice'))
                if files.get('voice'):
                    print(handle_voice_file(thesurvey, files.get('voice')))
        except Registrasi.DoesNotExist:
            error = "Id Registrasi tidak ditemukan"
        except Exception as e:
            error = e.__str__()
            print(error)
    else:
        error = "id_registrasi tidak terkirim"
    return success, error


def laporan_export_pdf(
        request: HttpRequest, dari: str = '', ke: str = ''):
    surveys = SurveiKepuasanMasyarakat.objects
    if dari != '' and ke != '':
        surveys = surveys.filter(created_at__gte=dari, created_at__lte=ke)
    else:
        surveys = surveys.all()
    pdfnya, filename = export_to_pdf_survey(request=request, queryset=surveys)
    response: HttpResponse = HttpResponse(
        pdfnya, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="' + filename + '"'
    return response