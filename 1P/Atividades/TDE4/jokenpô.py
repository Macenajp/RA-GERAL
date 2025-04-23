# TDE4 - Raciocínio Algorítmico
# Github: https://github.com/Macenajp

# Biblioteca:
import random

# Entrada e dados:
print("Regras do jogo: Pedra ganha da tesoura / Tesoura ganha do papel / Papel ganha da pedra")
inicioDoJogo = input("Gostaria de iniciar o jogo (s/n)?: ")

# Gameplay geral:
jogadas = {1: "Pedra", 2: "Papel", 3: "Tesoura"}
if inicioDoJogo == "s":
    print("1 - Humano x Humano")
    print("2 - Humano x Bot")
    print("3 - Bot x Bot")
else:
    print("Volte logo!")
    exit()

# Gameplay: Player x Player:
jogadaContinuar = int(input("Qual será o modo de jogo? "))
if jogadaContinuar == 1:
    print("Modalidade selecionada: Humano x Humano")

    placarHumano1 = 0
    placarHumano2 = 0

    while True:
        jogadaHumano1 = int(input("Pedra - 1, Papel - 2 e Tesoura - 3 \nSelecione sua jogada (Humano 1): "))
        jogadaHumano2 = int(input("Selecione sua jogada (Humano 2): "))

        if jogadaHumano1 == 1 and jogadaHumano2 == 2:
            print("Humano 2 venceu!")
            placarHumano2 += 1
        elif jogadaHumano1 == 1 and jogadaHumano2 == 3:
            print("Humano 1 venceu!")
            placarHumano1 += 1
        elif jogadaHumano1 == 2 and jogadaHumano2 == 1:
            print("Humano 1 venceu!")
            placarHumano1 += 1
        elif jogadaHumano1 == 2 and jogadaHumano2 == 3:
            print("Humano 2 venceu!")
            placarHumano2 += 1
        elif jogadaHumano1 == 3 and jogadaHumano2 == 1:
            print("Humano 2 venceu!")
            placarHumano2 += 1
        elif jogadaHumano1 == 3 and jogadaHumano2 == 2:
            print("Humano 1 venceu!")
            placarHumano1 += 1
        else:
            print("Empate!")

        opcao = input("Deseja continuar? (s/n): ")
        if opcao.lower() != "s":
            print("Placar final:")
            print(f"Humano 1 = {placarHumano1} pontos")
            print(f"Humano 2 = {placarHumano2} pontos")
            break

# Gameplay: Player x Bot:
elif jogadaContinuar == 2:
    print("Modalidade selecionada: Humano x Bot")

    placarHumano = 0
    placarBot = 0

    while True:
        jogadaHumano = int(input("Pedra - 1, Papel - 2 e Tesoura - 3 \nSelecione sua jogada: "))
        jogadaBot = random.randint(1, 3)
        print("Bot escolheu:", jogadas[jogadaBot])

        if jogadaHumano == 1 and jogadaBot == 2:
            print("Bot venceu!")
            placarBot += 1
        elif jogadaHumano == 1 and jogadaBot == 3:
            print("Humano venceu!")
            placarHumano += 1
        elif jogadaHumano == 2 and jogadaBot == 1:
            print("Humano venceu!")
            placarHumano += 1
        elif jogadaHumano == 2 and jogadaBot == 3:
            print("Bot venceu!")
            placarBot += 1
        elif jogadaHumano == 3 and jogadaBot == 1:
            print("Bot venceu!")
            placarBot += 1
        elif jogadaHumano == 3 and jogadaBot == 2:
            print("Humano venceu!")
            placarHumano += 1
        else:
            print("Empate!")

        opcao = input("Deseja continuar? (s/n): ")
        if opcao.lower() != "s":
            print("Placar final:")
            print(f"Humano = {placarHumano} pontos")
            print(f"Bot = {placarBot} pontos")
            break

# Gameplay: Bot x Bot:
elif jogadaContinuar == 3:
    print("Modalidade selecionada: Bot x Bot")
    print("Pedra - 1, Papel - 2 e Tesoura - 3.")

    placarBot1 = 0
    placarBot2 = 0

    while True:
        jogadaBot1 = random.randint(1, 3)
        jogadaBot2 = random.randint(1, 3)
        print("Bot 1 escolheu:", jogadas[jogadaBot1])
        print("Bot 2 escolheu:", jogadas[jogadaBot2])

        if jogadaBot1 == 1 and jogadaBot2 == 2:
            print("Bot 2 venceu!")
            placarBot2 += 1
        elif jogadaBot1 == 1 and jogadaBot2 == 3:
            print("Bot 1 venceu!")
            placarBot1 += 1
        elif jogadaBot1 == 2 and jogadaBot2 == 1:
            print("Bot 1 venceu!")
            placarBot1 += 1
        elif jogadaBot1 == 2 and jogadaBot2 == 3:
            print("Bot 2 venceu!")
            placarBot2 += 1
        elif jogadaBot1 == 3 and jogadaBot2 == 1:
            print("Bot 2 venceu!")
            placarBot2 += 1
        elif jogadaBot1 == 3 and jogadaBot2 == 2:
            print("Bot 1 venceu!")
            placarBot1 += 1
        else:
            print("Empate!")

        # Finalização do jogo:
        opcao = input("Deseja continuar? (s/n): ")
        if opcao.lower() != "s":
            print("Placar final:")
            print(f"Bot 1 = {placarBot1} pontos")
            print(f"Bot 2 = {placarBot2} pontos")
            break
else:
    print("Opção inválida!")
