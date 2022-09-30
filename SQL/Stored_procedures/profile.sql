DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_upadateusuario`(IN `n` VARCHAR(50), IN `a` VARCHAR(50), IN `pw` VARCHAR(64), IN `id` INT)
    NO SQL
UPDATE `usuarios` SET usuarios.nombre= n, usuarios.apellido= a, password= pw WHERE usuarios.id = id$$
DELIMITER ;