number001 = float(input('Digite o primeiro número: '))
number002 = float(input('Digite o segundo número: '))
number003 = float(input('Digite o terceiro número: '))

if number001 > number002:
    if number001 > number003:
        maiorNumero = number001
    else:
        menorNumero = number002

elif number002 > number003:
    maiorNumero = number002
    if number001 > number003:
        menorNumero = number003

else:
    maiorNumero = number003
    menorNumero = number001

print('O maior número é: {}\nO menor número é: {}' .format(maiorNumero, menorNumero))
