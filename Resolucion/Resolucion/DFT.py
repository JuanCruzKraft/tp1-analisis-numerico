import numpy as np

def calcular_serie_fourier_sinFFT(vectorX, vectorY):
    # Obtengo la long de la señal
    N = len(vectorY)
    
    # guardo en vectores los val de ampl y frec
    amplitud = np.zeros(N//2)
    frecuencias = np.zeros(N//2)
    
    # Itero sobre los primeros N/2 coef de frecuencia
    for k in range(N//2):
        suma = 0  # Arranco la suma en 0
        # Itero sobre todos los puntos de la señal
        for n in range(N):
            # Calculo la suma para el coef de frecuencia actual k
            suma += vectorY[n] * np.exp(-1j * 2 * np.pi * k * vectorX[n] / (vectorX[-1] - vectorX[0]))
        
        # Calculo la amplitud del coeficiente de frecuencia actual
        amplitud[k] = 2 * np.abs(suma) / N
        
        # Calculo la frec correspondiente al coeficiente de frecuencia actual
        frecuencias[k] = k / (vectorX[-1] - vectorX[0])
    
    return amplitud, frecuencias