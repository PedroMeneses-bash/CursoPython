import math
catetoAdj=float(input('Digite o valor do cateto adjcente: '))
catetoOposto=float(input('Digite a medida do cateto oposto: '))
hipotenusa001=math.sqrt(catetoAdj**2+catetoOposto**2)


hipotenusa002=math.hypot(catetoOposto,catetoAdj)

print('O valor da hipotenusa calculada manual foi de : {}' .format(hipotenusa001))
print('O valor da Hipotenusa feito pela função é de : {}' .format(hipotenusa002))