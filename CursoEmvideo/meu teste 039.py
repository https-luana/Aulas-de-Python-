from datetime import date
print('-='*20)
print('\033[1mBem vindo digite suas iformações\033[m')
print('-='*20)
nome = str(input('Qual é o seu nome? ')).title().strip().split()
print('''\033[1;36m[1] para MASCULINO
[2] para FEMININO \033[m''')
sexo = int(input('Digite a opção que corresponde ao seu genero: '))
if sexo == 1:
    atual = date.today().year
    nasc = int(input('Qual é o seu ano de nascimento: '))
    idade = atual - nasc
    print(f'* {nome[0]},quem nasceu em {nasc} tem {idade} anos em {atual}')
    if idade == 18:
        print('Você deve se alistar imediatamente!')
    elif idade < 18:
        saldo = 18 - idade 
        print(f'* Ainda faltam {saldo} anos para o alistamento.')
        ano = atual + saldo
        print(f'''* Seu alistamento será em {ano}.
        *** FINALIZADO ***''')
    else: 
        idade > 18
        saldo = idade - 18
        print(f'* Você já deveria ter se alistado há {saldo} anos.')
        ano = atual - saldo
        print(f'''* Seu alistamento foi em {ano}.
        *** FINALIZADO ***''')
elif sexo == 2:
    print(f'''{nome[0]}, você não precisa fazer o alistamento obrigatório
    *** FINALIZADO ***''')
else:
    print('\033[7mOPÇÃO INVALIDA. TENTE NOVAMENTE!\033[m')

