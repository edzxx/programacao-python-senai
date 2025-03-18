# Exercícios
# 1* 
# Peça para o usuário digitar um número, verifique se um número é positivo, 
# negativo ou zero.

# num1 = int(input('Digite um número: '))
# if num1 > 0:
#     print('Positivo')
# elif num1 < 0:
#     print('Negativo')
# else:
#     print('Zero')

# # 2*
# # Peça para o usuário digitar a idade, verifique se uma pessoa pode votar com 
# # base na idade.

# idade = int(input('Digite sua idade: '))
# if idade >= 16:
#     print('Pode votar')
# else:
#     print('Nao pode votar')

# # 3*
# # Declara uma variável com um número qualquer, determine se um número é par ou ímpar.

# num2 = int(input('Digite um número: '))
# if num2 % 2 == 0:
#     print('Par')
# else:
#     print('Impar')
    
# # 4*
# # Usuário vai digitar 3  números, para criar um triângulo, verifique se um triângulo 
# # é equilátero, isósceles ou escaleno
# # Um triângulo é chamado de equilátero se todos os lados possuem a mesma medida. 
# # Um triângulo é chamado de isósceles se dois lados possuem a mesma medida. 
# # Um triângulo é chamado de escaleno se todos os lados possuem medidas diferentes.

# numt1 = int(input('Digite um número: '))
# numt2 = int(input('Digite um número: '))
# numt3 = int(input('Digite um número: '))
# if numt1 == numt2 == numt3:
#     print('Equilatero')
# elif numt1 == numt2 or numt1 == numt3 or numt2 == numt3:
#     print('Isosceles')
# else:
#     print('Escaleno')   
    
# # 5*
# # Determine se um número é múltiplo de 5 e 7.

# num3 = int(input('Digite um número: '))
# if num3 % 5 == 0 and num3 % 7 == 0:
#     print('Multiplo de 5 e 7')
# else:
#     print('Nao multiplo de 5 e 7')

# # 6*
# # Verifique se um número é positivo e maior que 10

# num4 = int(input('Digite um número: '))
# if num4 > 0 and num4 > 10:
#     print('Positivo e maior que 10')
# else:
#     print('Nao positivo e maior que 10')

# # 7*
# # Verifique se um número é divisível por 3 ou 5.

# num5 = int(input('Digite um número: '))
# if num5 % 3 == 0 or num5 % 5 == 0:
#     print('Divisivel por 3 ou 5')
# else:
#     print('Nao divisivel por 3 ou 5')






print('Loja Bala')

#Cadastro

from asyncio import wait
usuario = str('Edu')
senha = int(1223)

tentativa_usuario = str(input('insira seu usuario: '))
tentativa_senha = int(input('insira sua senha: '))

if tentativa_usuario == usuario and tentativa_senha == senha:
    produtos = ['Cadeira de plastico de bar', 'Mesa de pau', 'Uma unidade de Prato', 'Preda']
    valor = [699.99, 449.99, 50, 30]
    carrinho = []
    total_a_pagar = []

    print('PRODUTOS')
    print(f''' Insira qual produto vc deseja
    0 - Cadeira de plastico de bar
    1 - Mesa de pau
    2 - Uma unidade de prato
    3 - Preda
    ''')

    escolha1 = int(input('Primeiro produto: '))
    escolha2 = int(input('Segundo produto: '))
    escolha3 = int(input('Terceiro produto: '))
    escolha4 = int(input('Quarto produto: '))

    carrinho += (produtos[escolha1], produtos[escolha2], produtos[escolha3], produtos[escolha4])
    valor
    total_a_pagar += (valor[escolha1], valor[escolha2], valor[escolha3], valor[escolha4])

    print('Seus produtos são:', carrinho)
    total = sum(total_a_pagar)
    print('')
    print('----' * 10)
    print('A pagar: R$', total)
    print('----' * 10)
    
    opcaodepagamento = int(input(f'''
    {total}                        
                                 
    Como deseja pagar?
    0 - Dinheiro
    1 - Cartao
    2 - Pix

    Escolha a partir do indice: '''))
    if opcaodepagamento == 0:
        print(f'''
    Voce escolheu pagar com dinheiro
    Obrigado pela compra

    Digira-se a unidade mais proxima para efetuar o pagamento
    ''')
    elif opcaodepagamento == 1:
        print(f'''
    Voce escolheu pagar com cartao
    Insira os dados de pagamento a seguir''')
    elif opcaodepagamento == 2:
        print('''Voce escolheu pagar com pix
    Gerando o pix...''')
    print('Escaneie e QR code ou copie o codigo Pix')
else:
    print('Usuario ou senha incorretos')