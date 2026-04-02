from flask import Flask, render_template
from model.burguer import recuperar_produtos
app = Flask(__name__)

@app.route('/')
def index():
    produtos = recuperar_produtos()
    return render_template('./index.html',  produtos = produtos)

@app.route('/produto')
def produto():
    
    return render_template('./produto.html')


app.run(host='0.0.0.0', port=8080, debug=True)

