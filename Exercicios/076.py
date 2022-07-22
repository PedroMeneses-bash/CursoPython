listaProdutos = ('Pão', 9.90, 'Frango', 23.20, 'Arroz', 7.10, 'Feijão',
                 8.70, 'Farinha', 3.2, 'Leite', 4.10, 'Óleo', 13.5, 'Macarrão', 2.9)

print('-'*44)
print(f'{"LISTA DE COMPRAS":^44}')  # centralizado a 40 espaços
print('-'*44)  # 44 hifens


for i in range(0, len(listaProdutos)):
    if i % 2 == 0:

        # nome do produto em 35 posições e os vazios preenchidos com ponto e todo a esquerda(<)
        print(f'{listaProdutos[i]:.<35}', end='')

    else:
        # preço dos produtos todo a direita(>) no espaço de 7 posiçoes com duas casas decimais
        print(f'R${listaProdutos[i]:>7.2f}')
