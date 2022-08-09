#Modularização

import Uteis.utilidade.utilidades

num = int(input('Digite um valor: '))
fat = Uteis.utilidade.utilidades.fatorial(num)
print(f'O fatorial de {num} é {fat}.')
print(f'O dobro de {num} é {Uteis.utilidade.utilidades.dobro(num)}.')