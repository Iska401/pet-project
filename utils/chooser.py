from services.downloader import download_inst_content
from services.OCR import reading_image
from services.whisper import transcription

def choose(url: str):
    type = download_inst_content(url)['type']

    if type  == 'video':
        return transcription(url)
    elif type == 'image':
        return reading_image(url)
    else:
        return None
