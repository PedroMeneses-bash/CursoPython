def aumentar(valor, taxa, format=False):

    s = valor + valor*taxa/100

    if format:
        return moeda(s)
    else:
        return s


def diminuir(valor, taxa, format=False):

    s = valor - valor*taxa/100

    if format:
        return moeda(s)
    else:
        return s


def dobro(valor, format=False):

    s = valor * 2
    if format:
        return moeda(s)
    else:
        return s


def metade(valor, format=False):

    s = valor / 2

    if format:
        return moeda(s)
    else:
        return s


def moeda(valor=0, moeda='R$'):
    return f'{moeda}{valor:.2f}'.replace('.', ',')


def resumo(valor=0, taxaa=0, taxar=0):
    print('-'*35)
    print('RESUMO DO VALOR'.center(35))
    print('-'*35)
    print(f'Preço analisado: \t{moeda(valor)}')
    print(f'Preço com aumento: \t{aumentar(valor,taxaa, True)}')
    print(f'Preço com redução: \t{diminuir(valor,taxar, True)}')
    print(f'Dobro do preço: \t{dobro(valor, True)}')
    print(f'Metade do valor: \t{metade(valor, True)}')
    print('-'*35)
