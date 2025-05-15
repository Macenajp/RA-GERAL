 # Questão 13 da lista:
preco = float(input("Digite o preço do produto: "))

print("Essas são :")
print("1 - À vista (8% de desconto)")
print("2 - Em 2 parcelas (4% de desconto)")
print("3 - Em 3 parcelas (sem desconto)")
print("4 - Em 4 parcelas (4% de acréscimo)")

opcao = int(input("Escolha a opção de pagamento (1 a 4): "))

if opcao == 1:
    valor_final = preco * 0.92
    print(f"Valor a ser pago à vista com 8% de desconto: R${valor_final:.2f}")
elif opcao == 2:
    valor_final = preco * 0.96
    print(f"Valor total com 4% de desconto, dividido em 2x de R${valor_final / 2:.2f}")
elif opcao == 3:
    print(f"Valor total sem desconto, dividido em 3x de R${preco / 3:.2f}")
elif opcao == 4:
    valor_final = preco * 1.04
    print(f"Valor total com 4% de acréscimo, dividido em 4x de R${valor_final / 4:.2f}")
else:
    print("Opção inválida!")
