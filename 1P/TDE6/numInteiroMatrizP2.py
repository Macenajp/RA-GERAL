# Exercício 4 (B) - TDE6
import random

matriz = [[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]]
for l in range (0,5):
    for c in range (0,5):
        matriz [l] [c] = random.randint(10, 99)
print("-=" * 30)

for l in range (0,5):
    for c in range (0,5):
        print(f"[{matriz [l][c]:^5}]" , end="")
    print()

print("-=" * 30)
for l in range(0, 5):
    for c in range(0, 5):
        matriz[l][c] = 0

conta = matriz[0][0] = random.randint(10, 99)
conta2 = matriz[0][1] = random.randint(10, 99)
conta3 = matriz[0][2] = random.randint(10, 99)
conta4 = matriz[0][3] = random.randint(10, 99)
conta5 = matriz[0][4] = random.randint(10, 99)

conta6 = matriz[1][0] = random.randint(10, 99)
conta7 = matriz[1][4] = random.randint(10, 99)
conta8 = matriz[2][0] = random.randint(10, 99)
conta9 = matriz[2][4] = random.randint(10, 99)
conta10 = matriz[3][0] = random.randint(10, 99)
conta11 = matriz[3][4] = random.randint(10, 99)

conta12 = matriz[4][0] = random.randint(10, 99)
conta13 = matriz[4][1] = random.randint(10, 99)
conta14 = matriz[4][2] = random.randint(10, 99)
conta15 = matriz[4][3] = random.randint(10, 99)
conta16 = matriz[4][4] = random.randint(10, 99)

soma = conta + conta2 + conta3 + conta4 + conta5 + conta6 + conta7 + conta8 + conta9 + conta10 + conta11 + conta12 + conta13 + conta14 + conta15 + conta16

for l in range (0,5):
    for c in range (0,5):
        print(f"[{matriz [l][c]:^5}]" , end="")
    print()

print(f"a soma dos itens é de:{soma}")
