def leiaInt(texto):

    while True:
        num = input(f'{texto}')
        if num.isnumeric():
            num = int(num)
            break
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
    return num


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
