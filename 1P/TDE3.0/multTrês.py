# Questão 9 da lista:

li = float(input("Insira um limite incical: "))
lf = float(input("Insira um limite final: "))

inicioLi = li + 1 if (li + 1) % 3 != 0 else li + 1
contador = inicioLi

while contador < lf:
    if contador % 3 == 0:
        print("Número:", contador)
    contador += 1
