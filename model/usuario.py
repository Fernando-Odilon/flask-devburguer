import mysql.connector
from database.conexao import conectar

def recuperar_users(usuario, password):
    conexao, cursor = conectar()
    cursor.execute('SELECT codigo_usuario, user_name, user_password FROM usuario WHERE user_name = %s AND user_password = %s', (usuario, password))
    user = cursor.fetchone()
    if user:
        return user
    else:
        return False
    
def cadastrar_usuario(usuario, password):
    conexao, cursor = conectar()
    cursor.execute('SELECT * FROM usuario;')
    num_users = cursor.fetchall()
    try:
        cursor.execute('INSERT INTO usuario(codigo_usuario, user_name, user_password) VALUES(%s, %s, %s)', ((len(num_users) + 1), usuario, password))
        conexao.commit()
        conexao.close()
        return True
    except:
        return False

    