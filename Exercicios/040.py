nota001 = float(input('Digite sua primeira nota: '))
nota002 = float(input('Digite sua segunda nota: '))

media = (nota001+nota002)/2

if media < 5.0:
    print('Reprovado.')
elif media >= 5.0 and media <= 6.9:
    print('Recuperação.')
else:
    print('Aprovado.')
