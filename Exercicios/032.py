from datetime import date

ano=int(input('Digite o ano para saber se é bissexto: \nDigite 0 se for o ano em questão.'))

if ano == 0 :
    ano=date.today().year

if ano%4 == 0 and ano%100 != 0 or ano%400 == 0:#divisivel por 4 e multiplo de 100 ou 400
    print('{} é bissexto.' .format(ano))
else:
    print('{} não é bissexto.' .format(ano))