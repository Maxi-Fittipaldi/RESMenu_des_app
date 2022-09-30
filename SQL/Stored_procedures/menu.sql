DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_insterdt`(IN `producto_id` INT, IN `uid` INT, IN `cantidad` INT)
    NO SQL
INSERT INTO detalleTransaccion
    VALUES((SELECT id
    FROM cabeceraTransaccion
    WHERE usuario_id = uid AND cabeceratransaccion.estado = "pendiente"),
    producto_id,
    cantidad,
    (SELECT precio FROM productos WHERE productos.id = producto_id),
    "pendiente",
    3,
    "Sin comentarios"
    )$$
DELIMITER ;

DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_insertct`(IN `uid` INT, IN `nm` INT, IN `e` ENUM('pendiente','cancelado','confirmado'))
    NO SQL
INSERT INTO
    cabeceraTransaccion (usuario_id,nro_mesa,estado)
    VALUES(uid, nm, e)$$
DELIMITER ;

DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_updatect`(IN `id` INT)
    NO SQL
UPDATE cabeceraTransaccion SET estado="cancelado" WHERE usuario_id = id AND estado="pendiente"$$
DELIMITER ;
