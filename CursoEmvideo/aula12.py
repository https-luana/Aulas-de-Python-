nome = str(input('Qual é o seu nome?'))
if nome == 'Luana': # se
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == "Maria" or nome== 'Paulo': #se nao se 
    print('Seu nome é bem popular no brasil.')  
elif nome in "Ana Cláudia Jéssica Juliana": # se estiver em "nome"
    print('Belo nome feminio')       
else:
    print('Seu nome é bem normal.')
print(f'Tenha um bom dia {nome}!')    