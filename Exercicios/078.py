valores = list()
maiorNumero = 0
menorNumero = 9999

for i in range(0, 5):
    valores.append(int(input('Digite um valor a ser inserido na lista: ')))

    if valores[i] > maiorNumero:
        maiorNumero = valores[i]
        poscMaior = i

    if valores[i] < menorNumero:
        menorNumero = valores[i]
        poscMenor = i

print(
    f'O maior número foi: {maiorNumero} na posição {poscMaior}\nE o menor: {menorNumero} na posição {poscMenor}.')
