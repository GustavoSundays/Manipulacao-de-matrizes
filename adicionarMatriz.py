def add():
    print()
    linha = int(input(f'\nDigite a quantidade de linhas de sua matriz: '))
    coluna = int(input(f'Digite a quantidade de colunas de sua matriz: '))
    matriz = [[0 for i in range(coluna)] for j in range(linha)]

    print('') #quebra linha
    for i in range(linha):
        for j in range(coluna):
            matriz[i][j] = (float(input(f'Posicao {i+1}, {j+1}: ')))

    return matriz