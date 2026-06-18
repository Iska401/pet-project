import pandas as pd
from .LLM import ai_response
from utils.delete_files import remove_file


def convert() -> None:
    json_path = ai_response()
    df = pd.read_json(json_path)
    df.to_csv('./downloads/events.csv', encoding='utf-8', index=False)
    remove_file()
    print(json_path)
