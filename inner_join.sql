create database if not exists clinica;
use clinica;

create table medicos (
idmedico int primary key auto_increment,
nomem varchar(100) not null,
idade int not null,
turno varchar(100) not null
);

create table pacientes (
idpaciente int primary key auto_increment,
nomep varchar(100) not null,
cpf varchar(45) not null
);

create table consulta (
idconsulta int primary key auto_increment,
medico_id int,
paciente_id int,
dataconsulta date,
foreign key (medico_id) references medicos(idmedico),
foreign key (paciente_id) references pacientes(idpaciente)
);

show tables;

insert into medicos (nomem,idade,turno)
values ('carlos',35,'noturno'),
('João',25,'matutino'),
('Sophia',28,'vespertino');

select * from medicos;

insert into pacientes (nomep, cpf)
values ('Edieno','1564564'),
('Lucas','56465');

insert into pacientes (nomep, cpf)
values ('Edieno','1564564'),
('Lucas','56465');
select * from pacientes;

insert into consulta (medico_id,paciente_id,dataconsulta)
values (1,2,'2026-05-02'),
(2,3,'2025-05-06'),
(3,1,'2026-01-03');


delete from pacientes
where idpaciente = '4';

create table teste (
idteste int primary key auto_increment
);

drop table teste;

select nomem,idade,turno from
medicos
order by nomem asc;

select nomep,cpf from
pacientes
order by nomep desc;

alter table consulta
add column valor decimal(10,2);

update consulta
set valor = 180.00
where idconsulta = 3;

insert into consulta (medico_id,paciente_id,dataconsulta,valor)
values (1,2,'2026-11-18',150);

select m.nomem as medicos,
count(c.idconsulta) as Total_consulta
from medicos m inner join consulta c on
m.idmedico = c.medico_id group by m.nomem;

select m.nomem as medicos,
avg(c.valor) as media_valores
from medicos m inner join consulta c on
m.idmedico = c.medico_id group by m.nomem;

select * from pacientes;

select p.nomep as pacientes,
count(c.idconsulta) as Total_consulta
from pacientes p inner join consulta c on
p.idpaciente = c.paciente_id group by p.nomep;

alter table pacientes
add column idade int not null;

update pacientes
set idade = 26
where idpaciente = 2;

select p.nomep as pacientes,
avg(p.idade) as Media_idade
from pacientes p inner join consulta c on
p.idpaciente = paciente_id group by p.nomep;                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   