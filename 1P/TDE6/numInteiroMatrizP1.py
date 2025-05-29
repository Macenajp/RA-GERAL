# Exercício 4 (A) - TDE6
import random

matriz = [[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]]
for l in range (0,5):
    for c in range (0,5):
        matriz [l] [c] = random.randint(10, 99)
print("-=" * 30)

for l in range (0,5):
    for c in range (0,5):
        print(f"[{matriz [l] [c]:^5}]" , end="")
    print()

print("-=" * 30)
for l in range(0, 5):
    for c in range(0, 5):
        matriz[l][c] = 0

conta = matriz[0][2] = random.randint(10, 99)
conta2 = matriz[1][2] = random.randint(10, 99)
conta3 = matriz[2][0] = random.randint(10, 99)
conta4 = matriz[2][1] = random.randint(10, 99)
conta5 = matriz[2][2] = random.randint(10, 99)
conta6 = matriz[2][3] = random.randint(10, 99)
conta7 = matriz[2][4] = random.randint(10, 99)
conta8 = matriz[3][2] = random.randint(10, 99)
conta9 = matriz[4][2] = random.randint(10, 99)

soma = conta + conta2 + conta3 + conta4 + conta5 + conta6 + conta7 + conta8 + conta9

for l in range(0, 5):
    for c in range(0, 5):
        print(f"[{matriz[l][c]:^5}]", end="")
    print()

print(f"a soma dos itens é de:{soma}")
