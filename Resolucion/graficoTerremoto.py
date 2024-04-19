import DFT
import graficar as gr
import convolucion as conv
import numpy as np
from matplotlib import pyplot as plt


# funcion que permite tomar los datos de un txt para luego
# procesar la señal del terremoto
def copiar_txt(txtFile):
    vectorX = []
    vectorY = []
    with open(txtFile, 'r') as txtfile:
        for line in txtfile:
            x, y = line.split() 
            vectorX.append(float(x))
            vectorY.append(float(y))

    return np.array(vectorX), np.array(vectorY)

# funcion principal
def main():
    # ingresar el nombre del archivo a analizar
    txt = input("Ingrese el nombre del archivo TXT que contiene la señal (sin extensión): ")
    txtFile = 'Resolucion/' + txt + '.txt'
    # guardar los valores x e y del archivo
    vectorX, vectorY = copiar_txt(txtFile)
    
    # INCISO A
    # utilizar calcular_serie_fourier() con los valores obtenidos de x e y del archivo para calcular
    # los coeficientes de la serie de fourier y calcular la TFD
    amplitud, frecuencias = DFT.calcular_serie_fourier(vectorX, vectorY)
    
    #INCISO B
    # tomar la transformada de fourier y convolucionarla con una ventana de gauss
    # para suavizar las señales mas altas (filtro pasabajos)
    # ampSuave = conv.calcular_convolcion(amplitud)
    
    # INCISO D

    
    # graficar los resultados obtenidos
    gr.graficar(vectorX, vectorY)
    gr.graficar(frecuencias, amplitud)
    plt.show()
    
if __name__ == "__main__":
    main()


# funcion que permite tomar los valores calculados de la señal
# y su procesamiento para graficarlos
""" def graficar(vectorX, vectorY, amplitud, frecuencias):
    
    # plotear la variacion de la amplitud en el tiempo
    plt.figure()
    plt.plot(vectorX, vectorY)
    plt.xlabel('Eje X')
    plt.ylabel('Eje Y')
    plt.title('Gráfico de los datos')
    plt.grid(True)
    
    
    # Plotear el espectro de frecuencia
    plt.figure()
    plt.plot(frecuencias, 2*np.abs(amplitud))
    plt.xlabel('Frecuencia [HZ]')
    plt.ylabel('Amplitud')
    plt.title('Espectro de frecuencia')
    plt.grid(True)
    
    plt.show() """