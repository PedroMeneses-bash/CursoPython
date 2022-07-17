numero = 0
somaNumeros = 0
contadorNumeros = 0
while True:
    numero = int(input('Informe um inteiro: '))
    if numero != 999:
        somaNumeros += numero
        contadorNumeros += 1
    else:
        break

print('Soma: {}' .format(somaNumeros))
print('E foram digitados {} números.' .format(contadorNumeros))
