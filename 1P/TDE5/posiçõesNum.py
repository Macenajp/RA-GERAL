# Questão 9 da lista:
posicao = 0
contador = 0
vetor = []

for i in range(10):
    a = int(input('Insira um número: '))
    vetor.append(a)
b = int(input('Qual valor você quer verificar?'))
numeroIdentificado = []

for numero in vetor:
    if numero == b:
        contador += 1
        numeroIdentificado.append(posicao)
    posicao += 1

print(f'O número está na(s) seguinte(s) posição(ões) {numeroIdentificado} e aparece(em):' f' {contador}x')
