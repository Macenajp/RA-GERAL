peso = float(input('Qual o seu peso? '))
altura = float(input('Qual a sua altura? '))

imc = peso / (altura * altura) * 10000

print(f'Seu IMC é: {imc:.2f}')
