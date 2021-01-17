import os, youtube_dl

ydl_opts = {
    'outtmpl': './bin/%(title)s.%(ext)s',
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3'
    }]
}

adele = [
    "https://www.youtube.com/watch?v=LJzp_mDxaT0", # skyfall
    "https://www.youtube.com/watch?v=93dCIYaB4Os", # set fire to the rain
    "https://www.youtube.com/watch?v=YQHsXMglC9A", # hello
    "https://www.youtube.com/watch?v=BW9Fzwuf43c", # hometown glory
    "https://www.youtube.com/watch?v=a1IuJLebHgM", # when we were young
    "https://www.youtube.com/watch?v=iC_T4x-7uD0", # chasing pavements
]

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(adele)
    
path = "./bin/"    
ctr = 0

for file in os.listdir(path):
    filepath = path + file
    print (filepath)
    os.rename(filepath, path + "audio_{}.mp3".format(str(ctr)))
    ctr += 1