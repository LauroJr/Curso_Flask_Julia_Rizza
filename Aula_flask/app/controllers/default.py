from app import app


@app.route('/')
def index():
    return 'Hello, World!'

# Aqui criamos a parte lógica, daquilo que tem a finalidade de mostrar ao usuário aquilo que
# queremos mostrar á ele.
