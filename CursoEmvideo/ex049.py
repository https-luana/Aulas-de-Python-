print(f'\033[1;35m {"="*10} TABUADA {"="*10}\033[m')
num = int(input('Digite um numero para ver sua tabuada: '))
for c in range(1, 11):
    print(f'{num} x {c:2} = {num*c}')
    
