from flask import Flask, render_template

# __name__: faz referência a esse próprio arquivo
app = Flask(__name__)

@app.route('/inicio')
def ola():
    return render_template('lista.html')

app.run()