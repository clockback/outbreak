import numpy as np
import pygame

bits = 16

pygame.mixer.init(44100, -bits, 1)

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
    buf[s] = volume * int(round(max_sample * np.sin(
        2 * np.pi * frequency * t
        )))

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
    buf[s] = volume * int(round(max_sample * np.sin(
        2 * np.pi * frequency * t
        )))
    buf[s] += volume * int(round(max_sample * np.sin(
        2 * np.pi * 1.5 * frequency * t
        )))
    buf[s] += volume * int(round(max_sample * np.sin(
        2 * np.pi * 1.2 * frequency * t
        )))

layegg_wav = pygame.sndarray.make_sound(buf)

frequency = 200
duration = 0.3
volume = 0.15

n_samples = int(round(duration * sample_rate))

buf = np.zeros(n_samples, dtype=np.int16)

for s in range(n_samples):
    t = float(s) / sample_rate # time in seconds
    if t > 0.05:
        volume *= 0.9998
    buf[s] = volume * int(round(max_sample * np.sin(
        2 * np.pi * frequency * t
        )))

crack_wav = pygame.sndarray.make_sound(buf)

frequency = 440
duration = 0.3
volume = 0.15

n_samples = int(round(duration * sample_rate))

buf = np.zeros(n_samples, dtype=np.int16)

for s in range(n_samples):
    t = float(s) / sample_rate # time in seconds
    if t > 0.05:
        volume *= 0.9998
    buf[s] = volume * int(round(max_sample * np.sin(
        2 * np.pi * frequency * t
        )))

hatch_wav = pygame.sndarray.make_sound(buf)

frequency = 440
duration = 2.5
volume = 0.2

n_samples = int(round(duration * sample_rate))

buf = np.zeros(n_samples, dtype=np.int16)

for s in range(n_samples):
    t = float(s) / sample_rate # time in seconds
    if t < 0.5:
        frequency = 329.63 / 2
        if t < 0.1:
            volume = 2 * (t)
        elif t > 0.3:
            volume = 0.5 - t
    elif t < 1.0:
        volume = 0.2
        frequency = 311.13 / 2
        if t < 0.6:
            volume = 2 * (t - 0.5)
        elif t > 0.8:
            volume = 1.0 - t
    elif t < 1.5:
        volume = 0.2
        frequency = 293.66 / 2
        if t < 1.1:
            volume = 2 * (t - 1.0)
        elif t > 1.3:
            volume = 1.5 - t
    else:
        volume = 0.2
        if t < 1.6:
            volume = 2 * (t - 1.5)
        elif t > 2.3:            
            volume = 2.5 - t
        frequency = 277.18 / 2
    buf[s] = volume * int(round(max_sample * np.sin(
        2 * np.pi * frequency * t
        )))

lose_wav = pygame.sndarray.make_sound(buf)
