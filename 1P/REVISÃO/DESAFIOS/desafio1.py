# Desafio - 29/05

def funcao1(x, y):
    return x + y

def funcao2(x):
    return x * 10

def funcao3(x):
    s = 0
    for i in range(x):
        s += 1
    return funcao1(s, x)

a = 3
b = 2

x = funcao1(a, b)
y = funcao2(funcao3(x))

print(x,y)
