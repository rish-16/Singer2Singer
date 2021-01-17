import librosa
import numpy as np
import glob
import matplotlib.pyplot as plt

data, sampling_rate = librosa.load("./bin/audio.mp3")
