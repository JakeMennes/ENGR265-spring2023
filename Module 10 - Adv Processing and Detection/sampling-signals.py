import numpy as np
import matplotlib.pyplot as plt
import math

# signal amplitude (Unitless)
A = 1

# signal frequency (Hertz)
signal_frequency = 10

# sampling rate (Hertz)
sampling_rate = 25

# make a simple plot of the signal sampled at the rate over 5 periods
# use np.line space to create a linearly spaced array
time = np.arange(start=0, stop=1, step=1 / sampling_rate)

# now calculate the signal from the resulting sample rate
# signal = Asin(2*pi*f*time+ phase)
signal = A * np.sin(2 * math.pi * signal_frequency * time)

# reconstruct the signal in higher sampling rate to see the effect
high_def_time = np.arange(start=0, stop=1, step=1 / (sampling_rate * 100))
high_def_signal = A * np.sin(2 * math.pi * signal_frequency * high_def_time)

# plot the resulting signal in matplotlib
plt.title('Sample of ' + str(signal_frequency) + 'Hz sine wave at ' + str(sampling_rate) + ' Hertz')
plt.xlabel('Time (s)')
plt.ylabel('Signal')
plt.scatter(time, signal, marker='x', label='Samples')
plt.plot(time, signal, marker='x', label='Reconstructed Signal')
plt.plot(high_def_time, high_def_signal, label='Original Signal')
plt.legend()
plt.show()
