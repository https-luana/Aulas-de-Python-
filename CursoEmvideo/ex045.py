print('\033[1;34;40m ====== J o k e n p ô ====== \033[m')
from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('''Suas opções:
[0]PEDRA
[1]PAPEL
[2]TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!')
print('-='*15)
print(f'O computador escolheu {itens[computador]}')
print(f'Jogador jogou {itens[jogador]} ')
print('-='*15)
if computador == 0:# o computador jogou pedra
    if jogador == 0:
        print('EMPATE :)')
    elif jogador == 1:
        print('VOCÊ GANHOU!')
    elif jogador == 2:
        print('COMPUTADOR VENCEU ;)')
    else:
        print('JOGADA INVALIDA!')    
elif computador == 1:# o computador jogou papel
    if jogador == 0:
        print('COMPUTADOR VENCEU ;)')
    elif jogador == 1:
        print('EMPATE :)')
    elif jogador == 2:
        print('VOCÊ VENCEU!')
    else:
        print('JOGADA INVALIDA!')
elif computador == 2: #o computador jogou tesoura   
    if jogador == 0:
        print('VOCÊ VENCEU!')
    elif jogador == 1:
        print('COMPUTADOR VENCEU ;)')
    elif jogador == 2:        
        print('EMPATE')
    else:
        print('JOGADA INAVALIDA!')    