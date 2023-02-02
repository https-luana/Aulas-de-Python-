from math import radians, sin, cos, tan 
ângulo = float(input('Digite um ângulo que você deseja:'))
seno = sin(radians(ângulo))
print(f'O ângulo {ângulo} tem o SENO de {seno:.2f}')
cosseno = cos(radians(ângulo))
print(f'O ângulo de {ângulo} tem o COSSENO de {cosseno:.2f}')
tangente = tan(radians(ângulo))
print(f'O ângulo de {ângulo} tem a TANGENTE de {tangente:.2f}')