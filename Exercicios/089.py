from turtle import clearscreen
import os #para usar a função de limpar tela, é necessario importar esta biblioteca

dados = list()
listaAlunos = list()

while True:

    dados.append(input('Nome do aluno: '))
    dados.append(float(input('Nota 1: ')))
    dados.append(float(input('Nota 2: ')))
    dados.append((dados[1]+dados[2])/2)

    listaAlunos.append(dados[:])

    dados.clear()
    breakPrograma = input('Quer continuar? [S/N]').upper().strip()[0]
    if breakPrograma == 'N':
        break
os.system('cls')#comando para limpar tela, neste caso após preenchimento de informações
print('-='*13)
print(f'{"No.":<4}{"Nome":<8}{"Média":>6}')
print('--'*13)
for i, a in enumerate(listaAlunos):
    print(f'{i:<4}{a[0]:<8}{a[3]:>6}')
print('--'*13)

while True:
    numero=int(input(f'Informe o indice para ver a nota de algum aluno: '))
    
    if numero == 999:
        print('Programa Finalizado!')
        break
    elif numero >= len(listaAlunos):
        print('Aluno não encontrado.')    
    else:
        print('-='*13)
        print(f'{"No.":<4}{"Nome":<8}{"Nota 1":<6}{"Nota 2":>8}')
        print(f'{numero:<4}{listaAlunos[numero][0]:<8}{listaAlunos[numero][1]:>6}{listaAlunos[numero][2]:>8}')
        print('--'*13)
