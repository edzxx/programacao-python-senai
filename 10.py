# # 1 - CRIE UMA FUNÇÃO PARA COMPARAR 2 NÚMEROS (par ou impar). UTILIZE VARIÁVEIS LOCAIS.

# def par_impar():
#     n = int(input('Digite um número: '))
#     n2 = int(input('Digite outro número: '))
    
#     if n % 2 == 0 and n2 % 2 == 0:
#         print('---' * 10)
#         print(f'{n} e {n2} sao pares')
#     elif n % 2 == 0 and n2 % 2 == 1:
#         print('---' * 10)
#         print(f'{n} é par e {n2} é impar')
#     elif n % 2 == 1 and n2 % 2 == 0:
#         print('---' * 10)
#         print(f'{n} é impar e {n2} é par')
#     else:
#         print('---' * 10)
#         print(f'{n} e {n2} ambos sao impares')

# par_impar()

# # 2 - CRIE UMAFUNÇÃO PARA MULTIPLICAR 3 NUMEROS.

# def multiplicar():
#     n = int(input('Digite um número: '))
#     n2 = int(input('Digite outro número: '))
#     n3 = int(input('Digite outro número: '))
#     print('---' * 10)
#     print(f'Resultado: {n * n2 * n3}')
    
# multiplicar()

# # 3 - CRIE UMA FUNÇÃO PARA DESCOBRIR O VALOR ELEVADO DE UM NÚMERO.

# def elevado():
#     n = int(input('Digite um número: '))
#     n2 = int(input('Digite outro número: '))
#     print('---' * 10)
#     print(f'Resultado: {n ** n2}')
    
# elevado()

# # 4 - CRIE UMA FUNÇÃO PARA MOSTRAR UMA MENSAGEM PERSONALIZADA NA TELA, SE O USUÁRIO  DIGITAR, 18 ANOS

# def mensagem():
#     idade = int(input('Digite sua idade: '))
#     if idade >= 18:
#         print('---' * 10)
#         print(f'Parabens, vocé tem 18 anos')
#     else:
#         pass
    
# mensagem()

# # 5 - DESENVOLVA UMA FUNÇÃO PARA DESCOBRIR A IDADE DE UMA PESSOA.

# def idade():
#     idade = int(input('Digite sua idade: '))
#     print('---' * 10)
#     print(f'Voce tem {idade} anos')
    
# idade()

# # 6 - DESENVOLVA UM AFUNÇÃO PARA VER SE O BRASIL GANHOU A COPA DE 1999

# def copa():
#     b_resultado = input('quantos gols o brasil fez: ')
#     ad_resultado = input('quantos gols o Uruguai fez: ')
#     if b_resultado == 3 and ad_resultado == 0:
#         print('---' * 10)
#         print('O Brasil ganhou a Copa de 1999 contra o Uruguai')
#     else:
#         print('---' * 10)
#         print('Resposta incorreta')
# copa()

# # 7 - DESENVOLVA UM SISTEMA DE RESTAURANTE, ONDE O CLIENTE TEM OPÇÃO DE ESCOLHER ENTRE SALADA, MACARRONADA,
# # SANDUICHE, SORVETE.

# Restaurante

produtos = ['Salada', 'Macarronada', 'Sanduiche', 'Sorvete']
preco_prod = [10, 15, 20, 25]
formas_de_pagamento = ['Dinheiro', 'Cartão', 'Pix']
preco = []
carrinho = []



def escolha_de_produtos():
    print('---' * 10)
    print(f'''
    1 - Salada
    2 - Macarronada
    3 - Sanduiche
    4 - Sorvete
    ''')
    print('---' * 10)
    
    
    escolha = int(input('Escolha um produto: '))
    carrinho.append(produtos[escolha - 1])
    preco.append(preco_prod[escolha - 1])
    print('---' * 10)
    print(f'Voce escolheu: {produtos[escolha - 1]}')
    print('')
    print('Seus produtos: ', carrinho)
    print('Total: R$', sum(preco))
    print('')
    print('---' * 10)

def mais_pedido():
    
    pedido_mais = str(input('Deseja fazer mais um pedido? s/n: '))
    while pedido_mais == 's':
        escolha_de_produtos()
        mais_pedido()
    else:
        pagamento()
    
        
def pagamento():
    
    print(f'''
        Seus produtos: {carrinho}
        Total: R${sum(preco)}
        ''')
    forma_de_pagamento = str(input(f'''
    Como deseja pagar?
    1 - Dinheiro
    2 - Cartão
    3 - Pix

    Escolha a partir do indice: '''))
    print('---' * 10)
    
    if forma_de_pagamento == '1':
        print('Voce escolheu pagar com dinheiro')
    elif forma_de_pagamento == '2':
        print('Voce escolheu pagar com cartao')
    elif forma_de_pagamento == '3':
        print('Voce escolheu pagar com pix')
    print('---' * 10)
    print('Obrigado pela compra')
        
        
        
fazer_pedido = str(input('Deseja fazer um pedido? s/n: '))

if fazer_pedido == 's':
    escolha_de_produtos()
    mais_pedido()
else:
    print('Obrigado pela compra')


    

    

































input('Pressione enter para sair')