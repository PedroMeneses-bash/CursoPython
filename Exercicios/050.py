somaPares = 0

for i in range(1, 7):
    number = int(input('Digite um número inteiro: '))

    if number % 2 == 0:
        somaPares += number
print(somaPares)
