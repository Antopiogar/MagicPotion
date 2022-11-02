DROP DATABASE IF EXISTS magicPotion ;
CREATE DATABASE IF NOT EXISTS magicPotion ;
USE magicPotion ;

CREATE TABLE users (
	id int PRIMARY KEY AUTO_INCREMENT ,
    username varchar (25) NOT null,
    pass varchar (25) NOT null,
    isAdmin BOOLEAN NOT null
);

CREATE TABLE potions (
	id int PRIMARY KEY AUTO_INCREMENT ,
    nome varchar (25) NOT null
);

CREATE TABLE ingredients (
	id int PRIMARY KEY AUTO_INCREMENT ,
    nome varchar (25) NOT null,
    fire int not null,
    air int not null,
    water int not null,
    earth int not null
);

CREATE TABLE pozioni_ingredienti (
    fk_potions int NOT null ,
    fk_ingredients int NOT null ,
    FOREIGN KEY (fk_potions) REFERENCES potions(id),
    FOREIGN KEY (fk_ingredients) REFERENCES ingredients(id),
    PRIMARY KEY (fk_potions,fk_ingredients) 
);

INSERT INTO `ingredients`( `name`, `fire`, `air`, `water`, `earth`) VALUES (
    ('Pescepalla',4,7,99,0),
    ('Occhio di ragno',0,12,37,3),
    ('Ram di Inf2',99,99,12,0),
    ('Piede di coniglio',0,37,58,33),
    ('polvere di Luminite',29,69,70,99),
    ('Anima di Admin',99,99,99,99),
    ('marmellata dimenticata nel frigo da un anno',0,69,99,40)
   )