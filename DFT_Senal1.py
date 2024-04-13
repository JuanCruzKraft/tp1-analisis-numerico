import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

ruta_archivo = "terremoto1.txt"

datos = pd.read_csv(ruta_archivo, sep='\t', header=None, names=['Tiempo', 'Valor'])

tiempo = datos['Tiempo'].values
valor = datos['Valor'].values

factor_reduccion_tiempo = 5  # Ajusta según sea necesario

# Submuestrear tiempo
tiempo_submuestreado = tiempo[::factor_reduccion_tiempo]
valor_submuestreado = valor

dft = np.fft.fft(valor_submuestreado)

N = len(valor_submuestreado)  # Número de muestras
T = (tiempo[1] - tiempo[0]) * factor_reduccion_tiempo  # Período de muestreo
frecuencias = np.fft.fftfreq(N, T)  # Vector de frecuencias

plt.figure(figsize=(12, 8))
plt.stem(frecuencias, dft.real)
plt.title('Transformada de Fourier Discreta (TFD)')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Amplitud')
plt.grid(True)
plt.show()
