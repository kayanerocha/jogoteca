from flask import Flask
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

app.run(debug=True)