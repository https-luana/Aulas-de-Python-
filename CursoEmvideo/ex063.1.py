print('-'*35)
print('Sequencia de fibonacci')
print('-'*35)
n = int(input('Quantos termos você quer mostrar? '))
# 1º termos definidos automaticamente
# começa com 0 e 1. Os números seguintes são sempre a soma dos dois números anteriores.
termo1 = 0 
termo2 = 1
print('~'*35)
print(f'{termo1} → {termo2}', end='')
cont = 3 # vai contar apartir do 3
while cont <= n: #enquanto cont for menor que n execute o bloco abaixo
    termo3 = termo1 + termo2 # termo3 é o termo1 somado com termo2
    print(f' → {termo3}', end ='')
    # transição dos termos para a soma entre os eles
    termo1 = termo2
    termo2 = termo3
    cont += 1 # cont atual sera o anterior mais 1
print('→ Fim')
print('~'*35)