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


def leiaFloat(texto):
    while True:
        try:
            num = float(input(texto))
        except TypeError:
            print('Informe um real válido.')
            continue
        except KeyboardInterrupt:
            print('O usuario preferiu não informar os dados.')
            break
        except ValueError:
            return 0
        else:
            return num


numInt = leiaInt('Digite um número: ')
numFloat = leiaFloat('Digite um número real: ')
print(f'Você acabou de digitar o número {numInt} e o {numFloat}.')
