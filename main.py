from menu import menu
from adicionarMatriz import add
from listarMatrizes import listar
from removerMatriz import remover
from somaMatrizes import soma
from subtraiMatrizes import subtracao
from multiplicaMatrizes import multiplicacao
from inversaMatriz import inversa
from transpostaMatriz import transposta
from determinanteMatriz import determinante

alternativa = 1
matrizes = []
while alternativa != 0:
    alternativa = menu()
    if alternativa == 1:
        matrizes.append(add())
    elif alternativa == 2:
        listar(matrizes)
    elif alternativa == 3:
        remover(matrizes)
    elif alternativa == 4:
        resultSoma = soma(matrizes)
        print(f'Resultado da soma: ')
        print(resultSoma)
        input(f'\nPressione qualquer tecla para voltar ao menu')
    elif alternativa == 5:
        resultSubtracao = subtracao(matrizes)
        print(f'Resultado da subtracao: ')
        print(resultSubtracao)
        input(f'\nPressione qualquer tecla para voltar ao menu')
    elif alternativa == 6:
        resultMultiplicacao = multiplicacao(matrizes)
        print(f'Resultado da multiplicacao: ')
        print(resultMultiplicacao)
        input(f'\nPressione qualquer tecla para voltar ao menu')
    elif alternativa == 7:
        resultInversa = inversa(matrizes)
        print('Matriz original:')
        print(resultInversa[0])
        print() #quebra-linha
        print(f'Matriz inversa:')
        print(resultInversa[1])
        input(f'\nPressione qualquer tecla para voltar ao menu')
    elif alternativa == 8:
        resultTransposta = transposta(matrizes)
        print('Matriz original:')
        print(resultTransposta[0])
        print() #quebra-linha
        print(f'Matriz transposta:')
        print(resultTransposta[1])
        input(f'\nPressione qualquer tecla para voltar ao menu')
    elif alternativa == 9:
        resultDeterminante = determinante(matrizes)
        print('Matriz original:')
        print(resultDeterminante[0])
        print() #quebra-linha
        print(f'Determinante da matriz:')
        print(resultDeterminante[1])
        input(f'\nPressione qualquer tecla para voltar ao menu')
    elif alternativa == 0:
        input('Obrigado, volte sempre :)')
    else:
        input('Alternativa incorreta, precione qualquer tecla para tentar novamente')