from flask import Flask, render_template
app = Flask(__name__, template_folder='templates')


@app.route('/')
def home():
    return render_template("index.html",titulo_pagina="Página inicial")


@app.route('/fofocas')
def fofocas():
    return render_template("paginas/fofocas.html",titulo_pagina="Fofocas")


@app.route('/esportes')
def esportes():
    return render_template("paginas/esportes.html",titulo_pagina="Esportes")


@app.route('/politica')
def politica():
    return render_template("paginas/politica.html",titulo_pagina="Politica")


if __name__ =="__main__":
    app.run(debug=True)