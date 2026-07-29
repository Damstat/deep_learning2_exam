from utils.pipeline import AudioSentimentPipeline

# Création du pipeline
pipeline = AudioSentimentPipeline()

# Audio de test
audio_path = "test_audio/audio1.wav"

# Prédiction
result = pipeline.predict(audio_path)

print("-" * 50)
print("Transcription :", result["transcription"])
print("Sentiment :", result["sentiment"])
print("Score :", result["score"])