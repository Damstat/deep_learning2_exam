from fastapi import FastAPI, UploadFile, File
import shutil
import os

from utils.pipeline import AudioSentimentPipeline

app = FastAPI(
    title="Audio Sentiment API"
)

pipeline = AudioSentimentPipeline()


@app.post("/predict")
async def predict(file: UploadFile = File(...)):

    os.makedirs("uploads", exist_ok=True)

    audio_path = f"uploads/{file.filename}"

    with open(audio_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    result = pipeline.predict(audio_path)

    return result