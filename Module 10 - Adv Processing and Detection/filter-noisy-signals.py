import numpy as np
import matplotlib.pyplot as plt
import math
from scipy import signal
from filter_utilities import plot_digital_filter_response, plot_fft_response

"""
Source Signal
"""
# signal amplitude (Unitless)
source_amplitude = 1

# signal frequency (Hertz)
source_signal_frequency = 25

# from the frequency find the period (seconds)
source_signal_period = 1 / source_signal_frequency

"""
Corrupting Signal
"""

# signal amplitude (Unitless)
corrupt_amplitude = 1.1

# signal frequency (Hertz)
corrupt_signal_frequency = 200

# from the frequency find the period (seconds)
corrupt_signal_period = 1 / corrupt_signal_frequency

"""
Global Parameters
"""

# sampling rate (Hertz)
sample_frequency = 10 * max(source_signal_frequency, corrupt_signal_frequency)

# make a simple plot of the signal sampled at the rate over one period
time = np.arange(0, 1, 1 / sample_frequency)

# now calculate the signal from the resulting sample rate
# signal = Asin(2*pi*f*time+ phase)
source = source_amplitude * np.sin(2 * math.pi * source_signal_frequency * time)
noise = corrupt_amplitude * np.sin(2 * math.pi * corrupt_signal_frequency * time)
real_signal = source + noise

# plot the resulting signal in matplotlib
plt.title('Base Signal with Corrupting Frequency')
plt.xlabel('Time (s)')
plt.ylabel('Signal')
plt.plot(time, source, label='Source Signal')
plt.plot(time, noise, label='Noise Signal')
plt.plot(time, real_signal, label='Combined Signal')
plt.legend()
plt.show()

"""
Plot signal in frequency domain
Pulling from: https://pythonnumericalmethods.berkeley.edu/notebooks/chapter24.04-FFT-in-Python.html
"""

plot_fft_response(real_signal, sample_frequency)

"""
After identifying the noise location, develop a filter type to remove it
In current example source is 25Hz, noise is 200Hz. A 50Hz low pass filter should do the trick
"""

# filter order
filter_order = 6

# cutoff frequency (Hertz)
f_c = 50

# generate magic coefficients for butterworth filter
b, a = signal.butter(filter_order, f_c, btype='lowpass', fs=sample_frequency)

plot_digital_filter_response(b, a, sample_frequency)

"""
Now apply filter to corrupted signal and plot the results
"""

filtered = signal.filtfilt(b, a, real_signal)

plt.plot(time, source, label='Original Signal')
plt.plot(time, real_signal, label='Corrupted Signal')
plt.plot(time[:len(filtered)], filtered, label='Filtered Result')
plt.title('Impact of Filtering with Butter and FiltFilt Function')
plt.legend()
plt.show()

"""
Show the resulting figure to see if it worked
"""
plot_fft_response(filtered, sample_frequency)

"""
Attempt a second approach with FIRWIN and convolve
@TODO: still a work in progress
"""
N = 20
f_s = sample_frequency
f_c = 50

b = signal.firwin(numtaps=N, cutoff=f_c, fs=f_s)

w, h = signal.freqz(b)

# because the results are normalized to sample frequency in radians, convert back
x = w * f_s * 1.0 / (2 * np.pi)

# Response is linear and not in dB
y = h

# plot filter response
plt.semilogx(x, y)
plt.ylabel('Amplitude [A]')
plt.xlabel('Frequency [Hz]')
plt.title('Digital Filter Frequency Response with FIRWIN')
plt.grid(which='both', linestyle='-', color='grey')
plt.show()


# filter signal with convolve
filtered = np.convolve(real_signal, b)

# replot the original and filtered signals
plt.plot(time, source, label='Original Signal')
plt.plot(time, real_signal, label='Corrupted Signal')
plt.plot(time, filtered[:len(time)], label='Filtered Result')
plt.title('Impact of Filtering with Butter and Convolve Function')
plt.legend()
plt.show()
