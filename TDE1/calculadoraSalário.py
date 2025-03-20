salarioMinimo = 1509.00
salarioDoProfissional = float(input("Digite o salário: "))

salarioAnual = salarioDoProfissional * 12
quantidadeDeSalarios = salarioAnual / 1509

print(f"O profissional recebe {quantidadeDeSalarios:.2f} salários mínimos")
