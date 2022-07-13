primeiroNumero = int(input('Informe o primeiro número: '))
segundoNumero = int(input('Informe o segundo número: '))

if primeiroNumero > segundoNumero:
    print('{} é maior que {}.' .format(primeiroNumero, segundoNumero))
elif primeiroNumero < segundoNumero:
    print('{} é maior que {}' .format(segundoNumero, primeiroNumero))
else:
    print('{} e {} são iguais.' .format(primeiroNumero, segundoNumero))
