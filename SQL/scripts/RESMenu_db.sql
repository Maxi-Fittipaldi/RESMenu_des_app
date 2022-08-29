DROP DATABASE IF EXISTS RESMenu;
CREATE DATABASE RESMenu;
USE RESMenu;
SET NAMES utf8;

CREATE TABLE usuarios (
    id INT(11) NOT NULL AUTO_INCREMENT,
    gmail VARCHAR(100) NOT NULL,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
    password VARCHAR(64) NOT NULL,
    estado ENUM("pendiente","verificado","terminado") DEFAULT "pendiente",
    rol ENUM("cliente","staff","admin") DEFAULT "cliente",
    PRIMARY KEY(id)
)ENGINE = InnoDB;

CREATE TABLE cabeceraTransaccion(
    id INT(11) NOT NULL AUTO_INCREMENT,
    usuario_id INT(11) NOT NULL,
    nro_mesa INT(3) NOT NULL,
    estado ENUM("completado","pendiente","cancelado") DEFAULT "pendiente",
    fecha datetime DEFAULT current_timestamp,
    PRIMARY KEY(id),
    CONSTRAINT fk_usuario_id FOREIGN KEY (usuario_id)
    REFERENCES usuarios(id)
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
    PRIMARY KEY(id),
    CONSTRAINT fk_propietario FOREIGN KEY(propietario)
    REFERENCES usuarios(id)
)ENGINE = InnoDB;

CREATE TABLE detalleTransaccion(
    cabecera_id INT(11) NOT NULL,
    producto_id INT(11) NOT NULL,
    cantidad INT(2) NOT NULL,
    monto DOUBLE(11,2) NOT NULL,
    estado VARCHAR(10) NOT NULL,
    ranking INT(1) DEFAULT 5,
    comentarios VARCHAR(150) DEFAULT "No se ofrecieron comentarios",
    PRIMARY KEY(cabecera_id, producto_id),
    CONSTRAINT fk_cabecera_id FOREIGN KEY(cabecera_id)
    REFERENCES cabeceraTransaccion(id),
    CONSTRAINT fk_producto_id FOREIGN KEY(producto_id)
    REFERENCES productos(id)
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
    REFERENCES productos(id),
    CONSTRAINT fk_local_id FOREIGN KEY(local_id)
    REFERENCES locales(id)
)ENGINE = InnoDB;
