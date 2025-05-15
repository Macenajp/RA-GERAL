# Questão 9 da lista

idade = int(input("Qual é sua idade? "))

if idade < 16:
    print("Não votante")
elif 18 <= idade <= 65:
    print("Você é eleitor obrigatorio")
else:
    print("Você é eleitor facultativo")
