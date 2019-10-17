from cls import cls

def menu():
    cls()
    print(f'\t Menu')
    print(f'1 - Adicionar matriz')
    print(f'2 - Listar matrizes')
    print(f'3 - Remover matriz')
    print(f'4 - Soma de matrizes')
    print(f'5 - Substracao de matrizes')
    print(f'6 - Multiplicacao de matrizes')
    print(f'7 - Inversa de matriz')
    print(f'8 - Transposta de matriz')
    print(f'9 - Determinante de matriz')
    print(f'0 - Sair')
    alternativa = int(input())

    return alternativa