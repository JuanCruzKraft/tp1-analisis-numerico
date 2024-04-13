import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import convolve
# Especifica la ruta de tu archivo de datos
ruta_archivo = "terremoto1.txt"  # Cambia "ruta/al/archivo.txt" a la ubicación real de tu archivo

# Lee los datos en un DataFrame de pandas
datos = pd.read_csv(ruta_archivo, sep='\t', header=None, names=['Tiempo', 'Valor'])

# Convierte la columna 'Tiempo' a tipo float (por si acaso)
datos['Tiempo'] = datos['Tiempo'].astype(float)

# Graficar
plt.plot(datos['Tiempo'], datos['Valor'])
plt.xlabel('Tiempo')
plt.ylabel('Valor')
plt.title('Gráfico de Tiempo-Valor')
plt.grid(True)
plt.show()