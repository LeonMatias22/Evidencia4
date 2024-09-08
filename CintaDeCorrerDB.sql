create database Cinta_de_correrDB

use Cinta_de_correrDB

create table marcas(
	id_marca int not null auto_increment primary key,
    nombre varchar(20) not null
);

create table modelos(
	id_modelo int not null auto_increment primary key,
    nombre varchar(20) not null,
    motor varchar(10),
    peso_maximo_soportado int,
    niveles_de_inclincacion int,
    velocidad_maxima int
); 

create table cintas_de_correr(
	id_cinta int not null auto_increment primary key,
    id_marca int not null,
    id_modelo int not null,
    foreign key(id_marca) references marcas(id_marca),
	foreign key(id_modelo) references modelos(id_modelo)
);

insert into marcas(nombre)
values ("Bringeri"),
	   ("NordiTrack");
       
insert into modelos(nombre, motor, peso_maximo_soportado, niveles_de_inclincacion, velocidad_maxima)
values ("RANDER 320", "1.5 HP", 120, 3, 22),
	   ("RANDER 2500 MaxRUN", "1.3 HP", 91, 3, 20),
       ("Run Dev 005", "1.5 HP", 100, 4, 24),
       ("Run Dev 2024", "1.3 HP", 90, 1, 20);
       
alter table cintas_de_correr
add sucursal varchar(50);
       
insert into cintas_de_correr(id_marca, id_modelo, sucursal)
values (1, 2, "Sucursal 1"),
       (1, 2, "Sucursal 2"),
       (1, 1, "sucursal 1"),
       (2, 4, "Sucursal 3"),
       (2, 3, "sucursal 1");
       
select * from marcas
select * from modelos
select * from cintas_de_correr

select cintas_de_correr.id_cinta,
	  cintas_de_correr.sucursal,
	   marcas.nombre,
       modelos.nombre
from cintas_de_correr 
join marcas on cintas_de_correr.id_marca = marcas.id_marca
join modelos on cintas_de_correr.id_modelo = modelos.id_modelo
where cintas_de_correr.id_cinta = 1

select cintas_de_correr.id_cinta,
	  cintas_de_correr.sucursal,
	   marcas.nombre,
       modelos.nombre,
       modelos.motor,
       modelos.velocidad_maxima,
       modelos.peso_maximo_soportado
from cintas_de_correr 
join marcas on cintas_de_correr.id_marca = marcas.id_marca
join modelos on cintas_de_correr.id_modelo = modelos.id_modelo
where cintas_de_correr.id_cinta = 2