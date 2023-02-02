from random import choice
n1 = str(input('Primeira rapariga: '))
n2 = str(input('Segunda rapariga: '))
n3 = str(input('Terceira rapariga: '))
n4 = str(input('Quarta rapariga: '))
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print(f'a rapariga escolhida foi {escolhido}')
