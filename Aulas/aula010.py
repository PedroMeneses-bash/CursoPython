tempo=int(input('Quantos anos tem seu carro ?'))
if tempo <= 3:
    print('Seu carro é novo.')
else:
    print ('Seu carro é velho.')

#OU

print('Carro novo.'if tempo <= 3 else 'Carro velho.')