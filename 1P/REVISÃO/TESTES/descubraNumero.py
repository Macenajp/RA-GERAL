import random
def numero():
    return random.randint(1, 50)

def jogadas():
    resposta = numero()

    print("Descubra o número! - Entre 0 e 50, você tem cinco tentativas.")
    while chutes > resposta or chutes < resposta:
        tentativa += 1
        chute = int(input("Qual o seu chute? "))
        if chute > resposta or chute < resposta:
            print("Vish, você errou.")
        else:
            print("Você acertou. Parabéns!"
                  "<=====================>")
            break

        if resposta > chute:
            print("Tente um número maior que esse.")
        else:
            print("Tente um número menor que esse.")
while True:
    jogadas()
