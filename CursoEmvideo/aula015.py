'''n = s = 0
while n != 999: #utilização de flags
    n = int(input('Digite um número:'))
    s += n
s -= 999
print(f'A soma vale {s}')'''


n = s = 0
while True:
    n = int(input('Digite um número:'))
    if n == 999:
        break # se nao for igual 999 ele soma ,se for 999 sai de um enquanto e quebra(finalizando)
    s += n
print(f'A soma vale {s}')