núm = cont = soma = 0
núm = int(input('\033[1;35mDIGITE UM NÚMERO\033[m\n[999 para parar]: '))
while núm != 999:
    soma += núm
    cont += 1
    núm = int(input('\033[1;35mDIGITE UM NÚMERO\033[m\n[999 para parar]: '))
print(f'Você digitou {cont} números e soma entre eles foi {soma}')