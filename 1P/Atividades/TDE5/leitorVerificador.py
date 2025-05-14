# Questão 3 da lista:
num1 = float(input("Digite o primeiro número como 'base': "))
num2 = float(input("Digite o segundo número que será usado para a soma com o próximo: "))
num3 = float(input("Digite o terceiro número que fará parte da soma: "))

if num1 > (num2 + num3):
    print(f"{num1} é maior que a soma de {num2} e {num3} ({num2 + num3}).")
else:
    print(f"{num1} não é maior que a soma de {num2} e {num3} ({num2 + num3}).")
