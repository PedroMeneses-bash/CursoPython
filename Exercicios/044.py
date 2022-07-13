valorProduto = float(input('Informe o valor do produto :'))
formaPagamento = input(
    'Qual a forma de pagamento:\n-À vista\n-Parcelado ').strip().upper()

if formaPagamento == 'A VISTA' or formaPagamento == 'Á VISTA' or formaPagamento == 'À VISTA' or formaPagamento == 'AVISTA' or formaPagamento == 'VISTA':
    formaPagamentoVista = input('Dinheiro,Cheque ou Cartão').strip().upper()
    if formaPagamentoVista == 'CARTÃO' or formaPagamentoVista == 'CARTAO':
        valorPagamento = valorProduto*0.95
        print()
    else:
        valorPagamento = valorProduto*0.9
        print('')
else:
    numeroParcelas = int(input('Informe o número de parcelas.'))
    if numeroParcelas < 2:
        valorPagamento = valorProduto*0.95
        print()
    elif numeroParcelas == 2:
        valorPagamento = valorProduto
        valorParcela = valorPagamento/numeroParcelas
        print()
    else:
        valorPagamento = valorProduto*1.2
        valorParcela = valorPagamento/numeroParcelas
        print()
