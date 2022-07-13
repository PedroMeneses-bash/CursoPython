# Pra quando digitar já eliminar os espaço inuteis
nome = input('Digite o nome completo: ').strip()
print(nome.upper())
print(nome.lower())
# Conta o total de char menos a contagem de espaços entre os nomes
print(len(nome)-nome.count(' '))
print(nome.find(' '))
# OU
nome = nome.split()
print(len(nome[0]))  # imprime comprimento primeiro nome
