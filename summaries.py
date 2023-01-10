from pprint import pprint
from time import sleep

import requests
import youtube_dl

from config import api_key
from utils import download_youtube_vide, upload_audiofile_to_assemblyai

url = "https://www.youtube.com/watch?v=Lpp9bHtPAN0"

audio_file = download_youtube_vide(url)

audio_url = upload_audiofile_to_assemblyai(audio_file)

endpoint = "https://api.assemblyai.com/v2/transcript"


import whisper
