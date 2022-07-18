contCedulaCinq = 0
contCedulaVinte = 0
contCedulaDez = 0


valor = int(input('Informe o valor a ser sacado: '))
restoValor = valor
numeroValor = str(valor)


unidade = valor // 1 % 10
restoValor -= unidade
contCedulaUm = unidade

dezena = (valor // 10 % 10)*10
restoValor -= dezena
restoDezena = dezena

while restoDezena != 0:
    if restoDezena >= 50:
        restoDezena -= 50
        contCedulaCinq += 1
    elif restoDezena < 50 and restoDezena >= 20:
        restoDezena -= 20
        contCedulaVinte += 1
    elif restoDezena == 10:
        restoDezena -= 10
        contCedulaDez += 1

contCedulaCinq += (restoValor/50)

contCedulaCinq = int(contCedulaCinq)
print(f'Notas de R$ 1,00 : {contCedulaUm}')
print(f'Notas de R$ 10,00: {contCedulaDez}')
print(f'Notas de R$ 20,00: {contCedulaVinte}')
print(f'Notas de R$ 50,00: {contCedulaCinq}')
