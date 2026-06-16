import instaloader
import requests
from shortcode_extraction import extract_shortcode


def download_reel(url: "str"):

    try:
        loader = instaloader.Instaloader()
        post = instaloader.Post.from_shortcode(loader.context, shortcode=extract_shortcode(url))
        video_url = post.video_url
        req = requests.get(video_url)

        with open("../downloads/reel.mp4", "wb") as file:
            file.write(req.content)

    except instaloader.BadResponseException:
        print("Bad connection or the reel doesnt exist.")

download_reel("https://www.instagram.com/reel/DYqFsjlRD1e/?igsh=cWFwc2Y5c3YxOHhj")