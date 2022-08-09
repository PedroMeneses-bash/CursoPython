def aumentar(valor, taxa, format = False):

    s = valor + valor*taxa/100
    
    if format:
        return moeda(s)
    else:
        return s



def diminuir(valor, taxa, format = False):

    s = valor - valor*taxa/100

    if format:
        return moeda(s)
    else:
        return s


def dobro(valor, format = False):
    
    s = valor * 2
    if format:
        return moeda(s)
    else:
        return s

def metade(valor, format = False):

    s = valor / 2
    
    if format:
        return moeda(s)
    else:
        return s


def moeda(valor = 0, moeda = 'R$'):
    return f'{moeda}{valor:.2f}'.replace('.',',')
