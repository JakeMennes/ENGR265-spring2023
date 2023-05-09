import numpy as np
import matplotlib.pyplot as plt
import math

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
corrupt_amplitude = 1.1

# signal frequency (Hertz)
corrupt_signal_frequency = 60

# from the frequency find the period (seconds)
corrupt_signal_period = 1 / corrupt_signal_frequency

"""
Global Parameters
"""

# sampling rate (Hertz)
sampling_rate = 1000

# make a simple plot of the signal sampled at the rate
time = np.arange(start=0, stop=20 / min(corrupt_signal_frequency, source_signal_frequency), step=1 / sampling_rate)

# now calculate the signal from the resulting sample rate
# signal = Asin(2*pi*f*time+ phase)
source_signal = source_amplitude * np.sin(2 * math.pi * source_signal_frequency * time)
corrupt_signal = corrupt_amplitude * np.sin(2 * math.pi * corrupt_signal_frequency * time)

# plot the resulting signal in matplotlib
plt.title('Base Signal with Corrupting Frequency')
plt.xlabel('Time (s)')
plt.ylabel('Signal')
plt.plot(time, source_signal, label='Source Signal')
plt.plot(time, corrupt_signal, label='Noise Signal')
plt.plot(time, corrupt_signal + source_signal, label='Combined Signal')
plt.legend()
plt.show()
