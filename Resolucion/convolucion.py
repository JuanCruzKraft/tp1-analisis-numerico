import numpy as np
from scipy.signal import convolve, butter, filtfilt


def calcular_convolcion(vectorY):
    
    ventana = ventana_gauss()
    señal_suavizada = convolve(vectorY, ventana, mode='same') / ventana.sum()  # Normalizar la convolución
    
    return señal_suavizada

def convolucion(vectorEntrada, vectorH):
    return convolve(vectorEntrada, vectorH, mode='same') / vectorH.sum()  # Normalizar la convolución

def ventana_gauss():
    # Elegir una ventana de convolución (por ejemplo, una ventana de Gauss)
    variacion_suavizado = 2 # cuanto mas alto el valor, mas se suaviza
    ventana = np.exp(-0.5 * (np.arange(-30, 31) / variacion_suavizado)**2)  # Ventana de Gauss de ancho 10
    return ventana

def ventana_gauss_alernative():
    N = 4000
    n = np.arange(-(N-1)/2,(N-1)/2)
    a = 8
    desviacionSTD = (N-1)/(2*a)
    y = np.exp(-0.5 * (n/desviacionSTD)**2)
    return y
# ------------------------------------------------

def butterworth_filter(data, cutoff_freq, sampling_freq, filter_order=4, filter_type='low'):
    # Normalizar la frecuencia de corte con respecto a la frecuencia de Nyquist
    nyquist_freq = 0.5 * sampling_freq
    cutoff_freq_normalized = cutoff_freq / nyquist_freq

    # Calcular los coeficientes del filtro
    b, a = butter(filter_order, cutoff_freq_normalized, btype=filter_type, analog=False)

    # Aplicar el filtro a los datos utilizando filtfilt para evitar el desplazamiento de fase
    filtered_data = filtfilt(b, a, data)

    return filtered_data




def suavizar_con_hamming(vectorY):
    # Definir la ventana de Hamming
    ventana_hamming = np.hamming(len(vectorY))
    # Realizar la convolución entre la señal y la ventana de Hamming
    signal_suavizada = np.convolve(vectorY, ventana_hamming, mode='same') / sum(ventana_hamming)
    return signal_suavizada

'''def butter_lowpass(cutoff_freq, sample_freq, order=5):
    nyquist_freq = 0.5 * sample_freq
    normal_cutoff = cutoff_freq / nyquist_freq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

def apply_filter(data, cutoff_freq, sample_freq, order=5):
    b, a = butter_lowpass(cutoff_freq, sample_freq, order=order)
    y = lfilter(b, a, data)
    return y'''