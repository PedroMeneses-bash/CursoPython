def linha():
    print('-'*35)


def leiaInt(texto):

    while True:
        try:
            num = int(input(texto))

        except TypeError:
            print('Informe um inteiro válido.')
            continue
        except KeyboardInterrupt:
            print('O usuario preferiu não informar os dados.')
            break
        except ValueError:
            return 0
        else:
            return num


def titulo(txt):
    linha()
    print(txt.center(35))
    linha()


def menu(lista):

    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    linha()
    num = leiaInt('Sua opção: ')
    return num
