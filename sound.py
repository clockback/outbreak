import math
import numpy as np
import pygame
from pygame import sndarray

bits = 16

pygame.mixer.pre_init(44100, -bits, 1)
pygame.init()
duration = 0.2
frequency = 330
sample_rate = 44100
volume = 0.15

n_samples = int(round(duration * sample_rate))

buf = np.zeros(n_samples, dtype=np.int16)
max_sample = 2 ** (bits - 1) - 1

for s in range(n_samples):
    t = float(s) / sample_rate # time in seconds
    frequency *= 1.0003
    buf[s] = volume * int(round(max_sample * np.sin(2 * np.pi * frequency * t)))

shockwave_wav = pygame.sndarray.make_sound(buf)

frequency = 330
duration = 0.5
n_samples = int(round(duration * sample_rate))

buf = np.zeros(n_samples, dtype=np.int16)

for s in range(n_samples):
    t = float(s) / sample_rate # time in seconds
    frequency *= 1.00001
    if t > 0.25:
        volume /= (1.0002) ** 2
    buf[s] = volume * int(round(max_sample * np.sin(2 * np.pi * frequency * t)))
    buf[s] += volume * int(round(max_sample * np.sin(2 * np.pi * 1.5 * frequency * t)))
    buf[s] += volume * int(round(max_sample * np.sin(2 * np.pi * 1.2 * frequency * t)))

layegg_wav = pygame.sndarray.make_sound(buf)
