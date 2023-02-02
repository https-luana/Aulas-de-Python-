times = ('Palmeiras', 'Flamengo', 'Corinthians', 'Fluminense', 'Athletico-PR', 'Internacional',
        'Atlético-MG', 'Santos', 'São Paulo', 'Botafogo', 'América-MG', 'ragantino', 'Goiás', 'Ceará', 'Fortaleza', 'Cuiabá', 'Avaí', 'Coritiba', 'Atlético-GO', 'Juventude')   
cont = 1
print('-='*15)
print('Tabela Brasileirao')
for t in times:
    print(f'{cont}º - {t}')
    cont += 1
print('-='*15)
print(f'Os 5 primeiros são {times[0:5]}')
print(f'Os quatro ultimos são {times[-4:]}')
print('-='*15)
print(f'Times em ordem alfabetica: {sorted(times)}')
print(f'O flamengo está na {times.index("Flamengo")+1}ª posiçao')
