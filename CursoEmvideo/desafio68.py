from random import randint
soma_vit = 0
print('-='*25)
print('*'*12, 'VAMOS JOGAR PAR OU ÍMPAR', '*'*12)
while True:
    print('-=' * 25)
    num_pc = randint(0, 10)
    parimp_huma = str(input('Digite \033[1;33m[P]\033[m para Par ou \033[1;36m[I]\033[m para Ímpar: ')).strip().upper()[0]
    if parimp_huma == 'P':
        parimp_pc = 'Í'
    if parimp_huma in 'íÍiI':
        parimp_huma = 'Í'
        parimp_pc = 'P'

    num_huma = int(input('Digite um número: '))
    soma_num = num_pc + num_huma
    resp = ' '

    if soma_num % 2 == 0:
        resp = 'Par'
    elif soma_num % 2 == 1:
        resp = 'Ímpar'

    if parimp_huma == resp[0]:
        soma_vit += 1
        print('Parabéns Você \033[1;34mvenceu!\033[m')
        print(f'O computador jogou {num_pc} e você {num_huma}. Total {soma_num} que é {resp}')
        print('Vamos jogar novamente...')
    elif parimp_pc == resp[0]:
        print('Que pena, você \033[1;35mperdeu!\033[m')
        print(f'O computador jogou {num_pc} e você {num_huma}. Total {soma_num} que é {resp}')
        print('-='*25)
        break
print('='*50)
print(f'Fim de Jogo! Você venceu durante {soma_vit} vezes seguidas!')