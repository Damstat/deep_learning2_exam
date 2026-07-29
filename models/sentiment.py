import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification


class SentimentAnalyzer:

    def __init__(self):

        self.model_name = "ac0hik/Sentiment_Analysis_French"

        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)

        self.model = AutoModelForSequenceClassification.from_pretrained(
            self.model_name
        )

        self.model.eval()

    def predict(self, text):

        inputs = self.tokenizer(
            text,
            return_tensors="pt",
            truncation=True,
            padding=True,
            max_length=512
        )

        with torch.no_grad():
            outputs = self.model(**inputs)

        probs = torch.softmax(outputs.logits, dim=1)

        pred = torch.argmax(probs, dim=1).item()

        score = probs[0][pred].item()

        # Les noms des classes proviennent directement du modèle
        label = self.model.config.id2label[pred]

        return {
            "label": label,
            "score": score
        }