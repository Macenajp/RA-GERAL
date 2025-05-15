#Questão 8 da lista:
vetor = []

for i in range(10):
    a = int(input('Insira um número: '))
    vetor.append(a)
    
print(f'O valor maximo escolhido foi: {max(vetor)}')
print(f'O valor mais baixo escolhido foi: {min(vetor)}')
print(f'A amplitude amostral: {max(vetor) - min(vetor)}')
