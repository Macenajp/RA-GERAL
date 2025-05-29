# Exercício 5 - TDE6
import random

linhas = 15
colunas = 7
matriz = []

for i in range(linhas):
    linha = []
    for j in range(colunas):
        linha.append(random.randint(10, 99))
    matriz.append(linha)

print("Matriz padrão:")
for linha in matriz:
    for valor in linha:
        print(f"[{valor:^3}]", end=" ")
    print()

todos_numeros = [num for linha in matriz for num in linha]
pares = [n for n in todos_numeros if n % 2 == 0]
impares = [n for n in todos_numeros if n % 2 != 0]
nova_lista = pares + impares

nova_matriz = []
indice = 0
for i in range(linhas):
    linha = []
    for j in range(colunas):
        linha.append(nova_lista[indice])
        indice += 1
    nova_matriz.append(linha)

print("\nMatriz com pares primeiro e ímpares depois:")
for linha in nova_matriz:
    for valor in linha:
        print(f"[{valor:^3}]", end=" ")
    print()
