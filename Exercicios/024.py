nomeCidade = input('Digite o nome da cidade: ').strip()
primeiroNomeCidade = nomeCidade.split()
if primeiroNomeCidade[0].find('Santo') >= 0:
    print('A cidade começa com Santo.')
else:
    print('A cidade não começa com Santo.')
