from faster_whisper import WhisperModel
from .downloader import download_inst_content


def transcription(url: str) -> str:

    model_size = "medium"
    text = ""
    model = WhisperModel(model_size, device="cpu", compute_type="int8")
    caption = download_inst_content(url)['caption']
    segments, info = model.transcribe(download_inst_content(url)["path"], beam_size=5)

    for segment in segments:
        text += segment.text

    return text + caption