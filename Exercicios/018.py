import math

angulo = float(input('Digite o angulo: '))
sen = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))


print('Para o angulo {}° temos: \nSeno: {:.2f}\nCosseno: {:.2f}\nTangente: {:.2f}'.format(
    angulo, sen, cos, tan))
