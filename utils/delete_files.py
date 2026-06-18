from pathlib import Path

def remove_file():
    reel_path = Path('./downloads/reel.jpg')
    image_path = Path('./downloads/content.jpg')
    json_path = Path('./downloads/response.json')
    reel_path.unlink(missing_ok=True)
    image_path.unlink(missing_ok=True)
    json_path.unlink(missing_ok=True)