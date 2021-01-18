# Singer2Singer
Inter-singer audio conversion using Deep Learning

## Why
> If Justin Bieber sang Adele's "Set Fire to the Rain", how would it sound?

Wouldn't it be interesting to know how songs would sound if sung by different singers and vocalists? I try to find an answer to this question through this project.

## Under the hood
I first create an audio dataset consisting of MP3s from the source singer and target singer. For instance, my source would be *Justin Bieber* and target *Adele*. 
<br>
<br>
I then convert these MP3 samples to MIDI; it's a format most ML projects work with. This allows me to work with raw numeric data that I can preprocess.

### Models used
Transformers have been picking up attention (pun unintended) in most practical areas outside the ML space. It has been used for Computer Vision and Audio Processing too. Riding on the hype train, I'll probably use `transformers` by Hugging Face to train on the MIDI sequences.

Ideally, this seems like a novel data generation task so it might require some heavy compute.
