'''
a tabela abaixo:

Categoria           Peso
Palha               Menor que 50kg
Pluma               50 - 59.99
Leve                60 - 75.99
Pesado              76 - 87.99
Super Pesado        Maior que 88
'''

peso = float(input("Entre com o peso do boxeador: "))
if peso < 50:
    categoria = 'Palha'
elif peso >= 50 and peso < 60:
    categoria = 'Pluma'
elif peso >= 60 and peso < 76:
    categoria = 'Leve'
elif peso >= 76 and peso < 88:
    categoria = 'Pesado'
else:
    categoria = 'Super Pesado'

print("A categoria é de", categoria)
