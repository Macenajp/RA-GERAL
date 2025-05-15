def main():
    print("Digite os elementos da matriz 4x4:")
    matriz = [[int(input(f"Elemento [{i}][{j}]: ")) for j in range(4)] for i in range(4)]

    maiores = [max(coluna) for coluna in zip(*matriz)]

    media = sum(maiores) / 4     # Calcula a média

    print("\nMatriz:")
    for linha in matriz:
        print(*linha, sep='\t')

    print("\nMaiores de cada coluna:", *maiores)
    print(f"Média: {media:.2f}")

if __name__ == "__main__":
    main()
