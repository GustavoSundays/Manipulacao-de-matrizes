def remover(listaMatrizes):
    index = int(input('Qual matriz deseja remover? '))
    index = index - 1
    listaMatrizes.pop(index)

    input('Pronto :)')