-- create initial content
CREATE DATABASE IF NOT EXISTS tyrell_corp;
USE tyrell_corp;
CREATE TABLE IF NOT EXISTS `nexus6`
(id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
name VARCHAR(30));
INSERT INTO `nexus6` (`name`) VALUES("Juancho");
GRANT SELECT ON `tyrell_corp`.`nexus6` TO 'holberton_user'@'localhost';
