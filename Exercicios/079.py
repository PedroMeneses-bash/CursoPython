listaNumeros = list()

while True:

    numero = int(input('Informe um numero: '))

    if numero not in listaNumeros:
        listaNumeros.append(numero)
    else:
        print('Valor duplicado! Não vou adicionar...')

    breakPrograma = input('Quer continuar? [S/N]').upper().strip()[0]
    if breakPrograma == 'N':
        break

listaNumeros.sort()
print(f'Você digitou os valores {listaNumeros}')
