
from math import factorial
numero = int(input('Informe um número para fatorial: '))
fatorialNumero = numero
while numero > 1:

    fatorialNumero *= (numero-1)
    numero -= 1

print(fatorialNumero)

# OU UTILIZANDO IMPORTAÇÃO

n1 = int(input('Digite um número para descobrir o seu fatorial: '))
fatorial = factorial(n1)
print('O fatorial de {} é \033[1;38m{}\033[m'.format(n1, fatorial))
