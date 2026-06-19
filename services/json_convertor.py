import pandas as pd
import os
from .LLM import ai_response
from utils.delete_files import remove_file


def convert(url: str) -> None:
    file_exists = os.path.exists('./downloads/events.csv')
    json_path = ai_response(url)
    df = pd.read_json(json_path)
    df.to_csv(
        './downloads/events.csv',
          encoding='utf-8',
         index=False,
         mode='a',
         header=not file_exists)
    remove_file()
    print(json_path)
