# Questão 2 da lista:
for i in range(1, 101):
    multiplicando = (i - 1) // 10 + 1
    multiplicador = (i - 1) % 10 + 1
    print(f"{multiplicando} x {multiplicador} = {multiplicando * multiplicador}")
