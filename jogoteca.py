from flask import Flask, render_template

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

# __name__: faz referência a esse próprio arquivo
app = Flask(__name__)

@app.route('/inicio')
def ola():
    jogo1 = Jogo('Tetris', 'Puzzle', 'Atari')
    jogo2 = Jogo('God of War', 'Rack and Slash', 'PS2')
    jogo3 = Jogo('Mortal Kombat', 'Luta', 'PS2')
    jogos = [jogo1, jogo2, jogo3]
    return render_template('lista.html', titulo='Jogos', jogos=jogos)

app.run()