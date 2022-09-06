def cadastro(nomeArq):
    


    while True:

        nome = input('Nome: ').capitalize()
        idade = int(input('Idade: '))
        try:
            a = open(nomeArq, 'at')
        except:
            print('ERROR ao gravar dados.')
        else:
            try:
                a.write(f'{nome};{idade}\n')
            except:
                print('Houve um problema no registro do dados.')
            else:
                print(f'{nome} registrado com sucesso. ')
                a.close()
        
        
        breakPrograma = input('Deseja cadastrar outra pessoa? [S/N]').upper().strip()[0]
        if breakPrograma == 'N':
            break

    