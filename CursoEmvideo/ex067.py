'''print('-'*20)
print('\033[1;36mTABUADA VIRTUAL\033[m')
print('-'*20)
while True: #enquanto for verdade execute o bloco abaixo
    numero = int(input('Digite um numero para ver sua tabuada: '))
    multiplicação = 0
    if numero > 0: # se numero for maior que zero print
        while multiplicação <= 10: # enquanto multiplicaçao for menor ou igual a 10
            operação = numero * multiplicação # variavel da operação multiplicação
            print(f'{numero} X {multiplicação} = {operação}')
            multiplicação += 1
    if numero < 0: # se numero for menor que zero quebre (pare) o loop
        break
print('\033[1;31mTabuada virtual encerrada. Volte sempre!!!\033[m')'''


print('-'*20)
print('\033[1;36mTABUADA VIRTUAL\033[m')
print('-'*20)
while True:
    num = int(input('Digite um numero para ver sua tabuada: '))
    if num < 0: # se numero for menor que zero quebre (pare) o loop
        break
    print(f'{num} x {1:2} = {num*1}')
    print(f'{num} x {2:2} = {num*2}')
    print(f'{num} x {3:2} = {num*3}')
    print(f'{num} x {4:2} = {num*4}')
    print(f'{num} x {5:2} = {num*5}')
    print(f'{num} x {6:2} = {num*6}')
    print(f'{num} x {7:2} = {num*7}')
    print(f'{num} x {8:2} = {num*8}')
    print(f'{num} x {9:2} = {num*9}')
    print(f'{num} x {10:2} = {num*10}')
    print('-'* 13)
print('\033[1;31mTabuada virtual encerrada.\033[m')