def maior(*valores):
    maiorNumero = 0
    for num in valores:
        if num > maiorNumero:
            maiorNumero = num

    return maiorNumero


print(maior(1, 3, 4, 9, 10, 15, 1, 0, 2))
print(maior(1, 3, 4, 20))
print(maior(1, 3, 4, 9, 10))
print(maior(100, 30, 25, 62))
