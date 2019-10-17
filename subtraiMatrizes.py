import numpy as np

def subtracao(listaMatrizes):
    qtdMatrizSubtracao = int(input(f'Há cadastradas {len(listaMatrizes)} matrizes, quantas deseja usar na subtracao? '))
    matrizesParaSubtracao = []
    subtracao = np.matrix(0)

    for i in range(qtdMatrizSubtracao):
        index = int(input(f'Qual seria a {i+1} matriz para subtracao? ')) - 1
        matrizesParaSubtracao.append(index)
        if len(matrizesParaSubtracao) > 1:
            isTamanhosIguais = validaMatrizes(listaMatrizes, matrizesParaSubtracao[0], index)
            if isTamanhosIguais == False:
                matrizesParaSubtracao.remove(index)
            while isTamanhosIguais == False:
                desejaSelecionarOutra = input(f'Matriz {index} tem tamanhos diferentes das outras matrizes, deseja selecionar outra? [S/N]').upper()
                if desejaSelecionarOutra == 'S':
                    index = int(input(f'Qual seria a {i+1} matriz para subtracao? ')) - 1
                    isTamanhosIguais = validaMatrizes(listaMatrizes, matrizesParaSubtracao[0], index)
                    if isTamanhosIguais == True:
                        matrizesParaSubtracao.append(index)
                else:
                    isTamanhosIguais = True
                    if len(matrizesParaSubtracao) >= 2:
                        for i in range(len(matrizesParaSubtracao)):
                            if i == 0 and len(matrizesParaSubtracao) > 1:
                                subtracao = np.matrix(listaMatrizes[matrizesParaSubtracao[i]]) - np.matrix(listaMatrizes[matrizesParaSubtracao[i+1]])
                                continue
                            elif i + 2 <= len(matrizesParaSubtracao):
                                subtracao -= np.matrix(listaMatrizes[matrizesParaSubtracao[i+1]])
                        return subtracao
                    else:
                        subtracao = np.matrix(listaMatrizes[matrizesParaSubtracao[0]])
                        return subtracao
    
    for i in range(len(matrizesParaSubtracao)):
        if len(matrizesParaSubtracao) == 1:
            subtracao = np.matrix(listaMatrizes[matrizesParaSubtracao[i]])
        elif i == 0:
            subtracao = np.matrix(listaMatrizes[matrizesParaSubtracao[i]]) - np.matrix(listaMatrizes[matrizesParaSubtracao[i+1]])
            continue
        elif i + 2 <= len(matrizesParaSubtracao):
            subtracao -= np.matrix(listaMatrizes[matrizesParaSubtracao[i+1]])
        return subtracao

def validaMatrizes(listaMatrizes, index1, index2):
    linhasMatriz1 = len(listaMatrizes[index1])
    colunasMatriz1 = len(listaMatrizes[index1][0])

    linhasMatriz2 = len(listaMatrizes[index2])
    colunasMatriz2 = len(listaMatrizes[index2][0])

    if linhasMatriz1 == linhasMatriz2 and colunasMatriz1 == colunasMatriz2:
        return True
    else:
        return False