import easyocr
from .downloader import download_inst_content


def reading_image(url: str) -> str:
    reader = easyocr.Reader(['en', 'ru'])
    result = reader.readtext(download_inst_content(url)['path'])
    caption = download_inst_content(url)["caption"]
    full_text = ''

    for (_, text) in result:
        full_text += text

    return full_text + caption