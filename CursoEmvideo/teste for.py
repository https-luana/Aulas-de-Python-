from datetime import date
d = str(date.today()).split('-')
menor = 0
maior = 0
print('Para saber se tem maior idade digite o ano de nascimento')
for i in range(0, 7):
    a = int(input('Digite o ano: '))
    b = int(input('Digite o mês: '))
    c = int(input('Digite o dia: '))
    if int(d[0])-18 < a:
        menor += 1
        print('Menor de idade')
    elif int(d[0])-18 == a and int(d[1]) == b and int(d[2]) == c:
        maior += 1
        print('Maior de idade')
    elif int(d[0])-18 == a and int(d[1]) < b:
        menor += 1
        print('Menor de idade')
    elif int(d[0]) - 18 == a and int(d[1]) == b and int(d[2]) < c:
        menor += 1
        print('Menor de idade')
    else:
        maior += 1
        print('Maior de idade')
print('{} Desses é maior de idade e {} destes é menor de idade.'.format(maior, menor))