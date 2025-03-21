# Questão 5 da lista:

cópias = int(input("Insira quantas cópias você gostaria de tirar: "))

valor1 = cópias * 0.25
valor2 = cópias * 0.20

if cópias <= 100:
    print("O valor de cada cópia será de R$0,25. O total vai ser: R$", valor1)
else:
    print("O valor de cada cópia será de R$0,20. O total vai ser: R$", valor2)
