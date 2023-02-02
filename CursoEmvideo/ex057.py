print(f"\033[1;33m{'=-'*30}\nDIGITE SUAS INFORMAÇÕES PARA REALIZAR O CADASTRO ONLINE\n{'-='*30}\033[m")
nome = (input('Digite seu 1° nome: ')).upper()
sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]
    if sexo != 'M' and sexo != 'F':
        print('\033[1;31mOPÇÃO INVALIDA!\033[m \nDigite novamente\n')
print(f"\033[1;34mCADASTRO REALIZADO COM SUCESSO\033[m\n{'-'*65}\nOlá {nome} seja bem vindo(a)\npode proseguir e aproveitar as ofertas do club de compras RL\n{'-'*65}")
