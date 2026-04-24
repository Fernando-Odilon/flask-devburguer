CREATE DATABASE db_burguer_produto;
USE db_burguer_produto;

CREATE TABLE IF NOT EXISTS burguer(
codigo_produto INT PRIMARY KEY AUTO_INCREMENT,
produto VARCHAR(50),
descricao VARCHAR(200),
preco DECIMAL(7, 2),
destaque bool default 0,
foto VARCHAR(200),
disponibilidade bool default 1);

CREATE TABLE IF NOT EXISTS usuario(
codigo_usuario INT,
user_name VARCHAR(200) unique PRIMARY KEY,
user_password VARCHAR (200));


CREATE TABLE IF NOT EXISTS carrinho (
codigo_carrinho INT PRIMARY KEY AUTO_INCREMENT,
user_name VARCHAR(200),
finalizado bool,
CONSTRAINT fk_carrinho_usuario FOREIGN KEY (user_name) REFERENCES usuario(user_name)
);

CREATE TABLE IF NOT EXISTS itens_carrinho (
codigo_itens_carrinho INT PRIMARY KEY AUTO_INCREMENT,
cod_carrinho int,
cod_produto int,
quantidade int,
CONSTRAINT fk_itens_carrinhos FOREIGN KEY (cod_carrinho) REFERENCES carrinho(codigo_carrinho),
CONSTRAINT fk_itenscarrinho_burguer FOREIGN KEY (cod_produto) REFERENCES burguer(codigo_produto)
);




INSERT INTO burguer (produto, descricao, preco, foto) VALUES
('Classic Dev', 'Pão brioche, carne suculenta e queijo derretido.', 25.00, 'https://images.pexels.com/photos/1639557/pexels-photo-1639557.jpeg?auto=compress&cs=tinysrgb&w=600'),
('Double Stack', 'Dois hambúrgueres, bacon crocante e molho especial.', 38.00, 'https://images.pexels.com/photos/2983101/pexels-photo-2983101.jpeg?auto=compress&cs=tinysrgb&w=600'),
('Veggie Script', 'Hambúrguer de grão de bico com salada fresca.', 30.00, 'https://images.pexels.com/photos/3219483/pexels-photo-3219483.jpeg?auto=compress&cs=tinysrgb&w=600'),
('Java Chicken', 'Frango empanado crocante com alface e maionese.', 28.00, 'https://images.pexels.com/photos/12034622/pexels-photo-12034622.jpeg'),
('Python Onion', 'Anéis de cebola, barbecue e queijo cheddar.', 33.00, 'https://images.pexels.com/photos/70497/pexels-photo-70497.jpeg?auto=compress&cs=tinysrgb&w=600'),
('React Salad', 'Uma opção leve e reativa para o seu almoço.', 27.00, 'https://images.pexels.com/photos/1199957/pexels-photo-1199957.jpeg?auto=compress&cs=tinysrgb&w=600');

-- 1. Inserindo um usuário (Necessário para o carrinho existir)
INSERT INTO usuario (codigo_usuario, user_name, user_password) 
VALUES (1, 'dev_faminto', 'senha123');

-- 2. Criando um carrinho para este usuário (finalizado = 0 significa "aberto")
INSERT INTO carrinho (user_name, finalizado) 
VALUES ('dev_faminto', 0);

-- 3. Adicionando itens ao carrinho recém-criado
-- Note: O cod_carrinho será 1 (se for o primeiro registro) e o cod_produto 1 e 2 (Classic Dev e Double Stack)
INSERT INTO itens_carrinho (cod_carrinho, cod_produto, quantidade) VALUES 
(1, 1, 2), -- 2 unidades do Classic Dev
(1, 2, 1); -- 1 unidade do Double Stack



SELECT * FROM carrinho 
INNER JOIN itens_carrinho ON carrinho.codigo_carrinho = itens_carrinho.cod_carrinho
INNER JOIN burguer ON burguer.codigo_produto = itens_carrinho.cod_produto
INNER JOIN usuario ON usuario.user_name = carrinho.user_name


