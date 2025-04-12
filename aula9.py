

# # #atividade 1
# # 1

# n = 1000
# while n > 0:
#     print(n)
#     n = n - 1


# # 2

# pessoas = []
# escolha = 's'

# while escolha == 's':
#     pessoas.append(str(input('Escreva o nome de uma pessoa: ')))
#     escolha = str(input('voce deseja escrever o nome de mais uma pessoa s/n: '))
# else:
#     print(pessoas)




# Crie um sistema de notas, com as seguintes operações:
# ***Utilize While ou for*** 
# Sistema de notas de alunos
# - Acesso a conta com condicionais
# - 3 chances de acessar o sistema
# - Após errar 3 x mensagem que diga que a conta bloqueada 
# - Inserir notas 
# - Fazer a média
    
Senha = 4002
NumeroTentativas = 3

while NumeroTentativas > 0:
    chute =  int(input('Digite sua senha: '))
    if chute == Senha:
        print('Logado com sucesso')
        not1 = int(input('insira a primeira nota: '))
        not2 = int(input('insira a segunda nota: '))
        not3 = int(input('insira a terceira nota: '))
        not4 = int(input('insira a quarta nota: '))

        media = (not1 + not2 + not3 + not4) / 4
        print(f'a media do aluno foi: {media}')
        input('aperte qulquer tecla para finalizar o programa')
        break
    else:
        print('senha incorreta')
        NumeroTentativas = NumeroTentativas - 1
        print(f'voce tem {NumeroTentativas} chances')
    if NumeroTentativas == 0:
        print('suas chances acabaram a conta foi bloqueada')
        input('aperte qulquer tecla para finalizar o programa')
        break


    

    

























































# import random


# chances = 3
# while chances > 0:
#     aleatorio = random.randint(1,10)
#     escolha = int(input('Digite um número: '))
#     if escolha  == aleatorio:
#         print('Acertou em cheio!')
#         print('O numero da sorte é ', aleatorio)
#         break
#     else:
#         chances = chances - 1
#         print('Você tem ', chances, 'chances')
# else:
#     print('Chances esgotadas', chances)
#     print(f'o numero sorteado era o {aleatorio}')
#     print('você perdeu o jogo!!!! ;(')