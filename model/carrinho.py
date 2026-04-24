import mysql.connector
from database.conexao import conectar

def buscar_carrinho(usuario):
    conexao, cursor = conectar()
    cursor.execute('SELECT codigo, user_name, finalizado FROM carrinho WHERE user_name = %s', (usuario,))
    carrinho = cursor.fetchall()
    conexao.close()
    return carrinho