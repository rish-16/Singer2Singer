import librosa
import numpy as np
import glob
import matplotlib.pyplot as plt

data, sampling_rate = librosa.load("./bin/audio.mp3")

plt.figure(figsize=(12, 4))
librosa.display.waveplot(data, sr=sampling_rate)
# plt.show()