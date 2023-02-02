print('-='*10)
print('''\033[1;36mBoletim online
Iforme sua nota\033[m''')
print('-='*10)
nota1 = float(input('\033[1mPrimeira nota:\033[m '))
nota2 = float(input('\033[1mSegunda nota:\033[m '))
média = (nota1 + nota2) / 2 
print(f'\033[1;37mTirando {nota1:.1f} e {nota2:.1f}, a média do aluno é {média:.1f}\033[m')
if média >=5 and média <7: # if 7 > média >= 5:
    print('\033[1;33mO aluno está em recuperação.\033[m')
elif média < 5:
    print('\033[1;31O aluno esta Reporvado.\033[m')
elif média >= 7:
    print('\033[1;34mO aluno está Aprovado.\033[m')      