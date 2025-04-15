numero1 = int(input("Insira um número: "))
numero2 = int(input("Insira um número: "))
numero3 = int(input("Insira um número: "))

if numero1 < numero2 and numero1 < numero3:
    print(numero1, "é o primeiro da sequencia")
elif numero1 > numero2 and numero1 > numero3:
    print(numero1, "é o último número da sequencia")
else:
    print(numero1, "é o segundo número da sequencia")

###########################################################

if numero2 < numero1 and numero2 < numero3:
     print(numero2, "é o primeiro da sequencia")
elif numero2 > numero1 and numero2 > numero3:
     print(numero2, "é o último número da sequencia")
else:
     print(numero2, "é o segundo número da sequencia")

###########################################################

if numero3 < numero1 and numero3 < numero2:
    print(numero3, "é o primeiro da sequencia")
elif numero3 > numero1 and numero3 > numero2:
     print(numero3, "é o último número da sequencia")
else:
     print(numero3, "é o segundo número da sequencia")
