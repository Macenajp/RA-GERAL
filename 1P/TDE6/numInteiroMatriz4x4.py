# Exercício 3 - TDE6
import random

numeros_unicos = random.sample(range(100, 1000), 16)
matriz = []
indice = 0
for l in range(4):
    linha = []
    for c in range(4):
        linha.append(numeros_unicos[indice])
        indice += 1
    matriz.append(linha)

for l in range(4):
    for c in range(4):
        print(f"[{matriz[l][c]:^5}]", end=" ")
    print()

maior_valor = -1
linha_do_maior = -1

for i in range(4):
    for j in range(4):
        if matriz[i][j] > maior_valor:
            maior_valor = matriz[i][j]
            linha_maior = i
            coluna_maior = j

menor_na_linha = min(matriz[linha_maior])

print("-=" * 30)
print(f"Maior valor da matriz: {maior_valor}")
print(f"Posição do maior valor: Linha {linha_maior + 1}, Coluna {coluna_maior + 1}")
print(f"Menor valor da mesma linha: {menor_na_linha}")
