# Questão 10 da lista:
vLido = []
for i in range(10):
    numero = int(input(f"Digite o {i+1}º número inteiro: "))
    vLido.append(numero)

vPares = []
vImpares = []

for num in vLido:
  # Exclui zeros
    if num != 0:
      
        if num % 2 == 0:
            vPares.append(num)
        else:
            vImpares.append(num)
          
print("\nVetor original (vLido):", vLido)
print("Vetor de pares (vPares):", vPares)
print("Vetor de ímpares (vImpares):", vImpares)
