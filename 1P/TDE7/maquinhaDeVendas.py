import time


itens = [[1, 3.75, 2],
         [2, 3.67, 5],
         [3, 9.96, 1],
         [4, 1.25, 100],
         [5, 13.99, 2]]

produtos = ('Coca-cola', 'Pepsi', 'Monster', 'Café', 'Redbull')



def escolha_produto():
    indice = 0
    print('-' * 20)
    print('lista de produtos:')
    for produto in produtos:
        print(f'{indice} - {produto} R${itens[indice][1]}')
        indice += 1
    print('-=' * 30)
    escolha = int(input('Escolha uma bebida?'))
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
    valor_produto = int(itens[indice][1])
    acumulado = 0

    print(f'Valor do produto: R${valor_produto},00')

    while acumulado < valor_produto:
        try:
            inserir = int(input(f'Insira o pagamento (Faltam R${valor_produto - acumulado},00): '))
            if inserir <= 0:
                print("Insira um valor positivo.")
                continue
            acumulado += inserir
            if acumulado < valor_produto:
                print(f'Valor insuficiente. Ainda faltam R${valor_produto - acumulado},00')
        except ValueError:
            print("Insira um valor válido em reais (apenas inteiros).")

    print(f'Pagamento completo. Total pago: R${acumulado},00')
    return acumulado


def calcular_troco(troco):
    cedulas = [100, 50, 20, 10, 5, 2, 1]
    print('Seu troco:')
    for cedula in cedulas:
        qtd = troco // cedula
        troco %= cedula
        if qtd > 0:
            print(f'{qtd}x cédula(s) de R${cedula},00')


def verificar_pagamento(indice, valor_pago):
    valor_produto = int(itens[indice][1])
    time.sleep(3)
    if valor_pago >= valor_produto:
        print('-' * 20)
        print('Retirando o produto...')
        print(f'Pegue sua {produtos[indice]}')
        troco = valor_pago - valor_produto
        print("Muito Obrigado pela compra,tenha um ótimo dia!!!")
        if troco > 0:
            calcular_troco(troco)
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
