# Exercício 7 - TDE6
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

roteiro = []
while True:
    C = int(input('Infome a cidade  (caso deseje saiu/acabar o programa digite -1.)'))
    if C == -1: break
    roteiro.append(C)

# Mostrar roteiro
print("Roteiro:")
total = 0
for z in range(len(roteiro)-1):
    a, b = roteiro[z], roteiro[z+1]
    d = matriz[a][b]
    print(f"{cidades[a]} -> {cidades[b]}: {d} km")
    total += d

print(f"Distância total: {total} km")
