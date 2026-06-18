import os
from openai import OpenAI
from pydantic import BaseModel
from utils.chooser import choose
from dotenv import load_dotenv
from typing import Optional


load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

class Event(BaseModel):
    link: Optional[str] = None
    event_name: Optional[str] = None
    country: Optional[str] = None
    city: Optional[str] = None
    date: Optional[str] = None
    is_online: Optional[bool] = None
    event_topic: Optional[str] = None
    is_free: Optional[bool] = None
    location: Optional[str] = None

def ai_response() -> str:
    try:
        response = client.responses.parse(
            model="gpt-5.4-mini",
            input=[
                {"role": "system", "content":
                    """
                    Extract event information from the provided text.
                    
                    If a field is missing, return null.
                    
                    Only extract:
                    - link
                    - event_name
                    - country
                    - city
                    - date
                    - is_online
                    - event_topic
                    - is_free
                    - location
                    """},
                {
                    "role": "user",
                    "content": choose("https://www.instagram.com/reel/DZehb7JIyDh/?igsh=ZmFzdTJoejU4OG1y"),
                },
            ],
            text_format=Event,
        )

    except Exception as e:
        return f"Error: {e}"
    else:
        event = response.output_parsed
        with open('downloads/response.json','w') as f:
            f.write(event.dumps(event))
        return 'downloads/response.json'