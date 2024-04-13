import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Especifica la ruta de tu archivo de datos
ruta_archivo = "terremoto2.txt"  # Cambia "ruta/al/archivo.txt" a la ubicación real de tu archivo

# Lee los datos en un DataFrame de pandas
datos = pd.read_csv(ruta_archivo, sep='\t', header=None, names=['Tiempo', 'Valor'])

#datos del txt terremoto1
tiempo = datos['Tiempo'].values
valor = datos['Valor'].values

# Calcula la Transformada de Fourier Discreta (TFD) usando la FFT
dft = np.fft.fft(valor)

# Calcula las frecuencias correspondientes
N = len(tiempo)  # Número de muestras
T = tiempo[2] - tiempo[0]  # Período de muestreo
frecuencias = np.fft.fftfreq(N, T)  # Vector de frecuencias

# Grafica la parte real de la TFD
plt.figure(figsize=(12, 8))
plt.plot(frecuencias, dft.real, label='Parte Real', marker='o', linestyle='-')
plt.title('Transformada de Fourier Discreta (TFD)')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Amplitud')
plt.legend()
plt.grid(True)
plt.show()