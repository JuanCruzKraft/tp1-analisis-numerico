import FFT
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
    amplitud, frecuencias = FFT.calcular_serie_fourier(vectorX, vectorY)
    #amplitud2, frecuencias2 = DFT.calcular_serie_fourier_sinFFT(vectorX, vectorY)
    
    #INCISO B
    #vectorYSuave = conv.calcular_convolcion(vectorY)
    # suavizar altas frecuencias con las transformadas
    #amp, freq = FFT.calcular_serie_fourier(vectorX, vectorYSuave)
    
    freqCorte = 2 #Hz
    fs = 1/(vectorX[1] - vectorX[0]) #Hz
    
    datosFiltrados = conv.butterworth_filter(vectorY, freqCorte, fs)
    
    amp, freq = FFT.calcular_serie_fourier(vectorX, datosFiltrados)
    
    
    # INCISO D

    
    # graficar los resultados obtenidos
    print()
    print("Amplitud maxima de señal original" + str(max(amplitud)))
    print("Amplitud maxima de señal filtrada" + str(max(amp)))
    
    
    gr.graficar(vectorX, vectorY)
    gr.graficar(frecuencias, amplitud)
    
    gr.graficar(vectorX, datosFiltrados)
    
    #gr.graficar(vectorX, vectorYSuave)
    gr.graficar(freq, amp)
    plt.show()
    
    
if __name__ == "__main__":
    main()
