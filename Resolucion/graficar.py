import matplotlib.pyplot as plt

def graficar(vectorX, vectorY, label='grafico'):
    
    
    plt.figure()
    plt.plot(vectorX, vectorY)
    plt.xlabel('Eje X')
    plt.ylabel('Eje Y')
    plt.title(label)
    plt.grid(True)