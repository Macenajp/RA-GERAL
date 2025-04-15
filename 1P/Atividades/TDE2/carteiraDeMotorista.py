# Questão 2 da lista:

anoDeNascimento = int(input("Coloque o ano do seu nascimento: "))
idade = 2023 - anoDeNascimento

if idade <= 18:
    print("Você ainda não completou a idade indicada para poder tirar a carteira de motorista!")
elif idade >= 18:
    print("Você já alcançou a idade adequada para tirar a carteira de motorista!")
