
contadorFrase = 0
fraseInvertida = ''

frase = input('Digite a frase: ').strip().upper().replace(' ', '')
tamanhoFrase = len(frase)
for i in range(tamanhoFrase-1, -1, -1):
    fraseInvertida += frase[i]

print(frase)
print(fraseInvertida)

if frase == fraseInvertida:
    print('A frase é Palindromo.')
else:
    print('A frase não é palimdromo.')
