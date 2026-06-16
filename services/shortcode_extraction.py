import re

def extract_shortcode(url: str) -> str:
    match = re.search(r'/(?:reel|p|tv)/([^/?]+)', url)

    if not match:
        raise ValueError("Invalid Instagram URL")

    return match.group(1)