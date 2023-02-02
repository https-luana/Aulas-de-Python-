print('-'*10, 'DESAFIO 67', '-'*10)
print()
print('='*10, '\033[1;34mTabuada eletronica do X\033[m', '='*10)
print()
while True:
    Num = int(input('Quer ver a tabuada de qual valor? '))
    mul = 0
    print('-'*30)
    if Num > 0:
        while mul <= 10:
            operação = Num * mul
            print(f'{Num} X {mul} = {operação}')
            mul += 1
        print('-'*30)
    if Num < 0:
        break
print('\033[1;31mTabuada eletronica encerrada. Volte sempre!!!\033[m')
