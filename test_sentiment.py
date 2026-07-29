from models.sentiment import SentimentAnalyzer

model = SentimentAnalyzer()

phrases = [
    "Je suis très heureux aujourd'hui.",
    "Ce service est catastrophique.",
    "Le produit est correct."
]

for phrase in phrases:

    result = model.predict(phrase)

    print("-" * 50)
    print("Texte :", phrase)
    print("Sentiment :", result["label"])
    print("Score :", result["score"], 4)