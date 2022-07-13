nomeCliente = input('Qual seu nome ?')
valorCasa = float(input('Qual o valor da casa ?'))
salarioCliente = float(input('Qual sua renda mensal ?'))
qtdParcelas = int(input('Em quantos anos pretende pagar ?'))
qtdParcelas *= 12
valorPrestacao = valorCasa/qtdParcelas
if valorPrestacao <= salarioCliente*1.3:
    print("""Crédito aprovado {}.\n{}x parcelas de R${:.2f}""" .format(
        nomeCliente, qtdParcelas, valorPrestacao))
else:
    print('Infelizmente crédito não foi aprovado.')
