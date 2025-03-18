# CONCATENAÇÃO: 

# TIPOS: 

# print(cumprimento, nome,'Sua senha é',senha)
# print(f'{cumprimento} {nome} Sua senha é {senha}')
# print(cumprimento + " "+ nome+ " " + 'Sua senha é',senha )
# print(cumprimento, nome, 'Sua senha é {}'.format(senha))
# print(cumprimento, nome, 'Sua senha é %s'%(senha))

# 1
print('Bem Vindo')

# 2
VarBool = True
print(type(VarBool))

#3
ResultadoMD = 13.2 * 5.6
print('O resultado da multiplicação decimal é : ', ResultadoMD)

#4
ResultadoDD = 15.5 / 5.5
print('O resultado da Divisão decimal é : ', ResultadoDD)

#5
ResultadoS = 55 - 20
print('O resultado da subtração é: {}'.format(ResultadoS))

#6
ResultadoDI = 10 / 5
print('O resultado da Divisão inteira é : ', ResultadoDI)

#7
NumM1 = 2
NumM2 = 5
NumM3 = 2
NumM4 = 8
print(f'O resultado da multiplicação dos 4 numeros é: {NumM1 * NumM2 * NumM3 * NumM4}')

#8

numero = 6
print(numero * 2)

#9

NumeroSoma1 = float(input("Digite o primeiro numero: "))
NumeroSoma2 = float(input("Digite o segundo numero: "))
ResultadoSoma = NumeroSoma1 + NumeroSoma2

print('Resultado da Soma é: {}'.format(ResultadoSoma))

#10

Nome = input('Qual é o seu nome: ')
Idade = int(input('Qual sua idade: '))
Senha = int(input('Qual sua Senha: '))

print(f'''
Nome: {Nome}
Idade: {Idade}
Senha: {Senha}
      ''')