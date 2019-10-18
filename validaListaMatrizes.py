def validaListaMatriz(listaMatrizes):
    if len(listaMatrizes) == 0:
        isMatrizCadastrada = False
        input('Nenhuma matriz cadastrada, selecione a opção "1" no menu para cadastrar alguma matriz e poder realizar a operação desejada.')
    else:
        isMatrizCadastrada = True
    return isMatrizCadastrada