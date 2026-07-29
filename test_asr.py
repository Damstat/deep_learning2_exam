from utils.audio import preprocess_audio
from models.asr import SpeechToText

audio = preprocess_audio("test_audio/audio2.wav")

asr = SpeechToText()

text = asr.transcribe(audio)

print(text)