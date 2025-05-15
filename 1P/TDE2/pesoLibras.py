# Questão 12 da lista:
peso = float(input("Qual seu peso em quilograma? "))

libras = peso * 2.20

if libras >= 201:
    print("A sua categoria é Peso-Pesado.")
elif libras >= 176:
    print("A sua categoria é Cruzador.")
elif libras >= 169:
    print("A sua categoria é Meio-pesado.")
elif libras >= 161:
    print("A sua categoria é Super-médio.")
else:
    print("A sua categoria é inferior a Super-médio.")
