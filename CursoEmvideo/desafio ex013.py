print('\n Simulação de custo sobre compra de produto.')
print(' Caso seja pagto á vista, há um desconto de 10% no valor do produto, e caso o pagto seja por cartão de crédito, a porcentagem do juros é de 8%')
prod = float(input(' Digite o valor do produto: R$'))
print('\n')
print('*' *40)
print(f' Valor do produto: R${prod:.2f}')
print(f' Valor á vista: R${(prod - (prod * 10 / 100)):.2f}')
print(f' Valor no cartão de crédito: R${(prod + (prod * 8 / 100)):.2f}')
print('*' *40)
print('\n')