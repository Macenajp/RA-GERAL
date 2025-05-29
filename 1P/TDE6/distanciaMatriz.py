#Exercício 6 - TDE6
matriz= [(0,310,716,408,852),
         (310,0,470,705,1144),
         (716,470,0,1119,1553),
         (408,705,1119,0,429),
         (852,1144,1553,429,0)]

indice = 0
cidades = ['Curitiba','Florianópolis','Porto Alegre','São Paulo','Rio de Janeiro']

for cidade in cidades:
    print(indice,cidade)
    indice += 1
print('-=' * 30)
