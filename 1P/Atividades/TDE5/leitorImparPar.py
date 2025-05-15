# Questão 6 da lista:
# Armazena os números:
vetor1=[]

# Impar:
vetor2=[]

# Par:
vetor3=[]

for i in range(4):
    numero = int(input(f"Digite o {i+1}º número inteiro: "))
    vetor1.append(numero)

for numero in vetor1:
    if numero % 2 == 0:
        vetor2.append(numero)
    if numero % 2 != 0:
        vetor3.append(numero)
soma2 = sum(vetor2)

print(f'Os numeros escolhidos foram: {vetor1}')
print(f'Os numeros pares são: {vetor2} ,e a soma deles resulta em: {soma2}')
print(f'Os numeros impares são: {vetor3}')
