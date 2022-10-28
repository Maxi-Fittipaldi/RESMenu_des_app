DROP DATABASE IF EXISTS RESMenu;
CREATE DATABASE RESMenu;
USE RESMenu;
SET NAMES utf8;

CREATE TABLE usuarios (
    id INT(11) NOT NULL AUTO_INCREMENT,
    email VARCHAR(100) NOT NULL,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
    password VARCHAR(64) NOT NULL,
    estado ENUM("pendiente","verificado","terminado") DEFAULT "pendiente",
    rol ENUM("sin_rol","chef","cajero","admin") DEFAULT "sin_rol",
    PRIMARY KEY(id)
)ENGINE = InnoDB;

CREATE TABLE cabeceraTransaccion(
    id INT(11) NOT NULL AUTO_INCREMENT,
    cliente_id VARCHAR(64) NOT NULL,
    estado ENUM("completado","en_proceso","pendiente","cancelado") DEFAULT "pendiente",
    fecha datetime DEFAULT current_timestamp,
    PRIMARY KEY(id)
) ENGINE = InnoDB;

CREATE TABLE productos(
    id INT(11) NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(50) NOT NULL,
    descripcion VARCHAR(150) DEFAULT "Sin descripción",
    cantidad INT(5) NOT NULL,
    precio DOUBLE(11,2) NOT NULL,
    disponibilidad_desde TIME(3) NOT NULL,
    disponibilidad_hasta TIME(3) NOT NULL,
    propietario INT(11) NOT NULL,
    estado ENUM("visible","oculto") DEFAULT "visible",
    PRIMARY KEY(id),
    CONSTRAINT fk_propietario FOREIGN KEY(propietario)
    REFERENCES usuarios(id)
)ENGINE = InnoDB;

CREATE TABLE detalleTransaccion(
    cabecera_id INT(11) NOT NULL,
    producto_id INT(11) NOT NULL,
    cantidad INT(2) DEFAULT 1,
    monto DOUBLE(11,2) NOT NULL,
    estado VARCHAR(10) NOT NULL,
    PRIMARY KEY(cabecera_id, producto_id),
    CONSTRAINT fk_cabecera_id FOREIGN KEY(cabecera_id)
    REFERENCES cabeceraTransaccion(id),
    CONSTRAINT fk_producto_id FOREIGN KEY(producto_id)
    REFERENCES productos(id) ON DELETE CASCADE
)ENGINE = InnoDB;

CREATE TABLE locales(
    id INT(11) NOT NULL,
    nombre VARCHAR(50) NOT NULL,
    domicilio VARCHAR(15) NOT NULL,
    telefono INT(11) NOT NULL,
    PRIMARY KEY(id)
)ENGINE = InnoDB;

CREATE TABLE localesProductos(
    producto_id INT(11) NOT NULL AUTO_INCREMENT,
    local_id INT(11) NOT NULL,
    estado VARCHAR(10) NOT NULL,
    PRIMARY KEY (producto_id, local_id),
    CONSTRAINT fk_producto_idl FOREIGN KEY(producto_id)
    REFERENCES productos(id) ON DELETE CASCADE,
    CONSTRAINT fk_local_id FOREIGN KEY(local_id)
    REFERENCES locales(id)
)ENGINE = InnoDB;
