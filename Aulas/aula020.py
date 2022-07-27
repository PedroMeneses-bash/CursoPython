
def titulo(texto):
    print('-'*44)
    print(f'{texto:^44}')  # centralizado a 40 espaços
    print('-'*44)


titulo('LISTA DE COMPRAS')
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


def soma(x, y):
    s = x + y
    return s


print(soma(1, 1))

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


def somaMuitos(*valores):
    r = 0
    for num in valores:
        r += num

    return r


print(somaMuitos(0, 1))
print(somaMuitos(0, 1, 4, 5, 4))
print(somaMuitos(0, 1, 4))


def contador(*num):  # quando há muitos parametros
    print(num)  # Nessa função será criada tuplas com os numeros


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [7, 2, 5, 0, 4]
dobra(valores)
print(valores)
