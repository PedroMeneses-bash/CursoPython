nome=input('Digite o nome completo: ').strip()#Pra quando digitar já eliminar os espaço inuteis
print(nome.upper())
print(nome.lower())
print(len(nome)-nome.count(' '))#Conta o total de char menos a contagem de espaços entre os nomes
print(nome.find(' '))
#OU
nome=nome.split()
print(len(nome[0]))

