import json
import os
import sys
from pprint import pprint
from time import sleep

import whisper
import yt_dlp
from transformers import pipeline


def download_youtube_vide(url):
    ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'outtmpl': './audio/%(id)s.%(ext)s',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        audio_file = ydl.extract_info(url, download=False).get("id", None)
        ydl.download([url])
        

    return audio_file + '.mp3'




def get_summary(url):
    #def video_sum(url):
    audio_file = download_youtube_vide(url) #Download and convert your file to mp3


    audio_path = './audio/'+ audio_file
    model = whisper.load_model("base")
    result = model.transcribe(audio_path)
    os.remove(audio_path) #deleteing audio file as it might not be legal
    #print(result["text"])

    summarizer = pipeline("summarization", model="facebook/bart-large-cnn", tokenizer="facebook/bart-large-cnn", truncation=True)
    summary = summarizer(result["text"], max_length=1024, min_length=50, do_sample=False)
    return summary[0]['summary_text'], result["text"]
