from flask import Flask, render_template, request, redirect

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

jogo1 = Jogo('Tetris', 'Puzzle', 'Atari')
jogo2 = Jogo('God of War', 'Rack and Slash', 'PS2')
jogo3 = Jogo('Mortal Kombat', 'Luta', 'PS2')
jogos = [jogo1, jogo2, jogo3]

# __name__: faz referência a esse próprio arquivo
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('lista.html', titulo='Jogos', jogos=jogos)

@app.route('/novo')
def novo():
    return render_template('novo.html', titulo='Novo Jogo')

@app.route('/criar', methods=['POST'])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    jogos.append(jogo)

    return redirect('/')

app.run(debug=True)