import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import convolve
# Especifica la ruta de tu archivo de datos
ruta_archivo = "terremoto1.txt"  # Cambia "ruta/al/archivo.txt" a la ubicación real de tu archivo

# Lee los datos en un DataFrame de pandas
datos = pd.read_csv(ruta_archivo, sep='\t', header=None, names=['Tiempo', 'Valor'])

#datos del txt terremoto1
tiempo = datos['Tiempo'].values
valor = datos['Valor'].values

# Elegir una ventana de convolución (por ejemplo, una ventana de Gauss)
variacion_suavizado= 100.0 # cuanto mas alto el valor, mas se suaviza
ventana = np.exp(-0.5 * (np.arange(-50, 51) / variacion_suavizado)**2)  # Ventana de Gauss de ancho 10

# Aplicar la convolución entre la señal original y la ventana
señal_suavizada = convolve(valor, ventana, mode='same') / ventana.sum()  # Normalizar la convolución

# Graficar la señal original y la señal suavizada
plt.figure(figsize=(12, 8))
plt.plot(tiempo, valor, label='Señal Original')
plt.plot(tiempo, señal_suavizada, label='Señal Suavizada')
plt.xlabel('Tiempo')
plt.ylabel('Valor')
plt.title('Comparación de Señal Original y Señal Suavizada')
plt.legend()
plt.grid(True)
plt.show()