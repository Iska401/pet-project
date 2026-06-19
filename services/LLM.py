import os
import json
from openai import OpenAI
from pydantic import BaseModel
from utils.chooser import choose
from dotenv import load_dotenv
from typing import Optional


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

def ai_response(url: str) -> str:
    load_dotenv()

    api_key = os.getenv("OPENAI_API_KEY")

    client = OpenAI(api_key=api_key)

    try:
        response = client.responses.parse(
            model="gpt-5.4-mini",
            input=[
                {"role": "system", "content":
                    f"""
                    Extract event information from the provided text.
                    There is the link by the way: {url}
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
                    "content": choose(url),
                },
            ],
            text_format=Event,
        )

    except Exception as e:
        raise e
    else:
        event = response.output_parsed
        with open('./downloads/response.json','w') as f:
            json.dump([event.model_dump()],
                      f,
                      ensure_ascii=False,
                      indent=4)

        return './downloads/response.json'
