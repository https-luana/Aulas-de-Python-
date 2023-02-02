velocidade = float(input('Qual é a velocidade atual do carro? '))
if velocidade >80:
    print('Multado! você excedeu o limite permitido que é de 80km/h')
    multa = (velocidade -80) * 7
    print(f'Você deve pagar uma multa de R${multa:.2f}')
print('Tenha um bom dia! dirija com segurança!')