# Questão 3 da list:
numeros = []

# Leitura e armazenamento:
for i in range(3):
    valor = float(input(f"Digite o {i + 1}º número: "))  # Alterado para float para maior flexibilidade
    numeros.append(valor)

produto = numeros[0] * numeros[1]
if numeros[2] > produto:
    print(f"O último valor ({numeros[2]}) é maior que o produto dos dois primeiros ({produto})")
elif numeros[2] < produto:
    print(f"O último valor ({numeros[2]}) não é maior que o produto dos dois primeiros ({produto})")
else:
    print(f"O último valor ({numeros[2]}) é igual ao produto dos dois primeiros ({produto})")
