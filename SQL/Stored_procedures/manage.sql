DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_instertproductos`(IN `n` VARCHAR(50), IN `p` DOUBLE, IN `c` INT, IN `d` VARCHAR(150), IN `dd` TIME, IN `dh` TIME, IN `prop` INT)
    NO SQL
INSERT INTO productos (productos.nombre,productos.precio,productos.cantidad, productos.descripcion, productos.disponibilidad_desde, productos.disponibilidad_hasta,productos.propietario) VALUES(n,p,c,d,dd,dh,prop)$$
DELIMITER ;

DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_selectproducts`(IN `nombre` INT(50))
SELECT * FROM productos WHERE productos.nombre = nombre$$
DELIMITER ;

DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_ocultarproducto`(IN `id` INT)
    NO SQL
UPDATE productos SET productos.estado ='oculto' WHERE productos.id = id$$
DELIMITER ;

DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_updateproductos`(IN `n` VARCHAR(50), IN `p` DOUBLE, IN `d` VARCHAR(150), IN `c` INT, IN `dd` TIME, IN `dh` TIME, IN `id` INT)
    NO SQL
UPDATE productos SET nombre= n , precio= p, descripcion = d, cantidad = c, disponibilidad_desde = dd, disponibilidad_hasta = dh WHERE id = id$$
DELIMITER ;

DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_deleteproductooculto`(IN `id` INT)
    NO SQL
DELETE FROM productos WHERE productos.estado='oculto' AND productos.id = id$$
DELIMITER ;

DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_visibleproducto`(IN `id` INT)
    NO SQL
UPDATE productos SET productos.estado='visible' WHERE productos.id = id$$
DELIMITER ;
