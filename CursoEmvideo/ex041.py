from datetime import date
print('\033[0;35m-=\033[m'*16)
print('\033[1mConfederação Nacional de Natação\033[m')
print('\033[0;35m=-\033[m'*16)
ano = date.today().year
nasc = int(input('Qual é o seu ano de nascimento: '))
idade = ano - nasc
print(f'O atleta tem {idade} anos.')
if idade <= 9:
    print('Classificação: \033[1mMIRIM\033[m')
elif idade <= 14:
    print('Classifição:\033[1m INFANTIL\033[m')    
elif idade <= 19:
    print('Classificação:\033[1m JUNIOR \033[m')
elif idade <= 25:
    print('Classificação:\033[1m SÊNIOR')
else:
    print('Classificação:\033[1m MASTER\033[m')