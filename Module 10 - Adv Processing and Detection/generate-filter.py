from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

"""
Example Butterworth filter from: https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.butter.html
"""

# sample frequency (Hertz)
sample_frequency = 1000

# filter order
filter_order = 4

# cutoff frequency (Hertz)
f_c = 50

b, a = signal.butter(filter_order, f_c, btype='lowpass', fs=sample_frequency)

"""
Plot the butterworth filter response
https://dsp.stackexchange.com/questions/49009/get-the-frequency-response-curve-from-fir-filter-coefficients-sampling-rate
"""

# NOTE: FREQS is not the same as FREQZ
w, h = signal.freqz(b, a)

# because the results are normalized to sample frequency in radians, convert back
x = w * sample_frequency * 1.0 / (2 * np.pi)

# 20x multiplier because of dB conversion??
y = 20 * np.log10(abs(h))

plt.semilogx(x, y)
plt.ylabel('Amplitude [dB]')
plt.xlabel('Frequency [Hz]')
plt.title('Digital Filter Frequency Response with Butter')
plt.grid(which='both', linestyle='-', color='grey')
plt.show()

"""
Attempting similar filter with FIRWIN.
https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.firwin.html
"""

N = 6
f_s = sample_frequency
f_c = 50

b = signal.firwin(numtaps=N, cutoff=f_c, fs=f_s)

w, h = signal.freqz(b)

# because the results are normalized to sample frequency in radians, convert back
x = w * sample_frequency * 1.0 / (2 * np.pi)

# Response is linear and not in dB
y = h

plt.semilogx(x, y)
plt.ylabel('Amplitude [A]')
plt.xlabel('Frequency [Hz]')
plt.title('Digital Filter Frequency Response with FIRWIN')
plt.grid(which='both', linestyle='-', color='grey')
plt.show()
