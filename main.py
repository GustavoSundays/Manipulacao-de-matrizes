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
from validaListaMatrizes import validaListaMatriz

alternativa = 1
matrizes = []
while alternativa != 0:
    alternativa = menu()
    if alternativa == 1: #adicionar matriz
        matrizes.append(add())
    elif alternativa == 2: #lista de matrizes
        listar(matrizes)
    elif alternativa == 3: #remover matriz
        remover(matrizes)
    elif alternativa == 4: #soma de matrizes
        if validaListaMatriz(matrizes):
            resultSoma = soma(matrizes)
            print(f'Resultado da soma: ')
            print(resultSoma)
            input(f'\nPressione qualquer tecla para voltar ao menu')
    elif alternativa == 5: #subtração de matrizes
        if validaListaMatriz(matrizes):
            resultSubtracao = subtracao(matrizes)
            print(f'Resultado da subtracao: ')
            print(resultSubtracao)
            input(f'\nPressione qualquer tecla para voltar ao menu')
    elif alternativa == 6: #multiplicação de matrizes
        if validaListaMatriz(matrizes):
            resultMultiplicacao = multiplicacao(matrizes)
            print(f'Resultado da multiplicacao: ')
            print(resultMultiplicacao)
            input(f'\nPressione qualquer tecla para voltar ao menu')
    elif alternativa == 7: #inversa da matriz
        if validaListaMatriz(matrizes):
            resultInversa = inversa(matrizes)
            print('Matriz original:')
            print(resultInversa[0])
            print() #quebra-linha
            print(f'Matriz inversa:')
            print(resultInversa[1])
            input(f'\nPressione qualquer tecla para voltar ao menu')
    elif alternativa == 8: #transposta da matriz
        if validaListaMatriz(matrizes):
            resultTransposta = transposta(matrizes)
            print('Matriz original:')
            print(resultTransposta[0])
            print() #quebra-linha
            print(f'Matriz transposta:')
            print(resultTransposta[1])
            input(f'\nPressione qualquer tecla para voltar ao menu')
    elif alternativa == 9: #determinante da matriz
        if validaListaMatriz(matrizes):
            resultDeterminante = determinante(matrizes)
            print('Matriz original:')
            print(resultDeterminante[0])
            print() #quebra-linha
            print(f'Determinante da matriz:')
            print(resultDeterminante[1])
            input(f'\nPressione qualquer tecla para voltar ao menu')
    elif alternativa == 0: #sair
        input('Obrigado, volte sempre :)')
    else:
        input('Alternativa incorreta, precione qualquer tecla para tentar novamente')