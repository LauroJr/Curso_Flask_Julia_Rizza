from app import app
from flask import render_template


@app.route('/')
def index():
    lista = []
    for nome in range(3):
        nome = input('Digite um nome: ')
        lista.append(nome)
    return render_template('index.html', lista=lista)

@app.route('/ola-mundo')
def ola_mundo():
    return 'Hello, World!'

@app.route('/login')
def login():
    return 'Aqui será feito seu login'

# Aqui criamos a parte lógica, daquilo que tem a finalidade de mostrar ao usuário aquilo que
# queremos mostrar á ele.
