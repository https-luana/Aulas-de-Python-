print(f'''{'='*19}
CADASTRO DE PESSOAS
{'='*19}''')
maior = homens = mulher20 = 0
sexo = continuar = ' '
while True:
    print("-"*20)
    idade = int(input("Informa a idade: "))
    while sexo not in 'MF':
       sexo = str(input("Informe o sexo [M/F]: ")).upper().strip()
       if idade > 18:
         maior = maior + 1
       if sexo == "M":
         homens = homens + 1
       if sexo == "F" and idade < 20:
         mulher20 = mulher20 + 1
    sexo = continuar = ' '
    while continuar not in 'SN':
       continuar = str(input("CONTINUAR [S/N]")).upper().strip()
    if continuar == "N":
       break
print(f'''MULHERES COM MENOS DE 20 ANOS SÃO {mulher20}
      \nTOTAL DE HOMENS SÃO {homens}
      \nMAIORES DE 18 ANOS SÃO {maior}''')