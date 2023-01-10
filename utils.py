import youtube_dl


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
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        audio_file = ydl.extract_info(url, download=False).get("id", None)
        ydl.download([url])
        

    return audio_file + '.mp3'
    
def upload_audiofile_to_assemblyai(file):
    import requests
    from config import api_key
    filename = "audio_book.mp3"
    def read_file(filename, chunk_size=5242880):
        with open(filename, 'rb') as _file:
            while True:
                data = _file.read(chunk_size)
                if not data:
                    break
                yield data

    headers = {'authorization': api_key}
    response = requests.post('https://api.assemblyai.com/v2/upload',
                            headers=headers,
                            data=read_file(filename))

    return response.json().get('upload_url')