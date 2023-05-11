from flask import Flask, render_template as rt
app = Flask(__name__, template_folder='templates')


@app.route('/')
def home():
    titulo_pagina = "Página Inicial"
    return rt("./paginas/index.html",titulo_pagina = titulo_pagina)

@app.route('/sobre/')
@app.route('/sobre/<nome_usuario>')
def sobre(nome_usuario = None):
    titulo_pagina = "Sobre"
    if nome_usuario is None:
        nome_usuario = "Faça login"
    return rt("./paginas/sobre.html",titulo_pagina = titulo_pagina,nome_usuario = nome_usuario)

@app.route('/background/')
@app.route('/background/<nome_usuario>')
def background(nome_usuario = None):
    titulo_pagina = "Background"
    if nome_usuario is None:
        nome_usuario = "Faça login"
    return rt("./paginas/background.html",titulo_pagina = titulo_pagina,nome_usuario = nome_usuario)

@app.route('/servicos/')
@app.route('/servicos/<nome_usuario>')
def servicos(nome_usuario = None):
    titulo_pagina = "Servicos"
    if nome_usuario is None:
        nome_usuario = "Faça login"
    return rt("./paginas/servicos.html",titulo_pagina = titulo_pagina,nome_usuario = nome_usuario)

@app.route('/produtos/')
@app.route('/produtos/<nome_usuario>')
def produtos(nome_usuario = None):
    titulo_pagina = "Produtos"
    if nome_usuario is None:
        nome_usuario = "Faça login"
    return rt("./paginas/produtos.html",titulo_pagina = titulo_pagina,nome_usuario = nome_usuario,pagina_produtos = True)



if __name__ == "__main__":
    app.run(debug=True)
