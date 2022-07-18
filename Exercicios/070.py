valorTotal = 0.0
contPrecoMil = 0
precoMaisBarato = 99999999.9
nomeProdutoMaisBarato = ' '
while True:
    nomeProduto = input('Nome do produto: ')
    precoProduto = float(input('Preço: R$ '))

    valorTotal += precoProduto

    if precoProduto > 1000:
        contPrecoMil += 1
    if precoProduto < precoMaisBarato:
        precoMaisBarato = precoProduto
        nomeProdutoMaisBarato = nomeProduto

    repete = ' '
    while repete not in 'SN':
        repete = input('Deseja repetir o processo ? S/N').upper().strip()[0]

    if repete == 'N':
        break
print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
print(f'Total da compra: R${valorTotal}')
print(f'{contPrecoMil} produtos custam mais de R$ 1.000,00')
print(f'Produto mais barato: {nomeProdutoMaisBarato}.')
print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
