import mysql.connector
from database.conexao import conectar

def buscar_carrinho(usuario):
    conexao, cursor = conectar()
    cursor.execute("""SELECT 
                    codigo_carrinho, 
                    carrinho.user_name, 
                    finalizado, 
                    quantidade, 
                    produto, 
                    preco, 
                    foto,
                    codigo_itens_carrinho
                    FROM carrinho 
                    INNER JOIN itens_carrinho ON carrinho.codigo_carrinho = itens_carrinho.cod_carrinho
                    INNER JOIN burguer ON burguer.codigo_produto = itens_carrinho.cod_produto
                    INNER JOIN usuario ON usuario.user_name = carrinho.user_name
                    WHERE carrinho.user_name = %s""", (usuario,))
    carrinho = cursor.fetchall()
    conexao.close()
    return carrinho


def adicionar_item_carrinho(usuario, codigo_produto, quantidade = 1):
    conexao, cursor = conectar()
    cursor.execute("SELECT codigo_carrinho FROM carrinho WHERE user_name = %s AND finalizado = 0 limit 1", (usuario,))
    resultado_carrinho = cursor.fetchone()
    if resultado_carrinho:
        codigo_carrinho = resultado_carrinho['codigo_carrinho']
        print(codigo_carrinho)
    else:
        cursor.execute("INSERT INTO carrinho(user_name) VALUES(%s)",(usuario,))
        codigo_carrinho = cursor.lastrowid
    print(codigo_carrinho)
    cursor.execute("INSERT INTO itens_carrinho(cod_carrinho, cod_produto, quantidade) VALUES(%s, %s, %s)",(codigo_carrinho, codigo_produto, quantidade))
    conexao.commit()
    conexao.close()


def remover_item_carrinho(codigo_item):
    conexao, cursor = conectar()

    cursor.execute("DELETE FROM itens_carrinho WHERE codigo_itens_carrinho = %s", (codigo_item,))
    
    conexao.commit()
    conexao.close()



