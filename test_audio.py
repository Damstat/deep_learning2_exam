from utils.audio import preprocess_audio

audio = preprocess_audio("test_audio/audio1.wav")

print(audio.shape)

print(audio)