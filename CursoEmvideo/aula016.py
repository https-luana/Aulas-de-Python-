'''lanche = 'Hambúrguer','Suco', 'Pizza', 'Pudim', 'Batata frita'''
#print(lanche[1:3])  elemento tres é ignorado
#print(lanche[-2:]) contagem inversa

# lanche[1] = 'Refrigerante' esta errado
#print(len(lanche))

'''
-------------------------------------------
for comida in lanche:
    print(f'eu vou comer{comida}')
-------------------------------------------
for cont in range(0, len(lanche)): # o range ignora o ultimo elemento, ele pode encontrar as posicoes
        print(f'Eu vou comer {lanche[cont]} na posiçao {cont}')
--------------------------------------------
for pos, comida in enumerate (lanche):
    print(f'eu vou comer {comida} na posição {pos}')
print('comi pra caramba!')
------------------------------

lanche = 'Hambúrguer','Suco', 'Pizza', 'Pudim', 'Batata frita'
print(sorted (lanche)) #Reorganiza
-------------------------------
a =(2, 5, 4)
b = (5, 8, 1, 2)
c = b + a # nao é a msm coisa  a + b
print(c)
print(c.index(5,1)) # Em que posiçao o 5 esta

---------------------------

pessoa = ('Gustavo', 39, 'M, '99.88')
del (pessoa) #somente deleta a tupla inteira
print(pessoa)
--------------------------------'''

