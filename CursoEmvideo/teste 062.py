print(f'''{'='*26}
     GERADOR DE UMA PA
{'='*26}''')
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
termo = primeiro
cont = 1
resposta = 10
total = 0
while resposta != 0:
    total = total + resposta # total atual é igual o anterior mais resposta
    while cont <= total: #Enquanto cont for menor ou igual a 10, executa o bloco
        print(f'{termo} ',end='')
        termo += razão
        cont += 1 # adiciona mais 1 no cont
    print(' PAUSA')
    resposta = int(input('Deseja mostrar mais quantos termos? \n[0] para sair.  '))
print(f'\n------Progressão finalizada com {total} termos mostrados------')


#O "total" está começando com valor 10 por causa do "mais" que foi setado anteriormente com esse valor, quando o contador for >(maior) que "total" no caso 10 ele para de executar o segundo while e vai te perguntar quantos numeros mais tu quer ver, esse numero vai ser o novo valor de "mais" só que o total ainda é 10 pq ele não finalizou o primeiro while ainda, então ele vai pegar o novo valor de "mais" por exemplo "5" e somar com o valor antigo de "total" que era 10 como na linha 3,(total  = 10 + 5) totalizando 15, esse é o novo valor de total, e agora novamente ele vai comparar na linha 4 , o "cont" que agora é 11 vai ser comparado com o total que agora é 15 e vai mostrar mais 5 vezes a PA, então voltar para o primeiro while e começar tudo de novo, até o q  "mais" seja igual a 0