# Questào 7 da lista:
numeros = []

a = int(input('Insira um número: '))

for i in range(a):
    multiplação = i * (i + 1) * (i + 2)
    numeros.append(multiplação)
    if multiplação == a:
        print('Este némero é triangular')
        break
else:
    print('Este número não é triangular')
