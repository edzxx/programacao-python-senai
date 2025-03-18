# ***Sistema de Reservas de Hotel:***
# ***Você foi contratado(a) para desenvolver uma parte do sistema de um hotel. 
# O objetivo é criar um sistema que gerencie reservas de quartos e o pagamento das diárias***.
# - *Cadastro de Cliente:*
# *O sistema deve permitir que o usuário "cadastre" o nome e a idade de até 3 clientes.*
# - *Reservas de Quartos:*
# ***O sistema deve oferecer 3 tipos de quartos:*** 
# ***"Simples", "Duplo" e "Luxo".***
# ***Cada cliente deve escolher um quarto para sua estadia.
# O preço da diária varia conforme o tipo de quarto:
# Simples: R$ 100,00 por dia.
# Duplo: R$ 150,00 por dia.
# Luxo: R$ 250,00 por dia.***
# - ***Cálculo da Estadia:***
# ***O usuário deve informar quantos dias cada cliente ficará no hotel.
# O sistema deve calcular o valor total da estadia para cada cliente, considerando o tipo de quarto e a quantidade de dias.***
# Exemplo: 
#  ***valor_cliente3 = preco_duplo * cliente3_dias***
# *Pagamento:*
# *O sistema deve exibir o valor total a ser pago por cada cliente após a aplicação do desconto.*
# *Regras Adicionais:
# Utilize apenas variáveis, condicionais (if, elif, else) e listas para resolver o desafio.*
# ***O sistema não deve usar loops (for, while) nem funções.**
# O código deve considerar todos os casos possíveis de escolha dos clientes.*


#Sistema de Reservas de Hotel

#Cadastro de Clientes

clientes = {'Edu' : 123}
Escolha_cadastro = str(input('Voce deseja inicar um cadastro: s/n: '))

if Escolha_cadastro == 's':
    print('')
    Cadastro_quantidade = str(input('Você deseja cadastrar quantos clientes: '))

    for i in range(int(Cadastro_quantidade)):
        usuario = str(input('Digite o usuario do cliente: '))
        senha = int(input('Digite a senha do cliente: '))
        clientes.append([usuario, senha])
else:
    print('Cadastro nao iniciado')
    print('')
    print('---' * 10)
    print('')

Escolha_Login = str(input('Voce deseja fazer login: s/n: '))
if Escolha_Login == str('s'):
    print('')
    Login_Usuario = str(input('Digite o usuario: '))
    Login_Senha = int(input('Digite a senha: '))

    for usuario, senha in clientes.items():
        if Login_Usuario == usuario and Login_Senha == senha:
            print('Login efetuado com sucesso')
            print('---' * 10)
            print(f'Olá {Login_Usuario} seja bem vindo')
            print('Deseja fazer alguma reserva? s/n')
            Quartos = {'Simples': 100, 'Duplo': 150, 'Luxo': 250}
    
            Escolha_Reserva = str(input())
        if Escolha_Reserva == 's':
            print(f''' Qual quarto deseja?
    1- Simples: R$ 100,00 por dia.
    2- Duplo: R$ 150,00 por dia.
    3- Luxo: R$ 250,00 por dia.''')
            Escolha_Quarto = int(input('escolha o quarto pelo indice: '))
            print('')
            Dias = int(input('Quantos dias deseja ficar: '))
            print('---' * 10)
            Total = Quartos[list(Quartos.keys())[Escolha_Quarto - 1]] * Dias
            print(f'Quarto escolhido: {list(Quartos.keys())[Escolha_Quarto - 1]}')
            print(f'Quantidade de dias: {Dias}')
            print(f'Total a pagar: R$ {Total}')
            print('---' * 10)
            
            Escolha_pagamento = int(input(f'''
                {Total}                        
                                            
                Como deseja pagar?
                0 - Dinheiro
                1 - Cartao
                2 - Pix

                Escolha a partir do indice: '''))
            if Escolha_pagamento == 0:
                print(f'''
            Voce escolheu pagar com dinheiro
            Obrigado pela compra

            Digira-se a unidade mais proxima para efetuar o pagamento
            ''')
            elif Escolha_pagamento == 1:
                print(f'''
            Voce escolheu pagar com cartao
            Insira os dados de pagamento a seguir''')
            elif Escolha_pagamento == 2:
                print('''Voce escolheu pagar com pix
            Gerando o pix...''')
            print('Escaneie e QR code ou copie o codigo Pix')
            print('---' * 10)
        else:
            print('pagamento cancelado')      
    else:
        print('')        
else:
    print('voce nao fez login')