##Parte 2 - variaveis compostas(listas), basicamente o conceito de matriz

teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])


galera2 = [['João' , 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
for p in galera2:
    print(f'{p[0]} tem {p[1]} anos de idade.')

dado = list()
galera3=list()
totalMaior = 0
totalMenor = 0

for c in range(0,3):
    dado.append((input('Nome: ').strip()))
    dado.append(int(input('Idade: ')))
    galera3.append(dado[:])
    dado.clear()

for p in galera3:
    print(f'{p[0]} tem {p[1]} anos de idade.')



for x in galera3:
    if x[1] >= 18:
        print(f'{x[0]} é maior de idade.')
        totalMaior+=1
    else:
        print(f'{x[0]} não é maior de idade.')
        totalMenor+=1

print(f'{totalMaior} pessoas são maior de idade e {totalMenor} pessoas são menores de idade.')