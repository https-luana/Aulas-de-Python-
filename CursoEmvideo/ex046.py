from time import sleep
import emoji
print(f'\033[1;36m{"="*10} Contagem regressiva 2022 {"="*10}\033[m')
for c in range(10, -1, -1):
   print(c)
   sleep(1)
print(emoji.emojize('FELIZ ANO NOVO!🎉💖'))    