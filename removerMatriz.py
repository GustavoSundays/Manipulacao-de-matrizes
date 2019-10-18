def remover(listaMatrizes):
    if len(listaMatrizes) == 0:
        input(f'\nNenhuma matriz adicionada')
        return
    index = int(input('Qual matriz deseja remover? '))
    index = index - 1
    listaMatrizes.pop(index)

    input('Pronto :)')