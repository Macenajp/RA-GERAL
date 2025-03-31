# Questão 10 da lista:
moeda = int(input("Qual moeda você quer comprar. Dolár (1), Euro (2) ou Libra (3). "))
valor = float(input("Quanto você quer adiquirir? "))

# Moedas:
dolar = valor * 5.74
euro = valor * 6.19
libra = valor * 7.42

# Cálculo da compra:
while moeda >= 1:
    dolar = valor * 5.74
    if dolar <= 1000 * 0.95:
        print("Você receberá:", dolar, ".A empresa ficará com 5% das taxas")
    elif dolar >= 1000 * 0.97:
        print("Você receberá: ", dolar, ".A empresa ficará com 3% das taxas")
