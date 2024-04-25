import numpy as np

def suavizar_con_convolucion(senial):
    #  elijo la long que va a tener la ventana
    ventana_longitud=8
    # Creo una ventana rectangular para el filtro pasa bajos
    ventana = np.ones(ventana_longitud) / ventana_longitud
    
    # Aca aplico la convolucion con el filtro pasa bajos
    senial_suavizada = np.convolve(senial, ventana, mode='same')

    return senial_suavizada