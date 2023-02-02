from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_bcrypt import Bcrypt

# __name__: faz referência a esse próprio arquivo
app = Flask(__name__)
app.config.from_pyfile('config.py')

# Instancia o banco do SQLAlchemy que faz a ponte com o banco de dados real
db = SQLAlchemy(app)
csrf = CSRFProtect(app)
bcypt = Bcrypt(app)

# Importa todas as rotas
from views_game import *
from views_user import *

# Faz rodar com todas as importações da aplicação
if __name__ == '__main__':
    app.run(debug=True)