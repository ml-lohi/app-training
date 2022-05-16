import numpy as np
from scipy import ndimage

def gauss(x, sigma):
    return np.exp(-(x**2) / (2 * sigma**2)) / (np.sqrt(2 * np.pi) * sigma)


def filter_gauss(image, kernel_factor, sigma):
    faktor = kernel_factor * sigma * 2 + 1
    line = np.linspace(-kernel_factor * sigma, kernel_factor * sigma, faktor)
    filter = gauss(line, sigma=sigma)
    data_smoothed = ndimage.convolve(image, filter, mode="wrap")
    return data_smoothed


def fft(data, samples_per_second=1000):
    """
    Args:
        data: numpy array with the data
        samples_per_second: samples per second
    Returns:
        freqs, fft_wave.real: x and y to plot
    """
    fft_wave = np.fft.fft(data)
    freqs = np.fft.fftfreq(n=data.size, d=1 / samples_per_second)
    indices = freqs > 0
    return freqs[indices], np.abs(fft_wave.real[indices])

def avarage_phases(phases, n = 20):
    phases_averaged = np.array([])
    for p in phases: 
        phases_averaged = np.append(phases_averaged, np.mean(p.reshape(-1, n), axis=1)) 
    return phases_averaged.reshape(phases.shape[0], int(phases.shape[1]/n))