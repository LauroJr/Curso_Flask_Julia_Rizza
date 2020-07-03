from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello, World!'


if __name__ == '__main__':
    app.run()


# Vamos usar a estrutura de organização MVC:
# Model (Banco de dados- informações)
# View  (Tudo aquilo que o usuário vê. Desde a página HTML, a estilos CSSs e JS(arquivos estáticos))
# Controller (Parte lógica. Onde gravar, onde editar, onde deletar... etc)
