DROP DATABASE IF EXISTS RESMenu;
CREATE DATABASE RESMenu;
USE RESMenu;
SET utf8;

CREATE TABLE usuarios ( 
    id INT(11) NOT NULL,
    gmail VARCHAR(100) NOT NULL,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
    password VARCHAR(50) NOT NULL,
    estado VARCHAR(10) NOT NULL,
    PRIMARY KEY(id)
)ENGINE = InnoDB;  

CREATE TABLE cabeceraTransaccion(
    id INT(11) NOT NULL,
    usuario_id INT(11) NOT NULL,
    fecha date NOT NULL,
    estado VARCHAR(10) NOT NULL,
    PRIMARY KEY(id),
    CONSTRAINT fk_usuario_id FOREIGN KEY (usuario_id)
    REFERENCES usuarios(id)
) ENGINE = InnoDB;

CREATE TABLE productos(
    id INT(11) NOT NULL,
    nombre VARCHAR(50) NOT NULL,
    descripcion VARCHAR(150) DEFAULT "Sin descripción",
    precio DOUBLE(11,2) NOT NULL,
)ENGINE = InnoDB;

CREATE TABLE detalleTRansaccion(
    cabecera_id INT(11) NOT NULL,
    producto_id INT(11) NOT NULL,
    cantidad INT(2) NOT NULL,
    monto DOUBLE(11,2) NOT NULL,
    estado VARCHAR(10) NOT NULL,
    ranking INT(1) DEFAULT 5,
    comentarios VARCHAR(150) DEFAULT "No se ofrecieron comentarios",
    PRIMARY KEY(cabecera_id,producto_id),
    CONSTRAINT fk_cabecera_id FOREIGN KEY(cabecera_id)
    REFERENCES cabeceraTransaccion(id),
    CONSTRAINT fk_producto_id FOREIGN KEY(producto_id)
    REFERENCES productos(id)
)ENGINE = InnoDB;