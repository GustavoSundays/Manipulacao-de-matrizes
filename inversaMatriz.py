import numpy as np

def inversa(listaMatrizes):
    index = int(input(f'\nHá cadastradas {len(listaMatrizes)} matrizes, qual deseja ver a inversa? ')) - 1
    matriz = np.matrix(listaMatrizes[index])
    if round(np.linalg.det(matriz)) == 0:
        return [matriz, "Não invertível"]
    matrizInversa = matriz.getI()
    
    return [matriz, matrizInversa]
