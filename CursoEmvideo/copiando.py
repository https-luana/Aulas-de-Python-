from datetime import date
from time import sleep
nome = str(input('olá, qual é o seu nome: ')).title().strip().split()
print('''[1] para MASCULINO
[2] para FEMININO''')
sexo = int(input('Qual é seu sexo: '))
if sexo == 1:
    ano = date.today().year
    anouser = int(input('Informe o ano de nascimento: '))
    idade = ano - anouser
    print('='*5,'PROCESSANDO','='*5)
    sleep(2)
    print(f'Em {ano}, {nome[0]} está com {idade} anos') 
    if idade < 18:
        falta = 18 - idade
        data = ano + falta
        if falta > 1:
            print(f'{nome[0]}, ainda falta {falta} ano(s) para seu alistamento')
            print(f'Seu alistamento será em {data}')
        elif falta == 1:
            print(f'{nome[0]}, ainda falta {falta} ano para seu alistamento')
            print(f'Seu alistamento será {data}')
    elif idade == 18:
        print(f'{nome[0]}, seu alistamento é neste ano. ALISTE-SE IMEDIATAMENTE')
    else:
        passou = (ano - anouser) - 18
        data = ano - passou
        print(f'{nome[0]}, já passou {passou} anos desde o ano do seu alistamento!')
        print(f'Seu alistamento foi em {data}')
elif sexo == 2:
    print(f'Você, {nome[0]}, não precisa fazer o alistamento obrigatório')
else:
    print('OPÇÃO INVALIDA. TENTE NOVAMENTE!')
