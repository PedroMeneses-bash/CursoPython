nome = input('Digite o nome completo: ').strip()
nome = nome.split()  # dividiu
print('Primeiro nome: {}' .format(nome[0]))  # primeiro nome
# retorna o tamanho, com isso seria o valor do ultimo grupo de caracter
ultimoNome = len(nome)
# print(type(ultimoNome))
# -1 para ele dar a posição, pq começa com 0
print('Segundo nome: {}' .format(nome[ultimoNome-1]))
