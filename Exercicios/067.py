
while True:

    numero = int(input('Informe um número para sair a tabuada: '))
    if numero < 0:
        break
    for i in range(1, 11):
        print(numero*i)
