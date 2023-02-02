núm = int(input('Digite um número: '))
tot = 0
for c in range(1, núm + 1):
    if núm % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')      
    print(f'{c} ', end='')
print(f'\n\033[mO número {núm} foi divisivel {tot} vezes')
if tot == 2:
    print('E por isso ele é primo!')
else:
    print('E por isso ele nao é primo!')