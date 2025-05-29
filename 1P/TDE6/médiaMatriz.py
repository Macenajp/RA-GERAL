# Exercício 1 - TDE6
matriz = []
print("Digite os elementos da matriz 4x4:")

for i in range(4):
    linha = []
    for j in range(4):
        valor = int(input(f"Elemento [{i}][{j}]: "))
        linha.append(valor)
    matriz.append(linha)

maiores = [0, 0, 0, 0]  

for coluna in range(4):
    maior = matriz[0][coluna]  
    for linha in range(1, 4):
        if matriz[linha][coluna] > maior:
            maior = matriz[linha][coluna]
    maiores[coluna] = maior

soma = 0
for valor in maiores:
    soma += valor
media = soma / 4

print("\nMatriz:")
for linha in matriz:
    print(linha)
    
print("\nMaiores de cada coluna:", maiores)
print(f"Média dos maiores: {media:.2f}")
