numero = int(input('Insira um número inteiro:'))
contador = 1
while contador <= numero:
    if contador % 2 != 0:
        print('Número:', contador)
    contador = contador + 1
