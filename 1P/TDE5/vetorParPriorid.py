# Questão 11 da lista:
vetor = []

for i in range(10):
    a = int(input('Insira um número: '))
    vetor.append(a)
    if a < 1:
        print('Esse valor é inválido/incorreto!')
        break

pares = []
impares = []

for numero in vetor:
    if numero % 2 == 0:
        pares.append(numero)
    if numero % 2 != 0:
        impares.append(numero)
vetor2 = pares + impares

print(f'V2'
      f'etor modificado (pares primeiro): {vetor2}')
