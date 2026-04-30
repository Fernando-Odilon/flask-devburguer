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

def remover_item_carrinho(codigo_item):
    conexao, cursor = conectar() # Sua função de conexão
    
    # Deletamos pelo ID único da tabela itens_carrinho

    cursor.execute("DELETE FROM itens_carrinho WHERE codigo_itens_carrinho = %s", (codigo_item,))
    
    conexao.commit()
    cursor.close()
    conexao.close()


