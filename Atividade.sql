create database if not exists LOCADORA2026;
use LOCADORA2026;

create table CARRO (
idCarro int primary key auto_increment,
placa varchar(45),
ano varchar(45),
cor varchar(45)
);

create table Clientes (
idClientes int primary key auto_increment,
nome varchar(100) not null,
CPF varchar(45),
datanascimento date
);

create table aluguel (
id_Carro int,
id_Clientes int,
dataaluguel varchar(45),
datafinal date,
foreign key(id_Carro) references CARRO(idCarro),
foreign key(id_Clientes) references Clientes(idClientes)
);

create table telefones(
idTelefones int primary key auto_increment,
numero varchar(45),
id_Clientes int,
foreign key(id_Clientes) references Clientes(idClientes)
);

alter table CARRO
modify placa varchar(12) not null unique;

alter table CARRO
add modelo varchar(100) not null;

alter table CARRO
modify ano year;

alter table CARRO
drop column modelo;

alter table aluguel
modify dataaluguel date not null;

 alter table aluguel
 add valor double;
 
 alter table Clientes
 modify CPF varchar(11) unique;
 
alter table Clientes
change datanascimento datadenascimento date;

alter table Clientes
add CNH varchar(100);

alter table telefones
add DDD int;

select * from CARRO;
select * from telefones;

describe aluguel;
describe Clientes;

show tables;

insert into CARRO (placa, ano, cor)
values ('thx-2999', 2005, 'Vermelho'),
('thx-2998', 1899, 'Azul'),
('thx-2997', 2026, 'Cinza'),
('thx-2996', 2007, 'Preto'),
('thx-2995', 2021, 'Marrom'),
('thx-2994', 2022, 'Verde'),
('thx-2993', 2006, 'Ciano'),
('thx-2992', 2023, 'Branco'),
('thx-2991', 2024, 'Verde-cana'),
('thx-2990', 2009, 'Azul-Marinho');

update CARRO
set ano = 2000
where idCarro = 2;
	
insert into Clientes (nome, CPF, datadenascimento, CNH)
values ('João', '11111111111', '1980-04-12', '121212121212'),
('Douglas', '22222222222', '1971-05-29', '212121212121'),
('Larissa', '33333333333', '2003-03-16', '23232323232332'),
('Manuela', '44444444444', '2005-11-22', '32323233223332'),
('Samira', '55555555555', '1999-12-14', '34343434343443'),
('Lucas', '66666666666', '2001-33-11', '434343433443434343');

insert into telefones (numero, ddd, id_Clientes) 
values ('912345678', '11', 1), ('998765432', '11', 1),
('934567890', '21', 2), ('987654321', '21', 2),
('945678901', '31', 3), ('956789012', '31', 3),
('967890123', '41', 4), ('978901234', '41', 4),
('989012345', '51', 5), ('990123456', '51', 5),
('901234567', '61', 6), ('912345678', '61', 6);

insert into aluguel (id_Carro, id_Clientes, dataaluguel, datafinal, valor) 
values (1, 1, '2021-01-10', '2021-01-15', 300.00),
(2, 2, '2021-02-12', '2021-02-20', 450.00),
(3, 3, '2021-03-05', '2021-03-10', 250.00),
(4, 4, '2021-04-01', '2021-04-07', 400.00),
(5, 5, '2021-05-10', '2021-05-15', 350.00),
(6, 6, '2021-06-18', '2021-06-25', 500.00),
(7, 1, '2021-07-10', '2021-07-12', 200.00),
(8, 2, '2021-08-15', '2021-08-20', 300.00),
(9, 3, '2021-09-05', '2021-09-12', 600.00),
(10, 4, '2021-10-01', '2021-10-05', 280.00);

delete from telefone
where ddd = '61';




