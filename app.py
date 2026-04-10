from flask import Flask, render_template
from model.burguer import recuperar_produtos
app = Flask(__name__)

@app.route('/')
def index():
    produtos = recuperar_produtos()
    return render_template('./index.html',  produtos = produtos)

@app.route('/produto/<codigo>')
def produto(codigo):
    produto = recuperar_produtos(codigo)
    print(produto)
    return render_template('./produto.html', produto = produto)



app.run(host='0.0.0.0', port=8080, debug=True)

