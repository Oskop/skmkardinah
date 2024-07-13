from survey.models import SurveiKepuasanMasyarakat, Registrasi
from survey.controllers.sherpa import predict_voice_text, ogg_to_wav
import pathlib
from datetime import datetime


def handle_voice_file(skm: SurveiKepuasanMasyarakat, f):
    message = ""
    parent_dir = 'media/'
    voice_directory = 'survey/voices/'
    destination_dir = parent_dir + voice_directory
    pathlib.Path(destination_dir).mkdir(parents=True, exist_ok=True)
    filename = str(f"{datetime.now().isoformat().replace(':', '..')}"
                   + f"__{skm.id}__{skm.id_registrasi_id}"
                   + f"__{skm.id_registrasi.norm_id}.ogg")
    print(str(destination_dir) + filename)
    with open(str(destination_dir) + filename, "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    if pathlib.Path(str(destination_dir) + filename).exists():
        message = f"voice {filename} [raw] saved."
    output_wav = filename[:-3] + "wav"
    if ogg_to_wav(str(destination_dir) + filename, 
                  str(destination_dir) + output_wav):
        result, success = predict_voice_text(
            str(destination_dir) + output_wav)
        print(result, success)
        if success:
            skm.komentar += f" ;;;[stt]{result}"
            skm.save()
            message = f"STT {output_wav} done = {result}"
        else:
            message = f"STT {output_wav} failed!"
    else:
        message = f"convert to {output_wav} failed!"
    print(message)
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
            if thesurvey.id is not None:
                success = True
                print(files.get('voice'))
                if files.get('voice'):
                    print(handle_voice_file(thesurvey, files.get('voice')))
        except Registrasi.DoesNotExist:
            error = "Id Registrasi tidak ditemukan"
        except Exception as e:
            error = e.__str__()
    else:
        error = "id_registrasi tidak terkirim"
    return success, error