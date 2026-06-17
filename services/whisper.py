import av.error
from faster_whisper import WhisperModel
from downloader import download_inst_content


def transcription(url: str) -> str:

    model_size = "large-v2"
    text = ""
    model = WhisperModel(model_size, device="cpu", compute_type="int8")

    if download_inst_content(url)["type"] == "video":
        try:
            segments, info = model.transcribe(download_inst_content(url)["path"], beam_size=5)
        except av.error.FileNotFoundError:
            return "File not found"

        else:
            for segment in segments:
                text += segment.text

            return text

