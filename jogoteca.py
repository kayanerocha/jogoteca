from flask import Flask, render_template, request, redirect, session, flash, url_for
from flask_sqlalchemy import SQLAlchemy

class Jogo:
    def __init__(self, nome, categoria, console) -> None:
        self.__nome = nome
        self.__categoria = categoria
        self.__console = console
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def categoria(self):
        return self.__categoria
    
    @property
    def console(self):
        return self.__console

class Usuario:
    def __init__(self, nome, nickname, senha) -> None:
        self.__nome = nome
        self.__nickname = nickname
        self.__senha = senha
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def nickname(self):
        return self.__nickname
    
    @property
    def senha(self):
        return self.__senha

usuario1 = Usuario('Kayane', 'kayane', '1234')
usuario2 = Usuario('Vitória', 'vitoria', '5678')
usuario3 = Usuario('Camila', 'cami', '2468')
usuarios = {usuario1.nickname: usuario1.senha,
            usuario2.nickname: usuario2.senha,
            usuario3.nickname: usuario3.senha}

jogo1 = Jogo('Tetris', 'Puzzle', 'Atari')
jogo2 = Jogo('God of War', 'Rack and Slash', 'PS2')
jogo3 = Jogo('Mortal Kombat', 'Luta', 'PS2')
jogos = [jogo1, jogo2, jogo3]

# __name__: faz referência a esse próprio arquivo
app = Flask(__name__)
app.secret_key = 'kvrds' # camada de segurança que criptografa o cookie

app.config['SQLALCHEMY_DATABASE_URI'] = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD = 'mysql+mysqlconnector',
        usuario = 'root',
        senha = '',
        servidor = '127.0.0.1',
        database = 'jogoteca'
    )

# Instancia o banco do SQLAlchemy que faz a ponte com o banco de dados real
db = SQLAlchemy(app)

@app.route('/')
def index():
    return render_template('lista.html', titulo='Jogos', jogos=jogos)

@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima='novo'))
    return render_template('novo.html', titulo='Novo Jogo')

@app.route('/criar', methods=['POST'])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    jogos.append(jogo)

    return redirect(url_for('index'))

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    proxima = 'novo' if proxima is None else proxima
    return render_template('login.html', proxima=proxima)

@app.route('/autenticar', methods=['POST'])
def autenticar():
    nickname = request.form['usuario']
    if nickname in usuarios:
        if request.form['senha'] == usuarios[nickname]:
            session['usuario_logado'] = nickname
            flash(f'{nickname} logado com sucesso!')
            proxima_pagina = request.form["proxima"]
            return redirect(proxima_pagina)
    flash('Usuário não logado!')
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso!')
    return redirect(url_for('index'))

app.run(debug=True)