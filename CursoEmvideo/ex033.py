a = int(input('Digite um valor: '))
b = int(input('Digite outro valor '))
c = int(input('Digite outro valor: '))
#Verificando o menor número
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
print(f'O menor valor foi o: {menor}')
#Verificando o maior valor
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print(f'O maior valor foi o {maior}')  