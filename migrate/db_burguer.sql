CREATE DATABASE db_burguer_produto;
USE db_burguer_produto;

CREATE TABLE IF NOT EXISTS burguer(
codigo INT PRIMARY KEY AUTO_INCREMENT,
produto VARCHAR(50),
descricao VARCHAR(200),
preco DECIMAL(7, 2),
destaque bool default 0,
foto VARCHAR(200),
disponibilidade bool default 1);

CREATE TABLE IF NOT EXISTS usuario(
codigo INT,
user_name VARCHAR(200) unique PRIMARY KEY,
user_password VARCHAR (200));


INSERT INTO burguer (produto, descricao, preco, foto) VALUES
('Classic Dev', 'Pão brioche, carne suculenta e queijo derretido.', 25.00, 'https://images.pexels.com/photos/1639557/pexels-photo-1639557.jpeg?auto=compress&cs=tinysrgb&w=600'),
('Double Stack', 'Dois hambúrgueres, bacon crocante e molho especial.', 38.00, 'https://images.pexels.com/photos/2983101/pexels-photo-2983101.jpeg?auto=compress&cs=tinysrgb&w=600'),
('Veggie Script', 'Hambúrguer de grão de bico com salada fresca.', 30.00, 'https://images.pexels.com/photos/3219483/pexels-photo-3219483.jpeg?auto=compress&cs=tinysrgb&w=600'),
('Java Chicken', 'Frango empanado crocante com alface e maionese.', 28.00, 'https://images.pexels.com/photos/12034622/pexels-photo-12034622.jpeg'),
('Python Onion', 'Anéis de cebola, barbecue e queijo cheddar.', 33.00, 'https://images.pexels.com/photos/70497/pexels-photo-70497.jpeg?auto=compress&cs=tinysrgb&w=600'),
('React Salad', 'Uma opção leve e reativa para o seu almoço.', 27.00, 'https://images.pexels.com/photos/1199957/pexels-photo-1199957.jpeg?auto=compress&cs=tinysrgb&w=600');

SELECT * FROM usuario;

