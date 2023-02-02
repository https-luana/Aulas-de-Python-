print('-'*25)
print('\033[1;36mVERFIFICADOR DE VALORES\033[m')
print('-'*25)
numero = soma = contador =0
while True:
    numero = int(input('Digite um valor \033[1m[999 para sair]\033[m:'))
    if numero == 999:
        break
    soma += numero
    contador += 1
print('-'*35)
print(f'Você digitou {contador} números e sua soma vale {soma}')