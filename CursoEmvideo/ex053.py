frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
'''inverso = '' '''
inverso = junto[::-1]
'''for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]'''
print(f'O inverso de {junto} é {inverso}')    
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')


'''

1°  split separa a frase entre os espaços delas criando uma lista ' '[1], [2]' '...,  2°   junto = '  '.join  vai junta-las novamente sem espaço entre elas , o for cria uma variável chamada letra  entao inverte ela . se o inverso é a msm coisa que junto( o if vai comparar as duas variáveis inverso e junto e dira se é palíndromo ou não)'''

    