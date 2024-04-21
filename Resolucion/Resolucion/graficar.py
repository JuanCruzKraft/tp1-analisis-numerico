import matplotlib.pyplot as plt

def graficar(vectorX, vectorY):
    
    
    plt.figure()
    plt.plot(vectorX, vectorY)
    plt.xlabel('Eje X')
    plt.ylabel('Eje Y')
    plt.title('Gráfico de los datos')
    plt.grid(True)