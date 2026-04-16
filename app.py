from flask import Flask, render_template, redirect, request, session
from model.burguer import recuperar_produtos
from model.usuario import cadastrar_usuario, recuperar_users
app = Flask(__name__)

app.secret_key = "MEGAMATS"

@app.route('/')
def index():
    if session.get('usuario_logado'):    
        produtos = recuperar_produtos()
        return render_template('./index.html',  produtos = produtos)
    return redirect('/login')

@app.route('/produto/<codigo>')
def produto(codigo):
    produto = recuperar_produtos(codigo)
    print(produto)
    return render_template('./produto.html', produto = produto)

@app.route('/cadastrar')
def cadastro():
    return render_template('cadastro.html')

@app.route('/cadastrar/cadastro', methods = ['POST'])
def cadastrar_user():
    usuario = request.form.get('nome')
    senha = request.form.get('password')
    senha_confirm = request.form.get('confirm-password')
    print(usuario, senha, senha_confirm)
    if cadastrar_usuario(usuario, senha) and len(senha) < 6 and senha != senha_confirm:
        return redirect('/login')
    return redirect('/cadastrar')

@app.route('/login')
def logar():
    return render_template('login.html')

@app.route('/logar', methods = ['POST'])
def logar_user():
    usuario = request.form.get('nome')
    senha = request.form.get('password')
    user = recuperar_users(usuario, senha)
    if user:
        session['usuario_logado'] = user
        return render_template('perfil.html', user = user)
    return redirect('/login')

    


app.run(host='0.0.0.0', port=8080, debug=True)

