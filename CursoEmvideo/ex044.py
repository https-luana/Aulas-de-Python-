print('\n\033[31m========== AMERICANAS ==========\033[m')
print('\033[1mtire suas dúvidas sobre os meios de pagamento a seguir\033[m')
print('')
preço = float(input('Qual o valor das compras? '))
print('''\033[31mFORMAS DE PAGAMENTO
[1] á vista dinheiro/debito
[2] á vista cartão de credito
[3] 2x no cartão de credito
[4] 3x ou mais no cartão de credito\033[m''')
opção = int(input('\033[1mEscolha qual forma deseja pagar\033[m '))
if opção == 1:
    total = preço - (preço * 10 /100)
elif opção == 2:
    total = preço - (preço * 5 /100)
elif opção == 3:
    total = preço
    parcela = total/2
    print(f'sua compra será parcela em 2x de R${parcela:.2f} ')
elif opção == 4:
    total = preço + (preço * 20/100)
    totalparc = int(input('Quantas parcelas? '))
    parcela = total / totalparc
    print(f'sua compra será parcelada em {totalparc}x de R$ {parcela:.2f} com juros!') 
else:
    total = preço
    print('\033[1;31m OPÇÃO INVÁLIDA DE PAGAMENTO TENTE NOVAMENTE\033[m')
print(f'Sua compra de R${preço:.2f} vai custar R${total:.2f} no final ')

   
