import instaloader
import requests
from .shortcode_extraction import extract_shortcode


def download_inst_content(url: str) -> str | dict[str, str]:

    try:
        loader = instaloader.Instaloader()
        post = instaloader.Post.from_shortcode(loader.context, shortcode=extract_shortcode(url))
        caption = post.caption
        if post.typename == "GraphVideo":
            video_url = post.video_url
        elif post.typename == "GraphImage":
            image_url = post.url

    except instaloader.BadResponseException:
        return "Bad connection or the reel doesnt exist."

    else:
        if post.is_video:
            with open("./downloads/reel.mp4", "wb") as file:
                req = requests.get(video_url)
                file.write(req.content)
            return {
                "type": "video",
                "path": "./downloads/reel.mp4",
                "caption": caption
            }

        else:
            with open("./downloads/content.jpg", "wb") as file:
                req = requests.get(image_url)
                file.write(req.content)
            return {
                "type": "image",
                "path": "./downloads/content.jpg",
                "caption": caption
            }
# download_inst_content("https://www.instagram.com/p/DZnV9dvvBU7/?igsh=NTM0bDgzOTlwZmth")