# Tuplas
lanche = ['hamburguer', 'suco', 'pizza', 'pudim']
print(lanche[1:])
print(lanche[-1])
print(len(lanche))
print(sorted(lanche))  # ordem alfabetica

for c in lanche:
    print(c)

a = (5, 6, 7, 8)
b = (1, 2, 3, 4, 5)
c = a+b  # concatena a e b, se fosse se fosse b + a seria outra ordem
print(c.index(5))  # posição que esta o primeiro 5
print(c.index(5, 2))  # posição do primeiro 5 a partir da posição 2
