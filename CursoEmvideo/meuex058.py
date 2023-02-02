from random import randint
from time import sleep

print(F"\033[1m{'-='*10}\nJOGO DA ADIVINHAÇÃO\n{'=-'*10}\033[m\n")
computador = randint(0, 10) # faz o computador "pensar"
jogador = 0
tentativa = 0
print(f"\033[1;32mVou pensar em um número entre 0 e 10. Tente adivinhar...\033[m\n{'-'*55}")
while jogador != computador:
    jogador = int(input('Em que número eu pensei? ')) # o jogador tenta adivinhar
    tentativa += 1
    print('PROCESSANDO...')
    sleep(2)
    if jogador!= computador: # se for diferente de jogador o computador ganha
        print(f'\033[1;31mERROU! TENTE NOVAMENTE\033[m Eu pensei no número {computador} e não {jogador}!')
    else: # se nao, jogador for igual ao computador jogador ganha
        print(f'\033[1mPARABÉNS! Você me venceu!\nVocê precisou de {tentativa} tentativas para acertar!\033[m')