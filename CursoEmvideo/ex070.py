total = totmil = menor = cont = 0
barato = ' '
print (f'{("LOJÃO DO BARATÃO"):-^40}')
while True:
    produto = input('Nome do produto: ')
    preço = float(input('Preço: R$ '))
    cont += 1
    total += preço
    if preço > 1000:
        totmil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = input('Quer continuar? [S/N] ').strip().upper()[0]
        print('-'*25)
    if resp == 'N':
        break
print (f'{("fim do programa"):-^40}')
print(f'O total da compra foi {total:.2f}')
print(f'Temos {totmil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} custando R${menor:.2f}')