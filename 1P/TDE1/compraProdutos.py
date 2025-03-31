valorProduto = float(input("Valor: "))

valorAVista = valorProduto * 0.95
valor2Parcelas = valorProduto / 2
valor3Parcelas = (valorProduto / 3) / 0.95

print(f"O valor do produto é de: R$ {valorProduto:.2f}, já à vista, sai por R$ {valorAVista:.2f}, e parcelado em duas vezes fica R$ {valor2Parcelas:.2f} cada parcela, e a última forma de pagamento seria com três parcelas e mais um acréscimo de 5%, ficando: R$ {valor3Parcelas:.2f}")
