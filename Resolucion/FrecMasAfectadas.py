import numpy as np

def frecuencias_mas_afectadas(amplitud, frecuencias, n):
    # Ordeno las amplitudes de mayor a menor y saco los índices de cada una
    indices_ordenados = np.argsort(amplitud)[::-1]
    # obt las primeras n ampli y su frec correspondiente
    amplitudes_n = amplitud[indices_ordenados[:n]]
    frecuencias_n = frecuencias[indices_ordenados[:n]]

    return amplitudes_n, frecuencias_n
