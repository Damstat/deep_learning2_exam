import gradio as gr

from utils.pipeline import AudioSentimentPipeline

pipeline = AudioSentimentPipeline()


def analyze(audio):

    result = pipeline.predict(audio)

    return (
        result["transcription"],
        result["sentiment"],
        round(result["score"], 4)
    )


demo = gr.Interface(

    fn=analyze,

    inputs=gr.Audio(
        type="filepath",
        label="Audio"
    ),

    outputs=[
        gr.Textbox(label="Transcription"),
        gr.Textbox(label="Sentiment"),
        gr.Number(label="Score")
    ],

    title="Audio Sentiment Analysis",

    description="Transcription audio avec Wav2Vec2 puis analyse de sentiment avec BERT."
)


if __name__ == "__main__":
    demo.launch()