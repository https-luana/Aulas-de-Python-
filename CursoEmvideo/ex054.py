from datetime import date
print(f'''\033[1;36m{'-='*10} 
GRUPO DA MAIOR IDADE 
{'-='*10}\033[m''')
atual = date.today().year
totalmaior = 0
totalmenor = 0
for pess in range(1, 8):
    nasc = int(input(f'Em que ano a {pess}° pessoa nasceu? '))
    idade = atual - nasc
    if idade >= 21:
        totalmaior += 1
    else:
        totalmenor += 1
print(f'\033[32mAo todo tivemos \033[4m{totalmaior}\033[m \033[32mpessoas maiores de idade\033[m')
print(f'\033[36mE tambem tivemos \033[4m{totalmenor}\033[m \033[36mpessoas menores de idade\033[m')
