#impmortamos el paquete para word cloud

import matplotlib as plt
%matplotlib inline
from WordCloud import WordCloud
import numpy as np
import pandas as pd
from os import path
FICHERO = "texto.txt"

def plotea():
    plt.imshow(nube)
    plt.axis("off")
    plt.show()

def leefichero()
    #fichero = open(FICHERO, "r")
    #Codificado para leer español
    fichero = Path(FICHERO).read_text(encoding='utf-8')
    return fichero

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    fichero = leefichero()
    #Asumimos que el texto tiene solo las palabras, es posible que si es un csv haya que partirlo y contenarlo con espacios luego
    #Y que no hay caracteres raros
    nube = WorldCloud(collocations = False).generate(fichero)

    #Ploteamos con matplotflib y ya
    plotea()
    
