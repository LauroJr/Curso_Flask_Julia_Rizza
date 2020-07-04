# OBS: Todas as pasta precisam ter um __init__.py, menos as pastas templates e static.
# Os __init__.py indica que aquela pasta é um módulo
# Inicializa essa pasta, dizendo oficialmente que esta é um módulo. Neste caso app é o módulo principal

from flask import Flask

app = Flask(__name__)

from app.controllers import default

# Vamos usar a estrutura de organização MVC:
# Model (Banco de dados- informações)
# View  (Tudo aquilo que o usuário vê. Desde a página HTML, a estilos CSSs e JS(arquivos estáticos))
# Controller (Parte lógica. Onde gravar, onde editar, onde deletar... etc)
