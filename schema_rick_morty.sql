SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema rick_morty
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema rick_morty
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `rick_morty` DEFAULT CHARACTER SET utf8 ;
-- -----------------------------------------------------
-- Schema project_rick_morty
-- -----------------------------------------------------
USE `rick_morty` ;

-- -----------------------------------------------------
-- Table `rick_morty`.`Character`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `rick_morty`.`Character` (
  `idCharacter` INT NOT NULL AUTO_INCREMENT,
  `Character_name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idCharacter`),
  UNIQUE INDEX `idCharacter_UNIQUE` (`idCharacter` ASC) VISIBLE,
  UNIQUE INDEX `Character_name_UNIQUE` (`Character_name` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `rick_morty`.`Episode`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `rick_morty`.`Episode` (
  `idEpisode` INT NOT NULL AUTO_INCREMENT,
  `Episode_name` VARCHAR(45) NULL,
  PRIMARY KEY (`idEpisode`),
  UNIQUE INDEX `idEpisode_UNIQUE` (`idEpisode` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `rick_morty`.`Phrase`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `rick_morty`.`Phrase` (
  `idPhrase` INT NOT NULL AUTO_INCREMENT,
  `Phrase` VARCHAR(5000) NOT NULL,
  `Character_idCharacter` INT NOT NULL,
  `Episode_idEpisode` INT NOT NULL,
  PRIMARY KEY (`idPhrase`),
  UNIQUE INDEX `idPhrase_UNIQUE` (`idPhrase` ASC) VISIBLE,
  INDEX `fk_Phrase_Character1_idx` (`Character_idCharacter` ASC) VISIBLE,
  INDEX `fk_Phrase_Episode1_idx` (`Episode_idEpisode` ASC) VISIBLE,
  CONSTRAINT `fk_Phrase_Character1`
    FOREIGN KEY (`Character_idCharacter`)
    REFERENCES `rick_morty`.`Character` (`idCharacter`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Phrase_Episode1`
    FOREIGN KEY (`Episode_idEpisode`)
    REFERENCES `rick_morty`.`Episode` (`idEpisode`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `rick_morty`.`Episode_has_Character`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `rick_morty`.`Episode_has_Character` (
  `Episode_idEpisode` INT NOT NULL,
  `Character_idCharacter` INT NOT NULL,
  PRIMARY KEY (`Episode_idEpisode`, `Character_idCharacter`),
  INDEX `fk_Episode_has_Character_Character1_idx` (`Character_idCharacter` ASC) VISIBLE,
  INDEX `fk_Episode_has_Character_Episode1_idx` (`Episode_idEpisode` ASC) VISIBLE,
  CONSTRAINT `fk_Episode_has_Character_Episode1`
    FOREIGN KEY (`Episode_idEpisode`)
    REFERENCES `rick_morty`.`Episode` (`idEpisode`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Episode_has_Character_Character1`
    FOREIGN KEY (`Character_idCharacter`)
    REFERENCES `rick_morty`.`Character` (`idCharacter`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
