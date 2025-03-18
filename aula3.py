n1  = float(input('digite o primeiro numero: '))
n2  = float(input('digite o segundo numero: '))

soma =  n1 + n2
sub = n1 - n2
mult =  n1 * n2
div = n2/n2

print(f'''

Soma - {soma}
Subtração - {sub}
Multiplicação - {mult}
Divisão -  {div}

''')

nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
nota3 = float(input('Terceira nota: '))
nota4 = float(input('Quarta nota: '))
nota5 = float(input('Quinta nota: '))

media  =  (nota1 + nota2 + nota3 + nota4 + nota5) / 5
print('A media do aluno foi: ', media )

aprovado = media >= 7
recuperacao = media >= 5 and media <= 6.9
reprovado  =  media <5

print('situacao: aprovado: ', aprovado)
print('situacao: recuperação:', recuperacao)
print('situacao: reprovado: ', reprovado)