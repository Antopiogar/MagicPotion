DROP DATABASE IF EXISTS magicPotion ;
CREATE DATABASE IF NOT EXISTS magicPotion ;
USE magicPotion ;

CREATE TABLE users (
	id int PRIMARY KEY AUTO_INCREMENT ,
    username varchar (25) NOT null,
    pass varchar (25) NOT null
);

CREATE TABLE potions (
	id int PRIMARY KEY AUTO_INCREMENT ,
    name varchar (25) NOT null unique
);

CREATE TABLE ingredients (
	id int PRIMARY KEY AUTO_INCREMENT ,
    name varchar (25) NOT null,
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
