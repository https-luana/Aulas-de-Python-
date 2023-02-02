n1 = 1
n2 = 0
c = 1
print('-' * 22)
print('Sequência de Fibonacci')
print('-' * 22)
q = int(input('Quantos termos você quer mostrar? '))
print('0 -> ', end='')
while c != q:
    print('{} -> '.format(n1), end='')
    n2 = n1 + n2
    c += 1
    if c != q:
        print('{} -> '.format(n2), end='')
        c += 1
        n1 = n1 + n2
print('FIM')