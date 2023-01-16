import sys
from pprint import pprint
from time import sleep

import whisper
from transformers import pipeline

from utils import download_youtube_vide, get_summary

url = "https://www.youtube.com/watch?v=Lpp9bHtPAN0" #Url of the video you want to summarize
#def video_sum(url):
audio_file = download_youtube_vide(url) #Download and convert your file to mp3



model = whisper.load_model("base")
result = model.transcribe(audio_file)
#print(result["text"])




summarizer = pipeline("summarization", model="facebook/bart-large-cnn", tokenizer="facebook/bart-large-cnn", truncation=True)
print(summarizer(result["text"], max_length=1024, min_length=50, do_sample=False))

""" if __name__ == '__main__':
    url = sys.argv[1]
    video_sum(url) """
#    "https://www.youtube.com/watch?v=Lpp9bHtPAN0"

    

test1, test2 = get_summary(url)