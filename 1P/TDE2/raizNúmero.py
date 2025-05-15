# Questão 3 da lista:
numero = int(input("Digite um número inteiro: "))

if numero < 0:
    print("Valor inválido")
else:
    raiz = numero ** 0.5
    print("A raiz quadrada de", numero, "é", round(raiz, 2))
