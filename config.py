import os

SECRET_KEY = 'kvrds' # camada de segurança que criptografa o cookie

SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD = 'mysql+mysqlconnector',
        usuario = 'root',
        senha = '',
        servidor = '127.0.0.1',
        database = 'jogoteca'
    )

# Pega o caminho absoluto do diretório que esse arquivo (__file__) está e acessa o uploads
UPLOAD_PATH = os.path.dirname(os.path.abspath(__file__)) + '\\uploads'