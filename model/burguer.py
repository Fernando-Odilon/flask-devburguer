import mysql.connector
from database.conexao import conectar

def recuperar_produtos(id = False):
    conexao, cursor = conectar()
    if not id:
        cursor.execute('SELECT codigo, produto, descricao, preco, destaque, foto, disponibilidade FROM burguer;')
        produtos = cursor.fetchall()
    else:
        cursor.execute('SELECT codigo, produto, descricao, preco, destaque, foto, disponibilidade FROM burguer WHERE codigo = %s;', (id,))
        produtos = cursor.fetchone()
    conexao.close()
    return produtos
