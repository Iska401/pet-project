# Instagram Event Extractor

## Overview

Instagram Event Extractor is a Python application that automatically extracts event information from Instagram posts and reels.

The application:

1. Downloads Instagram content.
2. Extracts text from images using OCR.
3. Extracts speech from videos using Whisper.
4. Sends the extracted text to an LLM.
5. Converts the result into structured JSON.
6. Saves the data as a CSV file.

## Features

* Instagram image and reel processing
* OCR text extraction
* Speech-to-text transcription
* Structured event extraction using OpenAI
* CSV export

## Tech Stack

* Python
* Instaloader
* EasyOCR
* OpenAI API
* Pandas
* Pydantic

## Project Structure

```text
pet-project/
├── downloads/
├── services/
├── utils/
├── main.py
├── requirements.txt
├── .env
└── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/Iska401/pet-project.git
cd pet-project
```

Create a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
OPENAI_API_KEY=your_api_key
```

## Usage

Run the application:

```bash
python main.py
```

The extracted event data will be saved as:

```text
downloads/events.csv
```

## Author

Iskander Tadjimuratov
