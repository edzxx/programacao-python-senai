# ListaVazia = []
# lista = [37,5,7,10,54, 'a' , True , 5.4]
# listaF = [1.4,5.7,95.3]
# listaI = [1,7,65,42,88,1022]
# listaB = [True, True, False]
# listaS = ['oi', 'palavra', 'Eu', 'Coisas']

# lista[4] = 999 

# numero1 = lista[2]
# numero2 = lista[4]
# lista[0] = listaF[2] ** 4

# soma = numero1 + numero2

# # print(soma)
# # print(lista[0])


# # inserir dado

# listaF.append(88.4)
# listaF.insert(1, 20.3)
# listaF.extend([2, 20, 59 ,89 ,88])

# # remover dado

# print('Original', listaF)

# listaF.pop(2)
# del listaF[1] 
# listaF.remove(59)

# print('Alterado' ,listaF)

# indice = listaF.index(20)
# print('indice do primero elemento na lista', indice)


# lista1 = (1,1,1,1,2,2,7,6,6,2,2,2,2,2,3,3,3,4,4,6,5,5,5)
# print(lista1)
# print('contador quantidade de um numero especifico', lista1.count(5))

# tamanho = len(lista1)
# maior = max(lista1)
# menor = min(lista1)

# print('tamanho')

# lista2 = list(range(1,101))
# # lista2.sort(reverse=True)
# print(lista2)





# EXERCICIOS

# listaPares =  list(range(2,22, 2))
# print('lista de pares', listaPares)

# numeros = list(range(1,11))
# print('todos os numeros: ', numeros)
# print('terceiro numero: ', numeros[2])
# numeros.append(9)
# print('numeros com o 9 adicionado', numeros)
# numeros.remove(5)
# print('sem o 5', numeros)
# carros = ('Carro 1', 'Carro 2', 'Carro 3')
# carrosenumeros = (carros, numeros)
# print(carrosenumeros)





# MERCADO


# lista_prod = ['meias', 'camisas', 'calcas', 'tenis']
# valores = [10.0, 150.0, 89.99, 299.99]
# print('Produtos disponiveis')
# print(lista_prod)

# print('----' * 10)

# carrinho = []
# meu_total = []

# prod1 = int(input(f'''
# 0 - Meias
# 1 - Camisas
# 2 - Calcas
# 3 - Tenis
# Escolha a partir do indice: '''))

# prod2 = int(input(f'''
# 0 - Meias
# 1 - Camisas
# 2 - Calcas
# 3 - Tenis
# Escolha a partir do indice: '''))

# prod3 = int(input(f'''
# 0 - Meias
# 1 - Camisas
# 2 - Calcas
# 3 - Tenis
# Escolha a partir do indice: '''))

# carrinho += (lista_prod[prod1], lista_prod[prod2], lista_prod[prod3])
# meu_total += (valores[prod1], valores[prod2], valores[prod3])

# print('Seus produtos são:', carrinho)
# print('***' * 21)
# total = sum(meu_total)
# print('R$', total)




# DESAFIO 1


## Desafio 1

# Crie um e-commerce com a estrutura de dicionários.
# Produtos:  Livros, tablets e fones de ouvido
# As ações: 
# Comprar()
# Pagar()
# mostra o valor da compra


print('E commerce')
print('----' * 10)

lista_prod = ['livros', 'tablets', 'fones de ouvido']
valores = [9.99, 1439.99, 89.99]
print('Produtos disponiveis')

carrinho = []   
meu_total = []

prod1 = int(input(f'''
0 - Livros
1 - Tablets
2 - Fones de ouvido
Escolha a partir do indice: '''))

prod2 = int(input(f'''
0 - Livros
1 - Tablets 
2 - Fones de ouvido
Escolha a partir do indice: '''))

prod3 = int(input(f'''  
0 - Livros          
1 - Tablets 
2 - Fones de ouvido
Escolha a partir do indice: '''))

carrinho += (lista_prod[prod1], lista_prod[prod2], lista_prod[prod3])
meu_total += (valores[prod1], valores[prod2], valores[prod3])

print('Seus produtos são:', carrinho)
total = sum(meu_total)
print('')
print('----' * 10)
print('A pagar: R$', total)
print('----' * 10)
OpcoesDePagamento = ['Dinheiro', 'Cartao', 'Pix']

Pagamento = int(input(f'''
Como deseja pagar 
0 - Dinheiro
1 - Cartao
2 - Pix

Escolha a partir do indice: '''))
print('----' * 10)
print('Voce escolheu escolheu pagar com:', OpcoesDePagamento[Pagamento])
print('----' * 10)
print('Obrigado pela compra')