-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema flask_login_reg
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `flask_login_reg` ;

-- -----------------------------------------------------
-- Schema flask_login_reg
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `flask_login_reg` DEFAULT CHARACTER SET utf8 ;
USE `flask_login_reg` ;

-- -----------------------------------------------------
-- Table `flask_login_reg`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `flask_login_reg`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NOT NULL,
  `last_name` VARCHAR(45) NOT NULL,
  `email_address` VARCHAR(45) NOT NULL,
  `password` CHAR(60) NOT NULL,
  `created` DATETIME NOT NULL DEFAULT NOW(),
  `modified` DATETIME NOT NULL DEFAULT NOW() ON UPDATE NOW(),
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
