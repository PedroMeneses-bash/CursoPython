#Módulos
#https://docs.python.org/3/library/index.html  <-----Todas as bibliotecas
#https://pypi.org/                             <-----PyPI

import emoji
import random
from math import sqrt
number001= random.randint(1,100)#gera numeros int random de 1 até 100
raizNumber001=sqrt(number001) # importando somente uma função não precisa referenciar (math.sqrt)
print("A raiz de {} é igua a {:.2f}".format(number001, raizNumber001), end="")
print(emoji.emojize(':astonished_face:'))