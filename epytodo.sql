-- MariaDB dump 10.17  Distrib 10.4.12-MariaDB, for Linux (x86_64)
--
-- Host: localhost    Database: epytodo
-- ------------------------------------------------------
-- Server version	10.4.12-MariaDB

CREATE DATABASE IF NOT EXISTS `epytodo`;

USE `epytodo`;

CREATE TABLE `task` (
  `task_id` int NOT NULL PRIMARY KEY AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `begin` datetime DEFAULT CURRENT_TIMESTAMP NOT NULL,
  `end` datetime DEFAULT NULL,
  `status` varchar(12) DEFAULT 'not started' NOT NULL,
  CONSTRAINT `CONSTRAINT_1` CHECK (`status` = 'not started' or `status` = 'in progress' or `status` = 'done')
);

CREATE TABLE `user` (
  `user_id` int NOT NULL PRIMARY KEY AUTO_INCREMENT,
  `username` char(255) NOT NULL,
  `password` char(255) NOT NULL
);

CREATE TABLE `user_has_task` (
  `fk_user_id` int DEFAULT NULL,
  `fk_task_id` int DEFAULT NULL
);