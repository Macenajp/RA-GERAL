distanciaPercorrida  = float(input("Digite a distância percorrida: "))
combustivelGasto = float(input("Quanto combustível foi gasto? "))

consumoMedio = distanciaPercorrida / combustivelGasto
print(f"O consumo médio do veículo foi de: {consumoMedio:.2f}km/l")
