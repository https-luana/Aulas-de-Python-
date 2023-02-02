número = int(input('Me diga um número qualquer: '))
resultado = número %2
if resultado == 0:
    print(f'O número {número} é PAR')
else:
    print(f'O número {número} é ÍMPAR')