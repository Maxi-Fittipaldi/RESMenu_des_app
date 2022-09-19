-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 06-06-2022 a las 16:26:21
-- Versión del servidor: 10.4.24-MariaDB
-- Versión de PHP: 8.1.6

SET FOREIGN_KEY_CHECKS=0;
SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `resmenu`
--
CREATE DATABASE IF NOT EXISTS `resmenu` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `resmenu`;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cabeceratransaccion`
--

DROP TABLE IF EXISTS `cabeceratransaccion`;
CREATE TABLE `cabeceratransaccion` (
  `id` int(11) NOT NULL,
  `usuario_id` int(11) NOT NULL,
  `nro_mesa` int(3) NOT NULL,
  `fecha` date NOT NULL,
  `estado` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `detalletransaccion`
--

DROP TABLE IF EXISTS `detalletransaccion`;
CREATE TABLE `detalletransaccion` (
  `cabecera_id` int(11) NOT NULL,
  `producto_id` int(11) NOT NULL,
  `cantidad` int(2) NOT NULL,
  `monto` double(11,2) NOT NULL,
  `estado` varchar(10) NOT NULL,
  `ranking` int(1) DEFAULT 5,
  `comentarios` varchar(150) DEFAULT 'No se ofrecieron comentarios'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `locales`
--

DROP TABLE IF EXISTS `locales`;
CREATE TABLE `locales` (
  `id` int(11) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `domicilio` varchar(15) NOT NULL,
  `telefono` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `localesproductos`
--

DROP TABLE IF EXISTS `localesproductos`;
CREATE TABLE `localesproductos` (
  `producto_id` int(11) NOT NULL,
  `local_id` int(11) NOT NULL,
  `estado` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `productos`
--

DROP TABLE IF EXISTS `productos`;
CREATE TABLE `productos` (
  `id` int(11) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `descripcion` varchar(150) DEFAULT 'Sin descripción',
  `precio` double(11,2) NOT NULL,
  `disponibilidad_desde` time(3) NOT NULL,
  `disponibilidad_hasta` time(3) NOT NULL,
  `propietario` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
CREATE TABLE `usuarios` (
  `id` int(11) NOT NULL,
  `gmail` varchar(100) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `apellido` varchar(50) NOT NULL,
  `password` varchar(64) NOT NULL,
  `estado` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`id`, `gmail`, `nombre`, `apellido`, `password`, `estado`) VALUES
(43, 'a.abril.tarrago@schonthal.esc.edu.ar', 'Abril Micaela', 'Tarrago', '123456', 'activo'),
(44, 'a.avril.lopez@schonthal.esc.edu.ar', 'Avril', 'Lopez Rodriguez', '123456', 'activo'),
(45, 'a.bautista.barrientos@schonthal.esc.edu.ar', 'Bautista', 'Barrientos', '123456', 'activo'),
(46, 'a.camila.arias@schonthal.esc.edu.ar', 'Camila Belén', 'Arias', '123456', 'activo'),
(47, 'a.candela.scillone@schonthal.esc.edu.ar', 'Candela Sofía', 'Scillone Paszkowski', '123456', 'activo'),
(48, 'a.catalina.mendez@schonthal.esc.edu.ar', 'Catalina', 'Mendez', '123456', 'activo'),
(49, 'a.constanza.martinez@schonthal.esc.edu.ar', 'Constanza', 'Martinez', '123456', 'activo'),
(50, 'a.delfina.cassani@schonthal.esc.edu.ar', 'Delfina', 'Cassani', '123456', 'activo'),
(51, 'a.fabrizio.amoroso@schonthal.esc.edu.ar', 'Fabrizio', 'Amoroso', '123456', 'activo'),
(52, 'a.facundo.reschini@schonthal.esc.edu.ar', 'Facundo', 'Reschini', '123456', 'activo'),
(53, 'a.facundo.nardi@schonthal.esc.edu.ar', 'Facundo Marco', 'Nardi', '123456', 'activo'),
(54, 'a.federico.evolo@schonthal.esc.edu.ar', 'Federico Martín', 'Evolo', '123456', 'activo'),
(55, 'a.federico.cancelleri@schonthal.esc.edu.ar', 'Federico Pablo', 'Cancelleri', '123456', 'activo'),
(56, 'a.federico.leguizamo@schonthal.esc.edu.ar', 'Federico Pablo', 'Leguizamo', '123456', 'activo'),
(57, 'a.felipe.robles@schonthal.esc.edu.ar', 'Felipe Agustin', 'Robles', '123456', 'activo'),
(58, 'a.florencia.greco@schonthal.esc.edu.ar', 'Florencia Pilar', 'Greco Rolandelli', '123456', 'activo'),
(59, 'a.giulia.lavalle@schonthal.esc.edu.ar', 'Giulia Emma', 'La Valle Tosoni', '123456', 'activo'),
(60, 'a.juan.fernandez@schonthal.esc.edu.ar', 'Juan Ignacio', 'Fernandez', '123456', 'activo'),
(61, 'a.julieta.orda@schonthal.esc.edu.ar', 'Julieta Belén', 'Orda', '123456', 'activo'),
(62, 'a.lucciano.cusinato@schonthal.esc.edu.ar', 'Lucciano Augusto', 'Cusinato', '123456', 'activo'),
(63, 'a.luciano.carini@schonthal.esc.edu.ar', 'Luciano Nahuel', 'Carini', '123456', 'activo'),
(64, 'a.malena.nigro@schonthal.esc.edu.ar', 'Malena Sofía', 'Nigro', '123456', 'activo'),
(65, 'a.manuel.elostondo@schonthal.esc.edu.ar', 'Manuel Facundo', 'Elostondo', '123456', 'activo'),
(66, 'a.mariajulieta.roman@schonthal.esc.edu.ar', 'Maria Julieta', 'Roman', '123456', 'activo'),
(67, 'a.martina.rosenbrock@schonthal.esc.edu.ar', 'Martina', 'Rosenbrock', '123456', 'activo'),
(68, 'a.mariadelrosario.hernandez@schonthal.esc.edu.ar', 'María Del Rosario', 'Hernandez', '123456', 'activo'),
(69, 'a.maximiliano.rivera@schonthal.esc.edu.ar', 'Maximiliano', 'Rivera', '123456', 'activo'),
(70, 'a.melany.kamis@schonthal.esc.edu.ar', 'Melany', 'Kamis', '123456', 'activo'),
(71, 'a.micaela.landro@schonthal.esc.edu.ar', 'Micaela', 'Landro', '123456', 'activo'),
(72, 'a.micaela.gebel@schonthal.esc.edu.ar', 'Micaela Abril', 'Gebel', '123456', 'activo'),
(73, 'a.mirko.herschel@schonthal.esc.edu.ar', 'Mirko Joaquín', 'Herschel Butula', '123456', 'activo'),
(74, 'a.morena.rabascall@schonthal.esc.edu.ar', 'Morena', 'Rabascall', '123456', 'activo'),
(75, 'a.nicolas.lopezdearmentia@schonthal.esc.edu.ar', 'Nicolás Galo', 'Lopez De Armentía', '123456', 'activo'),
(76, 'a.ornella.fortino@schonthal.esc.edu.ar', 'Ornella Bryanna', 'Fortino', '123456', 'activo'),
(77, 'a.pilar.costa@schonthal.esc.edu.ar', 'Pilar', 'Costa Vigo', '123456', 'activo'),
(78, 'a.ramiro.kalerguiz@schonthal.esc.edu.ar', 'Ramiro Damián', 'Kalerguiz', '123456', 'activo'),
(79, 'a.selena.perez@schonthal.esc.edu.ar', 'Selena Julieta', 'Perez Paz', '123456', 'activo'),
(80, 'a.sofia.agustini@schonthal.esc.edu.ar', 'Sofia Malena', 'Agustini', '123456', 'activo'),
(81, 'a.sol.corbellini@schonthal.esc.edu.ar', 'Sol', 'Corbellini', '123456', 'activo'),
(82, 'a.thomas.baron@schonthal.esc.edu.ar', 'Thomás André', 'Baron Diaz', '123456', 'activo'),
(83, 'a.yeres.chaar@schonthal.esc.edu.ar', 'Yeres', 'Chaar', '123456', 'activo');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `cabeceratransaccion`
--
ALTER TABLE `cabeceratransaccion`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_usuario_id` (`usuario_id`);

--
-- Indices de la tabla `detalletransaccion`
--
ALTER TABLE `detalletransaccion`
  ADD PRIMARY KEY (`cabecera_id`,`producto_id`),
  ADD KEY `fk_producto_id` (`producto_id`);

--
-- Indices de la tabla `locales`
--
ALTER TABLE `locales`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `localesproductos`
--
ALTER TABLE `localesproductos`
  ADD PRIMARY KEY (`producto_id`,`local_id`),
  ADD KEY `fk_local_id` (`local_id`);

--
-- Indices de la tabla `productos`
--
ALTER TABLE `productos`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_propietario` (`propietario`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `cabeceratransaccion`
--
ALTER TABLE `cabeceratransaccion`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `localesproductos`
--
ALTER TABLE `localesproductos`
  MODIFY `producto_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `productos`
--
ALTER TABLE `productos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=84;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `cabeceratransaccion`
--
ALTER TABLE `cabeceratransaccion`
  ADD CONSTRAINT `fk_usuario_id` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios` (`id`);

--
-- Filtros para la tabla `detalletransaccion`
--
ALTER TABLE `detalletransaccion`
  ADD CONSTRAINT `fk_cabecera_id` FOREIGN KEY (`cabecera_id`) REFERENCES `cabeceratransaccion` (`id`),
  ADD CONSTRAINT `fk_producto_id` FOREIGN KEY (`producto_id`) REFERENCES `productos` (`id`);

--
-- Filtros para la tabla `localesproductos`
--
ALTER TABLE `localesproductos`
  ADD CONSTRAINT `fk_local_id` FOREIGN KEY (`local_id`) REFERENCES `locales` (`id`),
  ADD CONSTRAINT `fk_producto_idl` FOREIGN KEY (`producto_id`) REFERENCES `productos` (`id`);

--
-- Filtros para la tabla `productos`
--
ALTER TABLE `productos`
  ADD CONSTRAINT `fk_propietario` FOREIGN KEY (`propietario`) REFERENCES `usuarios` (`id`);
SET FOREIGN_KEY_CHECKS=1;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
