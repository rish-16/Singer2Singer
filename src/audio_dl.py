import os, youtube_dl

ydl_opts = {
    'outtmpl': './bin/adele/%(title)s.%(ext)s',
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
    
adele_path = "./bin/adele/"
ctr = 0

for file in os.listdir(adele_path):
    filepath = adele_path + file
    os.rename(filepath, adele_path + "audio_adele_{}.mp3".format(str(ctr)))
    ctr += 1    

ydl_opts = {
    'outtmpl': './bin/bieber/%(title)s.%(ext)s',
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3'
    }]
}    

bieber = [
    "https://www.youtube.com/watch?v=8ELbX5CMomE", # sorry
    "https://www.youtube.com/watch?v=h2jvHynuMjI", # stuck with u
    "https://www.youtube.com/watch?v=EaMed9sUPVo", # yummy
    "https://www.youtube.com/watch?v=ztHWxFVk9jE", # intentions
    "https://www.youtube.com/watch?v=Uim4GwSfzxY", # baby
    "https://www.youtube.com/watch?v=nPfg2Qymj8U", # love yourself
]

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(bieber)
    
bieber_path = "./bin/bieber/"
ctr = 0

for file in os.listdir(bieber_path):
    filepath = bieber_path + file
    os.rename(filepath, bieber_path + "audio_bieber_{}.mp3".format(str(ctr)))
    ctr += 1