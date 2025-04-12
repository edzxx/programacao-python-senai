import sqlite3

conexao = sqlite3.connect('banco_de_dados_foda.db')

cursor = conexao.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS pessoas (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    nome TEXT NOT NULL,
    idade INTEGER NOT NULL,
    cidade TEXT NOT NULL
)
''')

nome = input('digite um nome: ')
idade = int(input('digite a idade da pessoa: '))
cidede = input('digite a cidade: ')

cursor.execute('''
    INSERT INTO pessoas (nome, idade, cidade)
    VALUES (?, ?, ?)
''', (nome, idade, cidede))

conexao.commit()

cursor.execute('SELECT * FROM pessoas')
pessoas = cursor.fetchall()

for pessoa in pessoas:
    print(f'''ID: {pessoa[0]}, Nome: {pessoa[1]}, Idade: {pessoa[2]}, Cidade{pessoa[3]}''')

conexao.close()