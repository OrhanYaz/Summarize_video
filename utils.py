import json

import yt_dlp


def download_youtube_vide(url):
    ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'outtmpl': '%(id)s.%(ext)s',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        audio_file = ydl.extract_info(url, download=False).get("id", None)
        ydl.download([url])
        

    return audio_file + '.mp3'