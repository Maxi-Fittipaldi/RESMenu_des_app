/* RESMenu user*/
CREATE USER 'testing'@'localhost' IDENTIFIED BY '12345';
GRANT INSERT, SELECT, UPDATE, DELETE ON RESMenu.* TO 'testing'@'localhost';
