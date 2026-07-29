from transformers import Wav2Vec2Processor, AutoModelForCTC
import torch


class SpeechToText:

    def __init__(self):

        model_name = "jonatasgrosman/wav2vec2-large-xlsr-53-french"

        self.processor = Wav2Vec2Processor.from_pretrained(
            model_name
        )

        self.model = AutoModelForCTC.from_pretrained(
            model_name
        )


    def transcribe(self, waveform):

        inputs = self.processor(
            waveform.squeeze().numpy(),
            sampling_rate=16000,
            return_tensors="pt"
        )

        with torch.no_grad():
            logits = self.model(**inputs).logits


        predicted_ids = torch.argmax(logits, dim=-1)


        transcription = self.processor.batch_decode(
            predicted_ids
        )[0]


        return transcription.lower()