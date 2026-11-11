create database if not exists Empresa;
use Empresa;

create table Clientes (
idCliente int primary key auto_increment,
nome varchar(100) not null,
data_nascimento date not null,
cidade varchar(100) not null
);

create table Produtos (
idProduto int primary key auto_increment,
nome varchar(100),
estoque int not null,
preco float not null
);

create table Pedidos (
idPedidos int primary key auto_increment,
id_cliente int,
id_produto int,
valor_total float,
quantidade int,
data_do_pedido date default current_timestamp,
foreign key (id_cliente) references Clientes(idcliente),
foreign key (id_produto) references Produtos(idproduto)
);

insert into Clientes (nome, data_nascimento, cidade)
values ('Ana', '2002-01-02', 'São Paulo'),
('Carlos', '1995-02-22', 'Rio de Janeiro'),
('João', '1987-01-05', 'Salvador');

select * from Clientes;

insert into Produtos (nome, estoque, preco)
values ('Mouse', 15, 20.00),
('Teclado', 50, 120.00),
('Monitor', 10, 700.00);

select * from Produtos;

insert into Pedidos (id_cliente, id_produto, valor_total, quantidade)
values (1, 1, 40.00, 2),
(2, 3,700.00 ,1);

select * from Pedidos;

create table teste(
idteste int primary key auto_increment);

drop table teste;

alter table Cliente
rename to Clientes;
show tables;

