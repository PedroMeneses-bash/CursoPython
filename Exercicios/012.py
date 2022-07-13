nomeProduto = input('Qual o nome do produto? ')
precoProduto = float(input('Qual o preço do produto? '))
precoProduto = precoProduto*0.95
print('O {} pode ser vendido no valor de R${:.2f}.' .format(
    nomeProduto, precoProduto))
