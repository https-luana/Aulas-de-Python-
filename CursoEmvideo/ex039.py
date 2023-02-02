from datetime import date
atual= date.today().year
nasc = int(input('Ano de nascimento: '))
sexo = str(input('Qual o seu sexo?: '))
idade = atual - nasc
print(f'Quem nasceu {nasc} tem {idade} anos em {atual}')
if idade == 18:
    print('Você tem que se alistar imediatamente')
elif idade < 18:
    saldo = 18 - idade
    print(f'Ainda falta {saldo} anos para o alistamento')
    ano = atual + saldo
    print(f'Seu alistamento será em {ano}')
else:
    saldo = idade - 18  
    print(f'Você ja deveria ter se alistado já há {saldo} anos')
    ano = atual -  saldo
    print(f'Seu alistamento foi em {ano}')
