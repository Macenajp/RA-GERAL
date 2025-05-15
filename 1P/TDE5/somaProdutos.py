# Questào 3 da lista:
numeros = []

# Lê os três números e armazena na lista
for i in range(3):
    valor = int(input(f"Digite o {i + 1}º número inteiro: "))
    numeros.append(valor)

if numeros[0] > numeros[1] + numeros[2]:
    print(f"O primeiro valor ({numeros[0]}) é maior que a soma dos outros dois ({numeros[1] + numeros[2]})")
elif numeros[0] < numeros[1] + numeros[2]:
    print(f"O primeiro valor ({numeros[0]}) é menor que a soma dos outros dois ({numeros[1] + numeros[2]})")
else:
    print(f"O primeiro valor ({numeros[0]}) é igual que a soma dos outros dois: ({numeros[1] + numeros[2]})")
