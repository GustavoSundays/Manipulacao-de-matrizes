import numpy as np

def transposta(listaMatrizes):
    index = int(input(f'\nHá cadastradas {len(listaMatrizes)} matrizes, qual deseja ver a transposta? ')) - 1
    matriz = np.matrix(listaMatrizes[index])
    matrizTransposta = matriz.getT()
    
    return [matriz, matrizTransposta]