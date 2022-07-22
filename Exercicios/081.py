listaNumeros = list()
qtdNumeros=0
while True:

    numero = int(input('Informe um numero: '))

    if numero not in listaNumeros:
        listaNumeros.append(numero)
        qtdNumeros+=1
    else:
        print('Valor duplicado! Não vou adicionar...')

    breakPrograma = input('Quer continuar? [S/N]').upper().strip()[0]
    if breakPrograma == 'N':
        break


print(f'Você digitou {qtdNumeros} valores.')
listaNumeros.sort(reverse=True)
print(f'Você digitou os valores {listaNumeros}')
if 5 in listaNumeros:
    print(f'O 5 foi digitado ')