from email.headerregistry import ContentTypeHeader


numero = int(input('Digite um numero: '))
contadorPrimo = 0
for i in range(1, numero+1):
    if numero % i == 0:
        contadorPrimo += 1
if contadorPrimo == 2:
    print('{} é primo.' .format(numero))
else:
    print('{} não é primo.' .format(numero))
