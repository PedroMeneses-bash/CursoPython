listaNumeros = list()

for i in range(0, 6):
    numero = int(input('Informe um número: '))

    if i == 0 or numero >= listaNumeros[-1]:
        listaNumeros.append(numero)
    else:
        pos = 0
        while pos < len(listaNumeros):
            if numero <= listaNumeros[pos]:
                listaNumeros.insert(pos, numero)
                break
            pos += 1
print(listaNumeros)
