import mysql.connector
from mysql.connector import errorcode

print('Conectando...')
try:
    conn = mysql.connector.connect(
        host = '127.0.0.1',
        user = 'root',
        password = ''
    )
except mysql.connector.Error as e:
    if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print('Existe algo errado no nome de usuário ou senha')
    else:
        print(e)

cursor = conn.cursor()

cursor.execute('DROP DATABASE IF EXISTS `jogoteca`;')
conn.commit()
cursor.execute('CREATE DATABASE `jogoteca`;')
conn.commit()
cursor.execute('USE `jogoteca`;')

# Criando tabelas
TABLES = {}
TABLES['jogos'] = ('''
CREATE TABLE `jogos` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `nome` varchar(50) NOT NULL,
    `categoria` varchar(40) NOT NULL,
    `console` varchar(20) NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

TABLES['usuarios'] = ('''
CREATE TABLE `usuarios` (
    `nome` varchar(20) NOT NULL,
    `nickname` varchar(8) NOT NULL,
    `senha` varchar(100) NOT NULL,
    PRIMARY KEY (`nickname`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

for tabela_nome in TABLES:
    tabela_sql = TABLES[tabela_nome]
    try:
        print(f'Criando tabela {tabela_nome}', end=' ')
        cursor.execute(tabela_sql)
        conn.commit()
    except mysql.connector.Error as e:
        if e.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print('Já existe')
        else:
            print(e.msg)
    else:
        print('OK')

# Inserindo usuários
usuario_sql = 'INSERT INTO usuarios (nome, nickname, senha) VALUES (%s, %s, %s)'
usuarios = [
    ('Bruno Divino', 'BD', 'alomohora'),
    ('Camila Ferreira', 'Mila', 'paozinho'),
    ('Guilherme Louro', 'Cake', 'python_eh_vida')
]
cursor.executemany(usuario_sql, usuarios)

cursor.execute('SELECT * FROM jogoteca.usuarios')
print(' ---------- Usuários ---------')
for user in cursor.fetchall():
    print(user[1])

# Inserindo jogos
jogos_sql = 'INSERT INTO jogos (nome, categoria, console) VALUES (%s, %s, %s)'
jogos = [
    ('Tetris', 'Puzzle', 'Atari'),
    ('God of War', 'Hack n Slash', 'PS2'),
    ('Mortal Kombate', 'Luta', 'PS2'),
    ('Valorant', 'FPS', 'PC'),
    ('Crash Bandicoot', 'Hack n Slash', 'PS2'),
    ('Need for Speed', 'Corrida', 'PS2'),
]
cursor.executemany(jogos_sql, jogos)

cursor.execute('SELECT * FROM jogoteca.jogos')
print(' ---------- Jogos ---------')
for jogo in cursor.fetchall():
    print(jogo[1])

# Comitando se nada tem feito
conn.commit()
cursor.close()
conn.close()
