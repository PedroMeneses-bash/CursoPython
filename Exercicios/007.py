# 007
nome = input('Qual seu nome ?')
nota001 = float(input('Qual foi a nota da sua AV1 ?'))
nota002 = float(input('Qual foi a nota da sua AV2 ?'))
nota003 = float(input('Qual foi a nota da sua AV3 ?'))
media = (nota001+nota002+nota003)/3

if media < 6:
    print('{} você foi reprovado com a nota {}.' .format(nome, media))
else:
    print('Parabéns {} você foi aprovado! Sua nota foi {}' .format(nome, media))
