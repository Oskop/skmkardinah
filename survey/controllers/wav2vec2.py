import soundfile as sf
import librosa
import torch
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor
import os
import re


def convert(inputfile, outfile):
    target_sr = 16000
    data, sample_rate = librosa.load(inputfile)
    data = librosa.resample(data, orig_sr=sample_rate, target_sr=target_sr)
    sf.write(outfile, data, target_sr)


def normalize_text(text: str) -> str:
    """DO ADAPT FOR YOUR USE CASE. this function normalizes the target text."""

    chars_to_ignore_regex = '[,?.!-;:""%\'"�\'‘’_，！łńō–—\\\\\\“”\\[\\]]'

    text = re.sub(chars_to_ignore_regex, "", text.lower())
    text = re.sub(r'[‘’´`]', r"'", text)
    text = re.sub(r'è', r"é", text)
    text = re.sub(r"(-|' | '|  +)", " ", text)

    # In addition, we can normalize the target text, e.g. removing new lines characters etc...
    # note that order is important here!
    token_sequences_to_ignore = ["\n\n", "\n", "   ", "  "]

    for t in token_sequences_to_ignore:
        text = " ".join(text.split(t))

    return text


def parse_transcription(wav_file):
    filename = wav_file.name.split('.')[0]
    convert(wav_file.name, filename + "16k.wav")
    speech, _ = sf.read(filename + "16k.wav")
    input_values = processor(speech, sampling_rate=16_000,
                             return_tensors="pt").input_values
    input_values = input_values.to(device)
    logits = model(input_values).logits
    predicted_ids = torch.argmax(logits, dim=-1)
    transcription = processor.decode(
        predicted_ids[0], skip_special_tokens=True)
    return transcription
