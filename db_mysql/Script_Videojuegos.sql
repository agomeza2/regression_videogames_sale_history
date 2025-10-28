CREATE DATABASE videojuegos;
USE videojuegos;

-- Tabla de Plataformas
CREATE TABLE Plataforma (
    id_plataforma INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL UNIQUE
);

-- Tabla de Editores
CREATE TABLE Editor (
    id_editor INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL UNIQUE
);



-- Tabla de Géneros
CREATE TABLE Genero (
    id_genero INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL UNIQUE
);

-- Tabla de Videojuegos
CREATE TABLE Videojuego (
    id_juego INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    anio INT,
    id_plataforma INT,
    id_editor INT,
    id_genero INT,
    FOREIGN KEY (id_plataforma) REFERENCES Plataforma(id_plataforma),
    FOREIGN KEY (id_editor) REFERENCES Editor(id_editor),
    FOREIGN KEY (id_genero) REFERENCES Genero(id_genero)
);

-- Tabla de Ventas
CREATE TABLE Venta (
    id_venta INT AUTO_INCREMENT PRIMARY KEY,
    id_juego INT,
    na_sales FLOAT,
    eu_sales FLOAT,
    jp_sales FLOAT,
    other_sales FLOAT,
    global_sales FLOAT,
    FOREIGN KEY (id_juego) REFERENCES Videojuego(id_juego)
);

SELECT * FROM  Videojuego;
SELECT * FROM  Venta;
SELECT * FROM  Plataforma;
SELECT * FROM  Editor;
SELECT * FROM  Genero;

SELECT * FROM Videojuego INNER JOIN Venta ;
