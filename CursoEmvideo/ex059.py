from time import sleep
print(f'\n\033[1;36m*CALCULADORA VIRTUAL*\033[m\n{"="*30}')
escolha = 0 # a escolha das operações matemticas
pve = int(input('Digite o primeiro valor: ')) # primeiro valor escolhido
sve = int(input('digite outro valor: ')) # segundo valor escolhido
while escolha != 5:
    escolha = int(input(f'{"="*30}\nOPÇÃO[1] SOMAR\nOPÇÃO[2] MULTIPLICAR\nOPÇÃO[3] MAIOR\nOPÇÃO[4] NOVOS NÚMEROS\nOPÇÃO[5] SAIR\n\033[1;35mDigite qual operaçao deseja iniciar: \033[m'))
    print('Carregando resultados aguarde...')
    sleep(1)
    print('')
    if escolha == 1:
        print(f'A soma dos valores \033[33m{pve}\033[m e \033[33m{sve}\033[m resulta em \033[32m{pve + sve}\033[m')
    elif escolha == 2:
        print(f'A multiplicação dos valores \033[33m{pve}\033[m e \033[33m{sve}\033[m resulta em \033[32m {pve * sve}\033[m')
    elif escolha == 3 and pve > sve:
        print(f'O maior valor entre \033[33m{pve}\033[m e \033[33m{sve}\033[m será \033[32m{pve}\033[m')
    elif escolha == 3 and pve < sve:
        print(f'O maior valor entre \033[33m{pve}\033[m e \033[33m{sve}\033[m será \033[32m{sve}\033[m')
    elif escolha == 3 and pve == sve:
        print('O valores são iguais')
    elif escolha == 4:
        pve = int(input('Digite o primeiro valor: '))
        sve = int(input('digite outro valor: '))
    elif escolha == 5:
        print('\n----Programa finalizado----')
    else:
        print('\033[31mEscolha Inválida!')
        sleep(0.5)
        print('\033[33mTente novamente!\033[m')
    sleep(1)
    print('')



