import sherpa_ncnn
import numpy as np
import wave
import soundfile as sf
import librosa
# from pydub import AudioSegment as am
from pathlib import Path
from google_spell_checker import GoogleSpellChecker

spell_checker = GoogleSpellChecker(lang="id")

config_dir = 'sherpa-ncnn-pruned-transducer-stateless7-streaming-id'

recognizer = sherpa_ncnn.Recognizer(
        tokens=f"{config_dir}/tokens.txt",
        encoder_param=f"{config_dir}/encoder_jit_trace-pnnx.ncnn.param",
        encoder_bin=f"{config_dir}/encoder_jit_trace-pnnx.ncnn.bin",
        decoder_param=f"{config_dir}/decoder_jit_trace-pnnx.ncnn.param",
        decoder_bin=f"{config_dir}/decoder_jit_trace-pnnx.ncnn.bin",
        joiner_param=f"{config_dir}/joiner_jit_trace-pnnx.ncnn.param",
        joiner_bin=f"{config_dir}/joiner_jit_trace-pnnx.ncnn.bin",
        num_threads=4,
    )


def ogg_to_wav(input_file_path, output_file_path, 
               frame_rate_output: int = 16000):
    print("ogg_to_wav start")
    # Old Method
    # data, samplerate = sf.read(input_file_path)
    # sf.write(output_file_path, data, samplerate)

    # with Librosa method
    raw_data, raw_sampling_rate = librosa.load(input_file_path)
    resampled_data = librosa.resample(
        raw_data, orig_sr=raw_sampling_rate, target_sr=frame_rate_output)
    sf.write(output_file_path, resampled_data, frame_rate_output, format='wav')


    # Pydub New Method
    # sound = am.from_ogg(input_file_path)
    # sound = sound.set_frame_rate(16000)
    # sound.export(filepath, format='wav')
    print('ogg_to_wav', Path(output_file_path).exists())
    print("ogg_to_wav end")
    return Path(output_file_path).exists()


def get_sample_rate(filename):
    # data, sample_rate = librosa.load(filename)

    # int16 = (data * 32767).astype(np.int16)
    samples_float32 = None
    with wave.open(filename) as f:
        assert f.getframerate() == recognizer.sample_rate, (
            f.getframerate(),
            recognizer.sample_rate,
        )
        assert f.getnchannels() == 1, f.getnchannels()
        assert f.getsampwidth() == 2, f.getsampwidth()  # it is in bytes
        num_samples = f.getnframes()
        samples = f.readframes(num_samples)
        samples_int16 = np.frombuffer(samples, dtype=np.int16)
        samples_float32 = samples_int16.astype(np.float32)
        samples_float32 = samples_float32 / 32768
    return samples_float32


def predict_voice_text(filename, correction: bool = True):
    samples_float32 = get_sample_rate(filename)
    if samples_float32 is not None:
        recognizer.accept_waveform(recognizer.sample_rate, samples_float32)

        tail_paddings = np.zeros(int(recognizer.sample_rate * 0.5), dtype=np.float32)
        recognizer.accept_waveform(recognizer.sample_rate, tail_paddings)

        recognizer.input_finished()
        print(recognizer.text)
        thetext = str(recognizer.text).replace('|', ' ')
        recognizer.reset()
        if correction:
            is_correct, corrected = spell_checker.check(thetext)
            if is_correct == False:
                thetext = corrected
        return thetext, True
    else:
        return "cannot get sampling rate", False