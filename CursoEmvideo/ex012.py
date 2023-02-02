preço = float(input('Qual é o preço do produto? R$'))
novo = preço - (preço * 5 /100)
print(f'O produto que custa R${preço:.2f}, na promoção com desconto de 5% vai custar R${novo:.2f}')