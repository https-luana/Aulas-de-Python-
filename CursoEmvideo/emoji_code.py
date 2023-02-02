import emoji
print(emoji.emojize('Python é :thumbs_up:'))
print(emoji.demojize('Python é👍'))
if emoji.is_emoji('👍'):
    print('É um emoji')
print(emoji.emojize('Python é :polegar_para_cima:', language='pt'))    
print(emoji.demojize('Python é 👍', language='pt'))