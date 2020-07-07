from app import db

# Vamos criar abaixo uma classe, onde poderemos criar usuários apartir dela
class User(db.Model):
    '''db.Model é uma classe do sqlalchemy, que traz um modelo de tabela padrão'''
    __tablename__ = "users" # users será o nome da minha tabela

    id = db.Column(db.Interger, primary_key=True)
    username = db.Column(db.String, unique= True)
    password = db.Column(db.String)
    name = db.Column(db.String)
    email = db.Column(db.String, unique=True)

    def __init__(self, username, password, name, email):
        self.username = username
        self.password = password
        self.name = name
        self.email = email

    def __repr__(self):
        # __repr__ de representação da tabela.
        # formatação para aparecer as informações de forma agradável(bonitinha)
        return "<User %r>" % self.username


# Vamos criar uma classe dos post dos usuários
class Post(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Interger, primary_key=True)
    content = db.Column(db.Text)
    user_id = db.Column(db.Interger, db.ForeignKey('users.id'))

    # Quando fizer uma pesquisa de determinado usuário, este comando já relaciona tudo...
    #... o que determinado user tem de acordo com o relacionamento que o próprio BD faz...
    #... por meio da FK
    user = db.relationship('User', foreign_keys=user_id)

    def __init__(self, content, user_id):
        # Recebe como parâmetro o conteúdo e o id do usuário que já existe.
        self.content = content
        self.user_id = user_id

    def __repr__(self):
        return "<Post %r>" % self.id


# Criando a classe de follow... Lembrando que essas duas ultimas tabelas, precisam se relacionar com
# o usuário. Preciso saber quem me segue, e quais são os meus posts, e assim sucessivamente.
class Follow(db.Model):
    __tablename__ = "follow"

    id = db.Column(db.Interger, primary_key=True)
    user_id = db.Column(db.Interger, db.ForeignKey('users.id'))
    folower_id = db.Column(db.Interger, db.ForeignKey('users.id'))

    user = db.relationship('User', foreign_keys=user_id)
    follower = db.relationship('User', foreign_keys=folower_id)
