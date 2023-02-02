print(f'''{'='*26}
     GERADOR DE UMA PA
{'='*26}''')
primeiro= int(input('Primeiro termo: '))
razão = int(input('Razão: '))
termo = primeiro
cont = 1
while cont <= 10: #Enquanto cont for menor ou igual a 10 execute print
    print(f'{termo} → ', end='')
    termo += razão  # o termo ira se somar junto com a razao
    cont += 1 # cont ira adionar mais 1 ate chegar em 10
print('\n\n------Fim da contagem------')