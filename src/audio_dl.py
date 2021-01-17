import youtube_dl

ydl_opts = {
    'outtmpl': './bin/audio.%(ext)s',
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3'
    }]
}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.youtube.com/watch?v=caySD0OJJvk'])