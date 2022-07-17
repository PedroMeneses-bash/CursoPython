primeiroTermo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiroTermo
cont = 1


while cont <= 10:
    print('{} ' .format(termo))
    termo += razao
    cont += 1


# for i in range(primeiroTermo, decimoTermo + razão, razão):
#    print('{} ' .format(c))
