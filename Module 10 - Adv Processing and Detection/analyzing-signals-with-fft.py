import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fft, ifft

"""
Source Signal
"""
# signal amplitude (Unitless)
source_amplitude = 1

# signal frequency (Hertz)
source_signal_frequency = 15

# from the frequency find the period (seconds)
source_signal_period = 1 / source_signal_frequency

"""
Corrupting Signal
"""

# signal amplitude (Unitless)
corrupt_amplitude = 0.5

# signal frequency (Hertz)
corrupt_signal_frequency = 60

# from the frequency find the period (seconds)
corrupt_signal_period = 1 / corrupt_signal_frequency

"""
Plot signal in time domain
"""

# sampling rate (Hertz)
sampling_rate = 1000

# sampling period (seconds)
sampling_period = 1 / sampling_rate

# make a simple plot of the signal sampled at the rate over 1 periods
# use np.line space to create a linearly spaced array
time = np.arange(start=0, stop=1, step=sampling_period)

# now calculate the signal from the resulting sample rate
# signal = Asin(2*pi*f*time+ phase)
source_signal = source_amplitude * np.sin(2 * np.pi * source_signal_frequency * time)
corrupt_signal = corrupt_amplitude * np.sin(2 * np.pi * corrupt_signal_frequency * time)
combined_signal = source_signal + corrupt_signal

# plot the resulting signal in matplotlib
plt.title('Base Signal with Corrupting Frequency')
plt.xlabel('Time (s)')
plt.ylabel('Signal')
plt.plot(time, source_signal, label=str('Source Signal ('+str(source_signal_frequency)+' Hz)'))
plt.plot(time, corrupt_signal, label=str('Corrupt Signal ('+str(corrupt_signal_frequency)+' Hz)'))
plt.plot(time, combined_signal, label='Combined Signal')
plt.legend()
plt.show()

"""
Plot signal in frequency domain: two-sided
Pulling from: https://pythonnumericalmethods.berkeley.edu/notebooks/chapter24.04-FFT-in-Python.html
"""

N = len(combined_signal)
X = fft(combined_signal)
sample_intervals = np.arange(N)
T = N / sampling_rate
freq = sample_intervals / T

plt.stem(freq, np.abs(X), 'b', markerfmt=" ", basefmt="-b")
plt.xlabel('Freq (Hz)')
plt.ylabel('FFT Amplitude |X(freq)|')
plt.title('Two-Sided FFT of Signal')
plt.show()

"""
Plot signal in frequency domain:
Using One-sided option from 
https://medium.com/0xcode/fast-fourier-transform-fft-algorithm-implementation-in-python-b592099bdb27
"""

N = len(combined_signal)//2
X = fft(combined_signal)[:N]
sample_intervals = np.arange(N)
T = N / sampling_rate
freq = sample_intervals / T / 2

plt.stem(freq, np.abs(X), 'b', markerfmt=" ", basefmt="-b")
plt.xlabel('Freq (Hz)')
plt.ylabel('FFT Amplitude |X(freq)|')
plt.title('One-Sided FFT of Signal')
plt.show()
