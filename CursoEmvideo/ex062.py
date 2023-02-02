print(f'''{'='*26}
     GERADOR DE PA
{'='*26}''')
primeiro= int(input('Primeiro termo: '))
razão = int(input('Razão: '))
termo = primeiro
cont = 1 # contatdor vale 1
total = 0
mais = 10 # logo no inico ja começar a valer 10
while mais != 0: # primeiro laço inicia enquanto mais for diferente de zero execute
     total = total + mais # o total que vai ser mostrado será 10
     while cont <= 10: # 2° laço , Enquanto cont for menor ou igual a 10 execute print
          print(f'{termo} → ', end='')
     termo += razão  # o termo ira se somar junto com a razao
     cont += 1 # cont ira adionar mais 1 ate chegar em 10/ resultado do cont = 11
     print('PAUSA')
     mais = int(input('quantos termos você deseja mostrar a mais? '))
print('FIM')
print(f'Progressão finalizada com {} termos mostra')