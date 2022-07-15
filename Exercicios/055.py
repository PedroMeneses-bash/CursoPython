
maiorPeso = 0.0
menorPeso = 999999999.9

for i in range(0, 6):

    peso = float(input('Digite seu pedo: '))

    if peso > maiorPeso:
        maiorPeso = peso
    elif peso < menorPeso:
        menorPeso = peso


print(maiorPeso, menorPeso)
