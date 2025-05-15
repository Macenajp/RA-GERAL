# Jokenpô - Entrega geral do grupo:
# Biblioteca:
import random

# Entrada geral:
entrada = int(input('Escolha um modo de jogo humano x humano(1), humano x computador (2), computador x computador (3): '))
continuar = True
placarJ1 = 0
placarJ2 = 0
placarE = 0
entradageral = entrada

# Gameplay geral:
while continuar:

    if entradageral:
        if entrada == 1:
            escolha1 = int(input('JOGADOR 1: escolha entre pedra (1), papel (2) ou tesoura (3): '))
            escolha2 = int(input('JOGADOR 2: escolha entre pedra (1), papel (2) ou tesoura (3): '))
        if entrada == 2:
            escolha1 = int(input('JOGADOR 1: escolha entre pedra (1), papel (2) ou tesoura (3): '))
            escolha2 = random.randint(1, 3)
        if entrada == 3:
            escolha1 = random.randint(1, 3)
            escolha2 = random.randint(1, 3)

    # Jogador 1 (bot) - Pedra:
    if escolha1 == 1 and escolha2 == 2:
        print('-----------------------------------------------------------------------------------------------------------------')
        print('Jogador 1 escolheu pedra e o jogador 2 escolheu papel.')
        print('Vitória do jogador 2!')
        print('-----------------------------------------------------------------------------------------------------------------')
        placarJ2 = placarJ2 + 1

    if escolha1 == 1 and escolha2 == 3:
        print('-----------------------------------------------------------------------------------------------------------------')
        print('Jogador 1 escolheu pedra e o jogador 2 escolheu tesoura.')
        print('Vitória do jogador 1')
        print('-----------------------------------------------------------------------------------------------------------------')
        placarJ1 = placarJ1 + 1

    if escolha1 == 1 and escolha2 == 1:
        print('-----------------------------------------------------------------------------------------------------------------')
        print('Jogador 1 escolheu pedra e o jogador 2 escolheu pedra.')
        print('Empate!')
        print('-----------------------------------------------------------------------------------------------------------------')
        placarE = placarE + 1

    # Jogador 1 (bot) - Papel:
    if escolha1 == 2 and escolha2 == 1:
        print('-----------------------------------------------------------------------------------------------------------------')
        print('Jogador 1 escolheu papel e o jogador 2 escolheu pedra.')
        print('Vitória do jogador 1')
        print('-----------------------------------------------------------------------------------------------------------------')
        placarJ1 += 1

    if escolha1 == 2 and escolha2 == 2:
        print('-----------------------------------------------------------------------------------------------------------------')
        print('Jogador 1 escolheu papel e o jogador 2 escolheu papel.')
        print('Empate!')
        print('-----------------------------------------------------------------------------------------------------------------')
        placarE += 1

    if escolha1 == 2 and escolha2 == 3:
        print('-----------------------------------------------------------------------------------------------------------------')
        print('Jogador 1 escolheu papel e o jogador 2 escolheu tesoura')
        print('Vitória do jogador 2!')
        print('-----------------------------------------------------------------------------------------------------------------')
        placarJ2 += 1

    # Jogador 1 (bot) - Tesoura:
    if escolha1 == 3 and escolha2 == 1:
        print('-----------------------------------------------------------------------------------------------------------------')
        print('Jogador 1 escolheu tesoura e o jogador 2 escolheu pedra')
        print('Vitória do jogador 2!')
        print('-----------------------------------------------------------------------------------------------------------------')
        placarJ2 += 1

    if escolha1 == 3 and escolha2 == 2:
        print('-----------------------------------------------------------------------------------------------------------------')
        print('Jogador 1 escolheu tesoura, e o jogador 2 escolheu papel')
        print('Vitória do jogador 1!')
        print('-----------------------------------------------------------------------------------------------------------------')
        placarJ1 += 1

    if escolha1 == 3 and escolha2 == 3:
        print('-----------------------------------------------------------------------------------------------------------------')
        print('Jogador 1 escolheu tesoura e o jogador 2 escolheu tesoura')
        print('Empate!')
        print('-----------------------------------------------------------------------------------------------------------------')
        placarE += 1

    # Finalização da gameplay:
    opcao = input('Deseja continuar (s/n): ')
    if opcao != 's':
        continuar = False
        print('-----------------------------------------------------------------------------------------------------------------')

# Conclusão e agradecimentos:
print('Placar final JOGADOR1:', placarJ1, ', JOGADOR2:', placarJ2, ', EMPATE', placarE)
print('Obrigado por usar este programa!')
print('Alunos: Heitor, Hugo, João, Nathan')
