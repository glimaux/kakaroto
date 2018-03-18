
SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- Schema Kakaroto
CREATE SCHEMA IF NOT EXISTS `kkrt` DEFAULT CHARACTER SET utf8;
USE `kkrt`;

-- Table GitHub User
CREATE TABLE IF NOT EXISTS `kkrt`.`github_user` (
    `id` INT(11) NOT NULL,
    `login` VARCHAR(128) NOT NULL,
    `html_url` VARCHAR(128) NOT NULL,
    `created_at` DATETIME(3) NOT NULL,
    PRIMARY KEY (`id`),
    UNIQUE INDEX `UQ_login` (`login` ASC)
)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

-- Table Project
CREATE TABLE IF NOT EXISTS `kkrt`.`project` (
    `id` INT(11) NOT NULL,
    `number` INT(11) NOT NULL,
    `name` VARCHAR(128) NOT NULL,
    `description` VARCHAR(500),
    `html_url` VARCHAR(128) NOT NULL,
    `created_at` DATETIME(3) NOT NULL,
    `updated_at` DATETIME(3) NOT NULL,
    PRIMARY KEY (`id`)
)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

-- Table Board Column
CREATE TABLE IF NOT EXISTS `kkrt`.`board_column` (
    `id` INT(11) NOT NULL,
    `project_id` INT(11) NOT NULL,
    `name` VARCHAR(128) NOT NULL,
    `created_at` DATETIME(3) NOT NULL,
    `updated_at` DATETIME(3) NOT NULL,
    PRIMARY KEY (`id`),
    UNIQUE INDEX `UQ_name` (`name` ASC),
    CONSTRAINT `FK_project_board_column`
        FOREIGN KEY (`project_id`)
        REFERENCES `kkrt`.`project` (`id`)
        ON DELETE CASCADE
        ON UPDATE RESTRICT
)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

-- Table Card
CREATE TABLE IF NOT EXISTS `kkrt`.`card` (
    `id` INT(11) NOT NULL,
    `project_id` INT(11) NOT NULL,
    `note` VARCHAR(128),
    `created_at` DATETIME(3) NOT NULL,
    `updated_at` DATETIME(3) NOT NULL,
    `created_by` INT(11),
    PRIMARY KEY (`id`),
    CONSTRAINT `FK_project_card`
        FOREIGN KEY (`project_id`)
        REFERENCES `kkrt`.`project` (`id`)
        ON DELETE CASCADE
        ON UPDATE RESTRICT,
    CONSTRAINT `FK_user_card`
        FOREIGN KEY (`created_by`)
        REFERENCES `kkrt`.`github_user` (`id`)
        ON DELETE SET NULL
        ON UPDATE RESTRICT
)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

-- Table Board Column Card
CREATE TABLE IF NOT EXISTS `kkrt`.`board_column_card` (
    `id` INT(11) NOT NULL AUTO_INCREMENT,
    `board_column_id` INT(11) NOT NULL,
    `card_id` INT(11) NOT NULL,
    `placed_at` DATETIME(3) NOT NULL,
    `removed_at` DATETIME(3),
    PRIMARY KEY (`id`),
    INDEX `IX_placed_at` (`placed_at` ASC),
    INDEX `IX_removed_at` (`removed_at` ASC),
    CONSTRAINT `FK_board_column`
        FOREIGN KEY (`board_column_id`)
        REFERENCES `kkrt`.`board_column` (`id`)
        ON DELETE CASCADE
        ON UPDATE RESTRICT,
    CONSTRAINT `FK_card`
        FOREIGN KEY (`card_id`)
        REFERENCES `kkrt`.`card` (`id`)
        ON DELETE CASCADE
        ON UPDATE RESTRICT
)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

-- Table Issue
CREATE TABLE IF NOT EXISTS `kkrt`.`issue` (
    `id` INT(11) NOT NULL,
    `card_id` INT(11) NOT NULL,
    `number` INT(11) NOT NULL,
    `title` VARCHAR(500) NOT NULL,
    `state` VARCHAR(128) NOT NULL,
    `repository` VARCHAR(128) NOT NULL,
    `is_pull_request` BOOLEAN NOT NULL,
    `html_url` VARCHAR(128) NOT NULL,
    `created_at` DATETIME(3) NOT NULL,
    `updated_at` DATETIME(3) NOT NULL,
    `created_by` INT(11),
    PRIMARY KEY (`id`),
    CONSTRAINT `FK_card_issue`
        FOREIGN KEY (`card_id`)
        REFERENCES `kkrt`.`card` (`id`)
        ON DELETE CASCADE
        ON UPDATE RESTRICT,
    CONSTRAINT `FK_user_issue`
        FOREIGN KEY (`created_by`)
        REFERENCES `kkrt`.`github_user` (`id`)
        ON DELETE SET NULL
        ON UPDATE RESTRICT
)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

-- Table Issue Label
CREATE TABLE IF NOT EXISTS `kkrt`.`issue_label` (
    `id` INT(11) NOT NULL AUTO_INCREMENT,
    `label_id` INT(11) NOT NULL,
    `issue_id` INT(11) NOT NULL,
    `name` VARCHAR(128),
    `created_at` DATETIME(3) NOT NULL,
    PRIMARY KEY (`id`),
    INDEX `IX_name` (`name` ASC),
    INDEX `IX_label_id` (`label_id` ASC),
    CONSTRAINT `FK_issue_issue_label`
        FOREIGN KEY (`issue_id`)
        REFERENCES `kkrt`.`issue` (`id`)
        ON DELETE CASCADE
        ON UPDATE RESTRICT
)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

-- Table Issue Assignee
CREATE TABLE IF NOT EXISTS `kkrt`.`issue_assignee` (
    `issue_id` INT(11) NOT NULL,
    `assignee_id` INT(11) NOT NULL,
    PRIMARY KEY (`issue_id`, `assignee_id`),
    CONSTRAINT `FK_issue_issue_assignee`
        FOREIGN KEY (`issue_id`)
        REFERENCES `kkrt`.`issue` (`id`)
        ON DELETE CASCADE
        ON UPDATE RESTRICT,
    CONSTRAINT `FK_user_issue_assignee`
        FOREIGN KEY (`assignee_id`)
        REFERENCES `kkrt`.`github_user` (`id`)
        ON DELETE CASCADE
        ON UPDATE RESTRICT
)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
