from scipy import signal
import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fft


def plot_digital_filter_response(b, a, f_s):
    w, h = signal.freqz(b, a)

    # because the results are normalized to sample frequency in radians, convert back
    x = w * f_s * 1.0 / (2 * np.pi)

    # 20x multiplier because of dB conversion??
    y = 20 * np.log10(abs(h))

    plt.semilogx(x, y)
    plt.ylabel('Amplitude [dB]')
    plt.xlabel('Frequency [Hz]')
    plt.title('Frequency response')
    plt.grid(which='both', linestyle='-', color='grey')
    plt.show()


def plot_fft_response(signal, f_s):
    N = len(signal) // 2
    X = fft(signal)[:N]
    sample_intervals = np.arange(N)
    T = N / f_s
    freq = sample_intervals / T / 2

    plt.stem(freq, np.abs(X), 'b', markerfmt=" ", basefmt="-b")
    plt.xlabel('Freq (Hz)')
    plt.ylabel('FFT Amplitude |X(freq)|')
    plt.title('One-Sided FFT of Signal')
    plt.show()
