# IA ASSISTANT

A command-line assistant that uses the OpenAI API to perform four tasks: text translation, image downloading, problem-solving from images, and audio transcription.

## Features

- **Text translation** — translates any text into the language you specify
- **Download image from URL** — downloads and saves an image locally
- **Solve problem from image** — analyzes a PNG and solves the problem it contains (vision)
- **Audio transcription** — converts an audio file to text using Whisper

## Requirements

- Python 3.8+
- An [OpenAI](https://platform.openai.com) account with an API key

## Installation

```bash
git clone https://github.com/1lauraog15-cloud/asistente-ia.git
cd asistente-ia
pip install openai python-dotenv requests
```

Create a `.env` file in the project root:

```
OPENAI_API_KEY=your_api_key_here
```

## Usage

```bash
python asistente.py
```

An interactive menu will open where you can choose the feature you want to use.
