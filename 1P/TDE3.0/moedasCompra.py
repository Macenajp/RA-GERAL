# Questão 10 da lista:

# Opções de moedas:
dolar = 5.76
euro = 6.19
libra = 7.42

# Escolha da moeda pelo usuário:
moeda = 0
while moeda < 1 or moeda > 3:
    print("Escolha uma dessas moedas para comprar:")
    print("1 - Dólar")
    print("2 - Euro")
    print("3 - Libra")

    moeda = int(input('Qual moeda você quer deseja comprar? '))
    total = float(input('Digite a quantidade desejada: '))

# Resultado final da "compra" das moedas:
if moeda  == 1:
    if total < 1000:
        print(f"O valor final é: {total * dolar * 1.05:.2f}")
    else:
        print(f"O valor final é: {total * dolar * 1.03:.2f}")
elif  moeda  ==  2:
    if total < 1000:
        print(f"O valor final é: {total * euro * 1.05:.2f}")
    else:
        print(f"O valor final é: {total * euro * 1.03:.2f}")
elif moeda  == 3:
    if total < 1000:
        print(f"O valor final é: {total * libra * 1.05:.2f}")
    else:
        print(f"O valor final é: {total * libra * 1.03:.2f}")
