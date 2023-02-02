#cidade = str(input('Em que cidade você nasceu? ')).split()
#print(cidade[:5].upper() == 'RIO')


cid = str(input('Em que cidade você nasceu? ')).lower().strip().split()
print('A sua cidade começa com santos? {}'.format('santos' in cid[0:6]))