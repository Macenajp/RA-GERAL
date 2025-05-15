# Questão 13 da lista:
vetor = []

for i in range(20):
    a = int(input("Insira um número: "))
    vetor.append(a)
posicoes = len(vetor)

for i in range(posicoes - 1):
    menor = i
    for a in range(i + 1, posicoes):
        if vetor[a] < vetor[menor]:
            menor = a
    vetor[i], vetor[menor] = vetor[menor], vetor[i]

print("Vetor ordenado:", vetor)
