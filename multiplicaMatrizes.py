import numpy as np

def multiplicacao(listaMatrizes):
    qtdMatrizMultiplicacao = int(input(f'Há cadastradas {len(listaMatrizes)} matrizes, quantas deseja usar na multiplicacao? '))
    matrizesParaMultiplicacao = []
    multiplicacao = np.matrix(0)

    for i in range(qtdMatrizMultiplicacao):
        index = int(input(f'Qual seria a {i+1} matriz para multiplicacao? ')) - 1
        matrizesParaMultiplicacao.append(index)
        if len(matrizesParaMultiplicacao) > 1:
            isTamanhosIguais = validaMatrizes(listaMatrizes, matrizesParaMultiplicacao[0], index)
            if isTamanhosIguais == False:
                matrizesParaMultiplicacao.remove(index)
            while isTamanhosIguais == False:
                desejaSelecionarOutra = input(f'Matriz {index+1} tem tamanhos diferentes das outras matrizes, deseja selecionar outra? [S/N]').upper()
                if desejaSelecionarOutra == 'S':
                    index = int(input(f'Qual seria a {i+1} matriz para multiplicacao? ')) - 1
                    isTamanhosIguais = validaMatrizes(listaMatrizes, matrizesParaMultiplicacao[0], index)
                    if isTamanhosIguais == True:
                        matrizesParaMultiplicacao.append(index)
                else:
                    isTamanhosIguais = True
                    if len(matrizesParaMultiplicacao) >= 2:
                        for i in range(len(matrizesParaMultiplicacao)):
                            if i == 0 and len(matrizesParaMultiplicacao) > 1:
                                multiplicacao = np.matrix(listaMatrizes[matrizesParaMultiplicacao[i]]) * np.matrix(listaMatrizes[matrizesParaMultiplicacao[i+1]])
                                continue
                            elif i + 2 <= len(matrizesParaMultiplicacao):
                                multiplicacao -= np.matrix(listaMatrizes[matrizesParaMultiplicacao[i+1]])
                        return multiplicacao
                    else:
                        multiplicacao = np.matrix(listaMatrizes[matrizesParaMultiplicacao[0]])
                        return multiplicacao
    
    for i in range(len(matrizesParaMultiplicacao)):
        if len(matrizesParaMultiplicacao) == 1:
            multiplicacao = np.matrix(listaMatrizes[matrizesParaMultiplicacao[i]])
        elif i == 0:
            multiplicacao = np.matrix(listaMatrizes[matrizesParaMultiplicacao[i]]) * np.matrix(listaMatrizes[matrizesParaMultiplicacao[i+1]])
            continue
        elif i + 2 <= len(matrizesParaMultiplicacao):
            multiplicacao *= np.matrix(listaMatrizes[matrizesParaMultiplicacao[i+1]])
        return multiplicacao

def validaMatrizes(listaMatrizes, index1, index2):
    colunasMatriz1 = len(listaMatrizes[index1][0])
    linhasMatriz2 = len(listaMatrizes[index2])

    if colunasMatriz1 == linhasMatriz2:
        return True
    else:
        return False