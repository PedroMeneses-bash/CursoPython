numero = 0
somaNumeros = 0
contadorNumeros = 0
maiorNumero = 0
menorNumero = 999

while numero != 999:
    numero = int(input('Informe um inteiro: '))
    if numero != 999:
        somaNumeros += numero
        contadorNumeros += 1

        if numero > maiorNumero:
            maiorNumero = numero
        elif numero < menorNumero:
            menorNumero = numero

mediaNumeros = somaNumeros/contadorNumeros

print('Média: {:.2f}' .format(mediaNumeros))
print('O maior número foi {} e o menor foi {}.' .format(maiorNumero, menorNumero))
