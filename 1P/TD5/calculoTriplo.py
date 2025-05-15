# Questões 4 e 5 da lista:
vetor = []

# Armazena e lê:
for i in range(2):
    a = float(input('Insira um número: '))
    vetor.append(a)

print(f'A soma dos valores totaliza: {sum(vetor)} ')
print(f'O produto dos valores é: {vetor[0] * vetor[1]} ')
print(f'A divisão dos valores resulta em: {vetor[0] / vetor[1]} ')
