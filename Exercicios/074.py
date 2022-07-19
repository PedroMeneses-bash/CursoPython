from random import randint

tuplaNumeros = (randint(1, 100), randint(1, 100), randint(
    1, 100), randint(1, 100), randint(1, 100))
maiorNumero = 0
menorNumero = 100


for i in range(0, 5):
    print(tuplaNumeros[i], end=' ')
    if tuplaNumeros[i] > maiorNumero:
        maiorNumero = tuplaNumeros[i]
    if tuplaNumeros[i] < menorNumero:
        menorNumero = tuplaNumeros[i]

print(f'\nO maior número foi o {maiorNumero}')
print(f'E o menor número foi o {menorNumero}')
