from time import sleep
print('-='*8)
print('''\033[1;37mBoletim online
informe sua nota\033[m''')
print('-='*8)
nota1 = float(input('Digite sua 1° nota: '))
nota2 = float(input('Digite sua 2° nota: '))
média = (nota1 + nota2) /2
print('\033[1;37mcarrendo suas informçoes aguarde...\033[m')
sleep(2)
print(f'Caro aluno, sua 1° nota foi \033[1;37m{nota1}\033[m e sua 2° nota \033[1;37m{nota2}\033[m calculando sua média em {média} seu resultado será')
if média >=5 and média <7:
    print('\033[1;33mEm recuperão\033[m')
elif média < 5:
    print('\033[1;31mReprovado.\033[m')
elif média >= 7:
    print('\033[1;34mAprovado!\033[m')    