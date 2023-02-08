from jogoteca import app
from flask import request, render_template, session, flash, redirect, url_for
from helpers import FormularioUsuario
from models import Usuarios
from flask_bcrypt import check_password_hash

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    proxima = 'novo' if proxima is None else proxima
    form = FormularioUsuario()
    return render_template('login.html', proxima=proxima, form=form)

@app.route('/autenticar', methods=['POST'])
def autenticar():
    form = FormularioUsuario(request.form)
    nickname = form.nickname.data
    usuario = Usuarios.query.filter_by(nickname=nickname).first()
    senha = check_password_hash(usuario.senha, form.senha.data)
    if usuario and senha:
        session['usuario_logado'] = nickname
        flash(f'{usuario.nickname} logado com sucesso!')
        proxima_pagina = request.form["proxima"]
        return redirect(proxima_pagina)
    flash('Usuário não logado!')
    return redirect(url_for('login'))

@app.rout('/novo-usuario')
def novo():
    return render_template()

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso!')
    return redirect(url_for('index'))