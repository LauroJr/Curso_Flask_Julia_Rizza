# OBS: Todas as pasta precisam ter um __init__.py, menos as pastas templates e static.
# Os __init__.py indica que aquela pasta é um módulo
# Inicializa essa pasta, dizendo oficialmente que esta é um módulo. Neste caso app é o módulo principal

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand


# criando um objeto do tipo Flask
app = Flask(__name__)

# configurando meu objeto, e criando ele localmente. storage.db será o nome do arquivo
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///storage.db'

# criando um objeto da classe SQLAlchemy e passando como parâmetro o app
db = SQLAlchemy(app)

# o objeto migrate terá a tarefa de manipular o bd e o app
migrate = Migrate(app, db)

# Logo abaixo criamos uma instância de Manager, pois Manager tem comandos próprios para executar nosso app.
# Além do mais, podemos adicionar comandos que já existe no MigrateCommand. Entenda melhor no arquivo
# comandos.txt
manager = Manager(app)
manager.add_command('db', MigrateCommand)

# importamos o arquivo default depois de criar o app, pois necessita que esteja criado antes
from app.controllers import default

# Vamos usar a estrutura de organização MVC:
# Model (Banco de dados- informações)
# View  (Tudo aquilo que o usuário vê. Desde a página HTML, a estilos CSSs e JS(arquivos estáticos))
# Controller (Parte lógica. Onde gravar, onde editar, onde deletar... etc)
