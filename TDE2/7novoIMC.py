# Questão 7 da lista:
massa = float(input("Coloque sua massa em quilogramas: "))
altura = float(input("Coloque sua altura em metros: "))

imc = massa / (altura ** 2)
print("Seu IMC é:", imc)

if imc >= 18.5 and imc < 25:
    print("Seu IMC está na faixa normal.")
else:
    massa_maxima = 24.9 * (altura ** 2)
    print("Seu IMC está fora da faixa normal.")
    print("Sua massa máxima considerada normal é:", massa_maxima, "kg")
