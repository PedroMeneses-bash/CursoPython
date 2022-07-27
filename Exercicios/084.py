listaPeso = list()
dado = list()
maiorPeso = 0
menorPeso = 0

while True:

    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    listaPeso.append(dado[:])

    if menorPeso == 0:
        menorPeso = dado[1]
    else:
        if dado[1] < menorPeso:
            menorPeso = dado[1]

        if dado[1] > maiorPeso:
            maiorPeso = dado[1]

    dado.clear()
    breakPrograma = input('Quer continuar? [S/N]').upper().strip()[0]
    if breakPrograma == 'N':
        break

print(f'Ao todo você cadastrou {len(listaPeso)} pessoas.')
print(f'O maior peso foi de {maiorPeso:.2f}Kg, que foram os pesos de :')
for p in listaPeso:
    if p[1] == maiorPeso:
        print(p[0])
print(f'O menor peso foi de {menorPeso:.2f}Kg, que foram os pesos de :')
for p in listaPeso:
    if p[1] == menorPeso:
        print(p[0])
