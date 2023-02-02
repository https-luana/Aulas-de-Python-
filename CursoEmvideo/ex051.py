print(f'''{'='*26}
    10 TERMOS DE UMA PA
{'='*26}''')
primeiro= int(input('Primeiro termo: '))
razão = int(input('Razão: '))
décimo = primeiro + (10 - 1) * razão
for c in range(primeiro, décimo + razão, razão):
    print(f'{c}', end='→')
print('ACABOU')

#p1 = int(input('Primeiro termo: '))
#rz = int(input('Razão: '))
#for c in range(0, 10,):
#   print('{}'.format(p1 + rz * c))