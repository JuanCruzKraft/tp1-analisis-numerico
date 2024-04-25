
import FFT
import Pasabajo
import FrecMasAfectadas
import graficar as gr
import convolucion as conv
import numpy as np
from matplotlib import pyplot as plt


# funcion que permite tomar los datos de un txt para luego
# procesar la señal del terremoto
def copiar_txt(txtFile):
    i = 1
    terr2 = False
    if(txtFile == 'terremoto2.txt'):
        terr2 = True
    vectorX = []
    vectorY = []
    with open(txtFile, 'r') as txtfile:
        for line in txtfile:
            if(i%2 != 0):
                x, y = line.split() 
                vectorX.append(float(x))
                vectorY.append(float(y))
            i = i+1 if terr2==True else i


    return np.array(vectorX), np.array(vectorY)

# funcion principal
def main():
    # ingresar el nombre del archivo a analizar
    txt = input("Ingrese el nombre del archivo TXT que contiene la señal (sin extensión): ")
    txtFile = txt + '.txt'
    # guardar los valores x e y del archivo
    vectorX, vectorY = copiar_txt(txtFile)
    print(len(vectorY))
    # ------------------------
    # INCISO A
    # utilizar calcular_serie_fourier() con los valores obtenidos de x e y del archivo para calcular
    # los coeficientes de la serie de fourier y calcular la TFD
    amplitud, frecuencias = FFT.calcular_serie_fourier(vectorX, vectorY)
    #amplitud2, frecuencias2 = DFT.calcular_serie_fourier_sinFFT(vectorX, vectorY)

    # mostrar resultados del inciso a
    gr.graficar(vectorX, vectorY, "Señal en el espectro del tiempo")
    gr.graficar(frecuencias, amplitud, "Señal en el espectro de frecuencias")
    plt.show()

    #INCISO B
    # calcular la convolucion para suavizar la señal
    vectorYSuave = Pasabajo.suavizar_con_convolucion(vectorY)
    amplitudSuave, frecuenciasSuave = FFT.calcular_serie_fourier(vectorX, vectorYSuave)

    # graficar y comparar el resultado con la original
    gr.graficar(frecuencias, amplitud, "Señal en el espectro de frecuencias sin suavizar")
    gr.graficar(frecuenciasSuave, amplitudSuave, "Señal en el espectro de frecuencias suavizada")
    plt.show()

    # ------------------------
    # INCISO C
    top_n = 10  #pongo el top de frec mas altas
    # busqueda de frecuencias mas amplias o afectadas
    amplitudes_top, frecuencias_top = FrecMasAfectadas.frecuencias_mas_afectadas(amplitud,frecuencias,top_n)

    #graf de inciso C
    print("Las", top_n, "frecuencias más afectadas son:")
    for i in range(top_n):
        print("Frecuencia:", frecuencias_top[i], "Hz - Amplitud:", amplitudes_top[i])


    #graf de inciso C
    print("Las", top_n, "frecuencias más afectadas son:")
    for i in range(top_n):
        print("Frecuencia:", frecuencias_top[i], "Hz - Amplitud:", amplitudes_top[i])
    
    
    # INCISO E
    vectorX3, vectorY3 = copiar_txt("terremoto3.txt")
    amplitud3, frecuencias3 = FFT.calcular_serie_fourier(vectorX3, vectorY3)

    gr.graficar(frecuencias, amplitud, "Señal ingresada")
    gr.graficar(frecuencias3, amplitud3, "Señal Terremoto3")




    # graficar los resultados obtenidos
    print()
    #print("Amplitud maxima de señal original" + str(max(amplitud)))
    #print("Amplitud maxima de señal filtrada" + str(max(amp)))
    
    
    #gr.graficar(vectorX, vectorY)
    gr.graficar(frecuencias, amplitud, 'Espectro de Frecuencias sin Filtro')
    
    #gr.graficar(vectorX, vectorYSuave)
    #gr.graficar(freq, amp, 'Espectro de Frecuencias con Filtro')
    plt.show()
    
    
if __name__ == "__main__":
    main()
