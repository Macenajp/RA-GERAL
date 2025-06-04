import time

itens = [[1, 3.75, 2],
         [2, 3.67, 5],
         [3, 9.96, 1],
         [4, 1.25, 100],
         [5, 13.99, 2]]

produtos = ('Coca-cola', 'Pepsi', 'Monster', 'Café', 'Redbull')
estoque_cedulas = {
    #Nota/moeda:        Quantidade de cada:
    200:                1,
    100:                3,
    50:                 4,
    20:                 5,
    10:                 10,
    5:                  12,
    2:                  10,
    1:                  20,
    0.50:               25,
    0.25:               25,
    0.10:               50,
    0.05:               50,
    0.01:               50
}

def escolha_produto():
    indice = 0
    print('-' * 20)
    print('Lista dos produtos:')
    for produto in produtos:
        print(f'{indice} - {produto} R${itens[indice][1]}')
        indice += 1
    print('-=' * 30)
    escolha = int(input('Qual bebida você quer comprar? '))
    return escolha

def verificar_produto(indice):
    if 0 <= indice < len(produtos):
        estoque = itens[indice][2]
        print(f'Produto disponível! Há {estoque} unidades.')
        print('-' * 20)
        return estoque > 0
    else:
        print('Produto inválido.')
        return False

def pagamento_parcial(indice):
    valor_produto = float(itens[indice][1])
    acumulado = 0
    print(f'Valor do produto: R${valor_produto}')

    while acumulado < valor_produto:
        try:
            inserir = int(input(f'Insira o pagamento (Faltam R${valor_produto - acumulado}): '))
            if inserir <= 0:
                print("Insira um valor positivo.")
                continue
            acumulado += inserir
            if acumulado < valor_produto:
                print(f'Valor insuficiente. Ainda faltam R${valor_produto - acumulado}')
        except ValueError:
            print("Insira um valor válido em reais (apenas inteiros).")

    print(f'Pagamento completo. Total pago: R${acumulado}')
    return acumulado


def calcular_troco(troco):
    cedulas = [100, 50, 20, 10, 5, 2, 1, 0.50, 0.25, 0.10, 0.05, 0.01]
    troco_restante = troco
    print("\nSeu troco:")

    for cedula in cedulas:
        if troco_restante >= cedula:
            qtd = int(troco_restante // cedula)
            if qtd > 0 and estoque_cedulas[cedula] >= qtd:
                print(f"{qtd}x R${cedula:.2f}")
                troco_restante -= qtd * cedula
                estoque_cedulas[cedula] -= qtd

    if troco_restante < 0:                                              # Aqui troquei o ">" pelo "<", pois estava apresentando msg de erro, mesmo com o troco certo
        print("ERRO: Não há cédulas suficientes para o troco completo!")
        return False

    return True

    print("Seu troco:")
    for cedula in cedulas:
        if troco >= cedula:
            qtd = troco // cedula
            if qtd > 0 and estoque_cedulas[cedula] >= qtd:
                print(f"{qtd}x R${cedula}")
                troco -= qtd * cedula
                estoque_cedulas[cedula] -= qtd                          #Atualiza o estoque

    return True

def verificar_pagamento(indice, valor_pago):
    valor_produto = float(itens[indice][1])
    time.sleep(3)
    if valor_pago >= valor_produto:
        troco = valor_pago - valor_produto
        if troco > 0:
            sucesso = calcular_troco(troco)
            if not sucesso:
                print("\n** COMPRA CANCELADA ** (Faltou R$", troco,")")
                print("Por favor, retire seu dinheiro.")
                return                                                  #Encerra a função sem entregar o produto

        print('-' * 20)
        print('Retirando o produto...')
        print(f'Pegue sua {produtos[indice]}')
        print("Muito Obrigado pela compra, tenha um ótimo dia!!!")
    else:
        print('Dinheiro insuficiente.')

escolha = escolha_produto()
if verificar_produto(escolha):
    confirmar = int(input('Deseja comprar? 1 - Sim | 2 - Não: '))
    if confirmar == 1:
        pago = pagamento_parcial(escolha)
        verificar_pagamento(escolha, pago)
    else:
        print('Operação cancelada.')
else:
    print('Produto indisponível.')
