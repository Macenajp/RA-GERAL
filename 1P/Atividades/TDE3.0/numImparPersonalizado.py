# Questão 5 da lista:
numero = int(input('Insira um número inteiro:'))
contador = 1
while contador <= numero:
    if contador % 2 != 0:
        print(f"Número:, {contador:.2f}")
    contador = contador + 1
