from pprint import pprint
from time import sleep

import requests
import youtube_dl

from config import api_key
from utils import download_youtube_vide, upload_audiofile_to_assemblyai

url = "https://www.youtube.com/watch?v=Lpp9bHtPAN0"

audio_file = download_youtube_vide(url)

audio_file = 'Lpp9bHtPAN0.mp3'
import whisper

model = whisper.load_model("base")
result = model.transcribe(audio_file)
print(result["text"])


from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn", tokenizer="facebook/bart-large-cnn", truncation=True)
print(summarizer(result["text"], max_length=1024, min_length=50, do_sample=False))


