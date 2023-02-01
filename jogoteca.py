from flask import Flask, render_template, request, redirect, session, flash, url_for
from flask_sqlalchemy import SQLAlchemy

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
    lista = Jogos.query.order_by(Jogos.id)
    return render_template('lista.html', titulo='Jogos', jogos=lista)

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

    # Verifica se o jogo existe
    jogo = Jogos.query.filter_by(nome=nome).first()
    if jogo:
        flash('Jogo já existente!')
        return redirect(url_for('index'))
    
    novo_jogo = Jogos(nome=nome, categoria=categoria, console=console)
    db.session.add(novo_jogo)
    db.session.commit()

    return redirect(url_for('index'))

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    proxima = 'novo' if proxima is None else proxima
    return render_template('login.html', proxima=proxima)

@app.route('/autenticar', methods=['POST'])
def autenticar():
    nickname = request.form['usuario']
    usuario = Usuarios.query.filter_by(nickname=nickname).first()
    if usuario:
        if request.form['senha'] == usuario.senha:
            session['usuario_logado'] = nickname
            flash(f'{usuario.nickname} logado com sucesso!')
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