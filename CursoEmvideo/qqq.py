from time import sleep
a1 = float(input('Digite o primeiro termos da P.A: '))
r = float(input('Digite a razão da P.A: '))
c = 0
c2 = 0
print('Os primeiro 10 termos da P.A são: ')
sleep(1)
print(a1)
res = 1
while res != 0:
    while c != 9:
        a1 += r
        c += 1
        sleep(1)
        print(a1)
    sleep(1)
    res = int(input('Deseja mostrar mais quantos termos? [0] para sair. '))
    while c2 != res:
        a1 += r
        c2 += 1
        sleep(1)
        print(a1)
    sleep(1)
    c2 = 0
print('Bye Bye')