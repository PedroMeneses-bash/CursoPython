# help(input)

# print(input.__doc__)


def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela.
    :param i: inicio da contagem
    :param f: fim da contagem 
    :param p: passo da contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c}', end='')
        c += p
    print('FIM!')


help(contador)


def soma(a=0, b=0, c=0):

    s = a + b + c
    print(f'O resultado da soma foi: {s}')


soma(5, 3)
# se fosse um parametro sem igual a zero :
# def soma(a, b, c) essa função daria erro, mas como foi igualada a zero

print('*'*30)


def teste(b):  # ESCOPO LOCAL
    a = 8  # Variavel LOCAL
    b += 4  # Variavel LOCAL
    c = 2  # Variavel LOCAL
    print(f'a no escopo LOCAL vale {a}')
    print(f'b no escopo LOCAL vale {b}')
    print(f'c no escopo LOCAL vale {c}')


# ESCOPO GLOBAL
a = 5  # variavel GLOBAL
print(f'a no escopo GLOBAL vale {a}')  # Será impresso a = 8
teste(a)  # Já aqui será impresso a função

print('*'*30)


def teste(e):  # ESCOPO LOCAL
    global d  # Com isso, torno d do escopo LOCAL com uma variavel GLOBAL
    d = 8  # Variavel LOCAL
    e += 4  # Variavel LOCAL
    f = 2  # Variavel LOCAL
    print(f'a no escopo LOCAL vale {a}')
    print(f'b no escopo LOCAL vale {e}')
    print(f'c no escopo LOCAL vale {f}')


# ESCOPO GLOBAL
d = 5  # variavel GLOBAL
print(f'a no escopo GLOBAL vale {d}')  # Será impresso a = 8
teste(d)  # Já aqui será impresso a função


def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um número: '))
if par(num):
    print('É par!')
else:
    print('Não é par!')
