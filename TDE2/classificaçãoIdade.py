# Questão 11 da lista:

'''
Tabela de classificação das categorias:

Classificação de idade      Categoria
5 até 7 anos                Infantil A
8 até 10 anos               Infantil B
11 até 13 anos              Juvenil A
14 até 17 anos              Juvenil B
Maiores de 18 anos          Adulto
'''

idade = int(input("Insira a sua idade: "))

if idade >= 5 and idade <= 7:
    categoria = 'Infantil A'

elif idade >= 8 and idade <= 10:
    categoria = 'Infantil B'

elif idade >= 11 and idade <= 13:
    categoria = 'Juvenil A'

elif idade >= 14 and idade <= 17:
    categoria = 'Juvenil B'

elif idade >= 18:
    categoria = 'Adulto'

print("Sua categoria é", categoria)
