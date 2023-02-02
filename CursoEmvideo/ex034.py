salário = float(input('Qual o salario do funcionario? R$'))
if salário <= 1250:
    novo = salário + (salário * 15 / 100)
else:
    novo = salário + (salário * 10 / 100)
print(f'Quem ganhava R${salário:.2f} passa a ganhar R${novo:.2f}')
