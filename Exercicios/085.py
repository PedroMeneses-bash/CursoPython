listaNumero = list()
listaPares = list()
listaImpares = list()

for i in range(0, 7):
    listaNumero.append(int(input('Informe um número: ')))

    if listaNumero[i] % 2 == 0:
        listaPares.append(listaNumero[i])
    else:
        listaImpares.append(listaNumero[i])

listaPares.sort()
listaImpares.sort()

print(f'Pares: {listaPares}')
print(f'Impares: {listaImpares}')
