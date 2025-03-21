# Questão 10 da lista

'''
Tabela de IMC em adultos:

Condição            IMC em adultos
Abaixo do peso      abaixo de 18,5
No peso normal      entre 18,5 e 25
Acima do peso       entre 25 e 30
Obeso               acima de 30
'''

peso = int(input("Insira seu peso: "))
altura = float(input("Coloque sua altura (em metros) "))

imc = peso / (altura * altura)

if imc < 18.5:
    condição = 'Abaixo do peso'
elif imc >= 18.5 and peso < 25:
    condição = 'No peso normal'
elif imc >= 25 and peso < 30:
    condição = 'Acima do peso'
else:
    condição = 'Obeso'


print(f"Seu IMC é: {imc:.2f}, e sua condição está:", condição)
