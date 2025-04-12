
print('Loja Bala')

#Cadastro

# usuario = str('Edu')
# senha = int(1223)

# tentativa_usuario = str(input('insira seu usuario: '))
# tentativa_senha = int(input('insira sua senha: '))

# if tentativa_usuario == usuario and tentativa_senha == senha:
produtos = ('Cadeira', 'Mesa', 'uma unidade de prato', 'preda')
valor = (119.99)
carrinho = []
total_a_pagar = []

print('PRODUTOS')
print(f''' Insira qual produto vc deseja
0 - Cadeira
1 - Mesa
2 - uma unidade de prato
3 - preda
''')

escolha1 = int(input('Primeiro produto: '))
escolha2 = int(input('Segundo produto: '))
escolha3 = int(input('Terceiro produto: '))
escolha4 = int(input('Quarto produto: '))

carrinho += (produtos[escolha1], produtos[escolha2], produtos[escolha3], produtos[escolha4])
valor