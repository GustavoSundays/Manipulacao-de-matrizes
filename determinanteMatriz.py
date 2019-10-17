import numpy as np

def determinante(listaMatrizes):
    index = int(input(f'\nHá cadastradas {len(listaMatrizes)} matrizes, qual deseja ver a determinante? ')) - 1
    matriz = np.matrix(listaMatrizes[index])
    matrizDeterminante = round(np.linalg.det(matriz))
    
    return [matriz, matrizDeterminante]