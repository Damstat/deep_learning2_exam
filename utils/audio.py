import torchaudio
import torch


def preprocess_audio(audio_path):
    """
    Charge un fichier audio,
    le convertit en mono,
    puis le rééchantillonne à 16 kHz.
    """

    # Chargement de l'audio
    waveform, sample_rate = torchaudio.load(audio_path)

    # Conversion en mono si nécessaire
    if waveform.shape[0] > 1:
        waveform = torch.mean(waveform, dim=0, keepdim=True)

    # Rééchantillonnage à 16 kHz
    if sample_rate != 16000:
        resampler = torchaudio.transforms.Resample(
            orig_freq=sample_rate,
            new_freq=16000
        )
        waveform = resampler(waveform)

    return waveform