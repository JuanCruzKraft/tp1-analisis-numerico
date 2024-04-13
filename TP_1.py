
# importar librerias para resolver el problema
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# guardar ruta del archivo que contiene las muestras del terremoto
ruta_archivo ="terremoto1.txt" 

# leer y guardar los datos en un variable 'datos' que contiene el tiempo n y la amplitud en ese tiempo f[n]
datos = pd.read_csv(ruta_archivo, sep='\t', header=None, names=['Tiempo', 'Amplitud'])
datos['Tiempo'] = datos['Tiempo'].astype(float)

# graficar las muestras obtenidas del terremoto utilizando matplotlib
plt.plot(datos['Tiempo'], datos['Amplitud'])
plt.xlabel('Tiempo')
plt.ylabel('Amplitud')
plt.title('Gráfico de Tiempo-Amplitud')
plt.grid(True)
plt.show()

# guardar los datos n y f[n] para procesarlos
tiempo= datos['Tiempo'].values
amplitud= datos['Amplitud'].values

# calcular los coeficientes de la serie de fourier discreta utilizando el algoritmo fft
dft = np.fft.fft(amplitud)


N = len(tiempo)  
T = tiempo[1] - tiempo[0] 

# calcular el vector de frecuencias con fftfreq para hacer cambio de dominio
frecuencias = np.fft.fftfreq(N, T)  

# graficar transformada de fourier con los valores absolutos de 'dft'
plt.figure(figsize=(10, 6))
plt.plot(frecuencias, np.abs(dft))
plt.title('Transformada de Fourier Discreta (TFD)')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Amplitud')
plt.grid(True)
plt.show() 
