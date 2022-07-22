lanche = ['Hamburguer', 'Refri', 'chocolate', 'churros', 'brigadeiro']

# insere SUCO mas na posição final, adicionar uma posição e inserindo o valor nela
lanche.append('Suco')

lanche.insert(0, 'SUCO')  # insere SUCO na posição 0
del lanche[3]  # deleta o valor da posição 3
lanche.pop(3)  # deleta tbm o valor da posição 3
lanche.pop()  # se não informa nada, ele pega o ultimo e deleta

# remove o valor especifico em qual for a posição(SUCO),mas remove o primeiro que ele encontrar, apaga tbm a posição e a lista se reajusta
lanche.remove('SUCO')
# se mandar lanche.remove() e não o valor não existir, retorna ERRO. Então é sugerido usar um IF

# cria uma lista com valores de 4 a 10, e aplica a lista "valores"
valores = list(range(4, 11))

valores = [8, 2, 5, 4, 9, 3, 0]
valores.sort()  # ordena menor ao maior
valores.sort(reverse=True)  # ordena do maior ao menor
len(valores)  # retorna tbm tamanho da lista

# Criando Lista Vazia
valores001 = []
# Ou assim
valores002 = list()


valores001.append(5)
valores001.append(9)
valores001.append(4)
for c, v in enumerate(valores001):
    print(f'Na posição {c} encontrei o valor {v}.')


for cont in range(0, 5):
    valores002.append(int(input('Digite um valor: ')))


a = [2, 3, 4, 7]
b = a  # elas literalmente se igualam, se muda A muda B e se muda B tbm muda A
b[2] = 8  # aqui muda B as tbm acaba alterando A
c = a[:]  # aqui somente copia os valores
c[2] = 0  # com isso não muda a tbm
