from flask import Flask, render_template, redirect, request, session, jsonify
from model.burguer import recuperar_produtos
from model.usuario import cadastrar_usuario, recuperar_users
from model.carrinho import buscar_carrinho, remover_item_carrinho

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
    usuario = request.form.get('user')
    senha = request.form.get('password')
    user = recuperar_users(usuario, senha)
    if user:
        session['usuario_logado'] = user
        return redirect('/perfil')
    return redirect('/login')
@app.route('/logout')
def deslogar():
    session.clear()
    return redirect('/')

@app.route('/perfil')
def perfil_user():
    user = session['usuario_logado']
    return render_template('perfil_usuario.html', usuario = user)

@app.route("/api/get/carrinho", methods = ["GET"])
def api_get_carrinho():
    if 'usuario_logado' in session:
        carrinho = buscar_carrinho(session['usuario_logado']['user_name'])
        return jsonify(carrinho), 200
    else:
        return jsonify({"message" : "Usuário não logado"}), 401

@app.route("/api/delete/carrinho", methods = ["DELETE"])
def api_delete_carrinho():
    if 'usuario_logado' in session:
        codigo = request.json['codigo']
        remover_item_carrinho(codigo)
        carrinho = buscar_carrinho(session['usuario_logado']['user_name'])
        return jsonify(carrinho), 200
    else:
        return jsonify({"message" : "Usuário não logado"}), 401

app.run(host='0.0.0.0', port=8080, debug=True)

