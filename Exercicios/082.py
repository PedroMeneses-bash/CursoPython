listaNumeros = list()
listaPares = list()
listaImpares = list()


while True:

    numero = int(input('Informe um numero: '))
    if numero % 2 == 0:
        listaPares.append(numero)
    else:
        listaImpares.append(numero)

    if numero not in listaNumeros:
        listaNumeros.append(numero)
    else:
        print('Valor duplicado! Não vou adicionar...')

    breakPrograma = input('Quer continuar? [S/N]').upper().strip()[0]
    if breakPrograma == 'N':
        break

listaNumeros.sort()
listaImpares.sort()
listaPares.sort()
print(f'Você digitou os valores {listaNumeros}')
print(f'Você digitou os valores pares {listaImpares}')
print(f'Você digitou os valores impares {listaPares}')
