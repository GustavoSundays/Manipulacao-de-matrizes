import numpy as np

def inversa(listaMatrizes):
    index = int(input(f'\nHá cadastradas {len(listaMatrizes)} matrizes, qual deseja ver a inversa? ')) - 1
    matriz = np.matrix(listaMatrizes[index])
    matrizInversa = matriz.getI()
    
    return [matriz, matrizInversa]