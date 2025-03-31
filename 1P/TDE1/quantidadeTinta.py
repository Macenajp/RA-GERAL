altura = float(input("Digite a altura do cilíndro (em metros): "))
raio = float(input("Digite o raio da base do cilíndro (em metros): "))

calculoLateral = 2 * 3.14 * raio * altura
calculaBase = 2 * 3.14 * (raio * raio)
calculoGeral = calculoLateral + calculaBase

calculoMetros = 5 * 3

calculoTotal = calculoGeral / calculoMetros
calculoTinta = calculoTotal * 50

print("Quantidade de latas necessárias:", int(calculoTotal))
print(f"Valor final: R$ {calculoTinta:.2f}")
