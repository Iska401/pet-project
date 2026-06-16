import av.error
from faster_whisper import WhisperModel


def transcription() -> str:

    model_size = "large-v2"
    text = ""
    model = WhisperModel(model_size, device="cpu", compute_type="int8")

    try:
        segments, info = model.transcribe("../downloads/rel.mp4", beam_size=5)
    except av.error.FileNotFoundError:
        return "File not found"

    else:
        for segment in segments:
            text += segment.text

        return text