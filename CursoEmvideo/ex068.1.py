from random import randint #importação de sortear
v = 0 # vitoria
while True: #enquanto infinita
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' ' # validação do tipo string par ou impar
    while tipo not in 'PI': #enquanto tipo nao for par ou impar(maiusculo)
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total} ', end= '')
    print('DEU PAR' if total %2 == 0 else 'DEU ÍMPAR') #OPERADOR TERNARIO
    if tipo == 'P':
        if total %2 == 0: # calculo par
            print('Você VENCEU!')
            v += 1 #contador de vitoria
        else:
            print('Você PERDEU')
            break # quebra o laço
    elif tipo == 'I': 
        if total %2 == 1: # calculo impar
            print('Você VENCEU')
            v += 1
        else:
            print('Você PERDEU')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {v} vezes.')
        