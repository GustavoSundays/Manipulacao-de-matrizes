def listar(listaDeMatriz):
    if len(listaDeMatriz) == 0:
        input(f'\nNenhuma matriz adicionada')
        return
    for i in range(len(listaDeMatriz)):
        print(f'\nMatriz {i+1}')
        for j in range(len(listaDeMatriz[i])):
            print(listaDeMatriz[i][j])
    input(f'\nPrecione qualquer tecla para continuar')