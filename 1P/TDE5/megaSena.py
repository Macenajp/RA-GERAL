# Questão 12 da lista:
import random
vetor = [random.sample(range(1,60),6)]
vetor2 =[]
vetor3 = []

valorInvalido = True

for i in range(6):
    a = int(input('Insira a sua aposta -> números de 1 até 60: '))
    vetor2.append(a)
    if a >= 60:
        print("Valor inválido!")
        valorInvalido = False
        

for numero in vetor:
    if numero in vetor2:
        vetor3.append(numero)

print(f'O resultado da mega-sena: {vetor}')
print(f'Sua aposta foi: {vetor2} | Você acertou {len(vetor3)} número(s)!')

