import numpy as np

def soma(listaMatrizes):
    qtdMatrizSoma = int(input(f'Há cadastradas {len(listaMatrizes)} matrizes, quantas deseja usar na soma? '))
    matrizesParaSoma = []
    soma = np.matrix(0)

    for i in range(qtdMatrizSoma):
        index = int(input(f'Qual seria a {i+1} matriz para soma? ')) - 1
        matrizesParaSoma.append(index)
        if len(matrizesParaSoma) > 1:
            isTamanhosIguais = validaMatrizes(listaMatrizes, matrizesParaSoma[0], index)
            if isTamanhosIguais == False:
                matrizesParaSoma.remove(index)
            while isTamanhosIguais == False:
                desejaSelecionarOutra = input(f'Matriz {index + 1} tem tamanhos diferentes das outras matrizes, deseja selecionar outra? [S/N]').upper()
                if desejaSelecionarOutra == 'S':
                    index = int(input(f'Qual seria a {i+1} matriz para soma?')) - 1
                    isTamanhosIguais = validaMatrizes(listaMatrizes, matrizesParaSoma[0], index)
                    if isTamanhosIguais == True:
                        matrizesParaSoma.append(index)
                else:
                    isTamanhosIguais = True
                    if len(matrizesParaSoma) >= 2:
                        for i in range(len(matrizesParaSoma)):
                            if i == 0:
                                soma = np.matrix(listaMatrizes[matrizesParaSoma[i]]) + np.matrix(listaMatrizes[matrizesParaSoma[i+1]])
                                continue
                            elif i + 2 <= len(matrizesParaSoma):
                                soma += np.matrix(listaMatrizes[matrizesParaSoma[i+1]])
                        return soma
                    else:
                        soma = np.matrix(listaMatrizes[matrizesParaSoma[0]])
                        return soma
        
    for i in range(len(matrizesParaSoma)):
        if len(matrizesParaSoma) == 1:
            soma = np.matrix(listaMatrizes[matrizesParaSoma[i]])
        elif i == 0:
            soma = np.matrix(listaMatrizes[matrizesParaSoma[i]]) + np.matrix(listaMatrizes[matrizesParaSoma[i+1]])
            continue
        elif i + 2 <= len(matrizesParaSoma):
            soma += np.matrix(listaMatrizes[matrizesParaSoma[i+1]])
        return soma

def validaMatrizes(listaMatrizes, index1, index2):
    linhasMatriz1 = len(listaMatrizes[index1])
    colunasMatriz1 = len(listaMatrizes[index1][0])

    linhasMatriz2 = len(listaMatrizes[index2])
    colunasMatriz2 = len(listaMatrizes[index2][0])

    if linhasMatriz1 == linhasMatriz2 and colunasMatriz1 == colunasMatriz2:
        return True
    else:
        return False