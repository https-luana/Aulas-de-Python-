qtd = int(input('Quantidade de alunos? '))
i = 1 #variavel de contagem
somaI = 0
while i < qtd:
    idade = int(input(f'Informe a idade do aluno {i}º: '))
    somaI = somaI + idade
    i += 1 #o i anterior recebe 2 com mais um vale 3
mediaI = somaI / qtd
print(f'Média das idades é {mediaI:.2f}')


'''i = 1
while i < 11:
    i = i + 1'''