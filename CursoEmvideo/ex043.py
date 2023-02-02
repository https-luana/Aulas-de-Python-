print('-='*10)
print('Calculadora IMC')
print('=-'*10)
peso = float(input('Qual é o seu peso?(kg) '))
altura = float(input('Qual é a sua altura? (m) '))
imc = peso / (altura ** 2)
print(f'O IMC será de \033[1m{imc:.1f}\033[m')
if imc < 18.5:
    print('\033[35mVocê está abaixo do peso normal\033[m')
elif imc >= 18.5 and imc < 25: #elif <=18.5 imc < 25
    print('\033[34mVocê está no peso ideal!\033[m')
elif 25 <= imc < 30:
    print('\033[33mEstá em sobrepeso!\033[m')  
elif 30 <= imc < 40:
    print('\033[31mAlerta você esta em obesidade!\033[m')
else:
    print('\033[31mCuidado você está em obesidade mórbida!\033[m')    