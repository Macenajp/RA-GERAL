# Questão 8 da lista:

contador = 1
soma = 0

while contador <= 10:
    entradas = int(input("Insira um número: "))
    contador = contador + 1
    soma += entradas

print("Valor total:", soma)
print("Média dos números:", soma / 10)
