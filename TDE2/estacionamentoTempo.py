# Questão 8 da lista

tempo = float(input("Quanto tempo você ficou no estacionamento em minutos: "))

tempoFinal = (tempo - 60)% 15
tempoFinal3 = (tempo - 60) // 15

if 0 < tempoFinal < 16:
    tempoFinal2 = int(1)
else:
    tempoFinal2 = 0

Valor = (tempoFinal2 + tempoFinal3) * 1.50 + 8

if tempo <= 60:
    print("O valor a ser pago será de R$8,00")
elif tempo > 60:
    print("O valor pago será de:", Valor)
