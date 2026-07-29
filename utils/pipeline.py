from utils.audio import preprocess_audio
from models.asr import SpeechToText
from models.sentiment import SentimentAnalyzer


class AudioSentimentPipeline:

    def __init__(self):

        # Chargé une seule fois
        self.asr = SpeechToText()

        self.sentiment = SentimentAnalyzer()

    def predict(self, audio_path):

        # 1. Prétraitement
        audio = preprocess_audio(audio_path)

        # 2. Audio -> Texte
        transcription = self.asr.predict(audio)

        # 3. Texte -> Sentiment
        sentiment = self.sentiment.predict(transcription)

        # 4. Résultat final
        return {
            "transcription": transcription,
            "sentiment": sentiment["label"],
            "score": sentiment["score"]
        }