import numpy as np
# funcion que recibe los datos de la señal capturada
# para calcular la serie de fourier
def calcular_serie_fourier(vectorX, vectorY):
    
    # Calcular los coeficientes de la serie de Fourier de la función
    N = len(vectorY)
    y_fft = np.fft.fft(vectorY)
    a = y_fft/N # amplitud de la serie de fourier
    f = np.fft.fftfreq(N, d=(vectorX[1] - vectorX[0]))  # Calcular las frecuencias correspondientes

    n = len(f)
    amplitud = a[:n//2]
    frecuencias = f[:n//2]
    
    # calcular el valor absoluto de la amplitud
    amplitud = 2*np.abs(amplitud)
    
    return amplitud, frecuencias