# Exercício 2 - TDE6
matriz = [[0,0,0,0], [0,0,0,0], [0,0,0,0]]
for l in range (0,3):
    for c in range (0,3):
        matriz [l] [c] = int(input(f"digite uma valor para [{l}, {c}]: "))
print("-=" * 30)
print("está é a matriz base")
for l in range (0,3):
    for c in range (0,3):
        print(f"[{matriz [l] [c]}]" , end="")
    print()

print("-=" * 30)
multiplicação = int(input("Escolha um numero que ira multiplicar toda matriz"))
print("-=" * 30)

print("Matriz multiplicada")
for LM in range (0,3):
    for CM in range (0,3):
        print(f"[{matriz [LM][CM]*multiplicação:^5}]" , end="")
    print()
