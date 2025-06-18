-- MySQL dump 10.13  Distrib 8.0.42, for Win64 (x86_64)
--
-- Host: localhost    Database: biogenetic
-- ------------------------------------------------------
-- Server version	9.3.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `alembic_version`
--

DROP TABLE IF EXISTS `alembic_version`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL,
  PRIMARY KEY (`version_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alembic_version`
--

LOCK TABLES `alembic_version` WRITE;
/*!40000 ALTER TABLE `alembic_version` DISABLE KEYS */;
/*!40000 ALTER TABLE `alembic_version` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bulls`
--

DROP TABLE IF EXISTS `bulls`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bulls` (
  `name` varchar(100) NOT NULL,
  `register` varchar(50) DEFAULT NULL,
  `race_id` int NOT NULL,
  `sex_id` int NOT NULL,
  `status` enum('active','inactive') NOT NULL,
  `user_id` int NOT NULL,
  `id` int NOT NULL AUTO_INCREMENT,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `lote` varchar(100) DEFAULT NULL,
  `escalerilla` varchar(100) DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ix_bulls_register` (`register`),
  KEY `race_id` (`race_id`),
  KEY `sex_id` (`sex_id`),
  KEY `user_id` (`user_id`),
  KEY `ix_bulls_id` (`id`),
  CONSTRAINT `bulls_ibfk_1` FOREIGN KEY (`race_id`) REFERENCES `races` (`id`),
  CONSTRAINT `bulls_ibfk_2` FOREIGN KEY (`sex_id`) REFERENCES `sexes` (`id`),
  CONSTRAINT `bulls_ibfk_3` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bulls`
--

LOCK TABLES `bulls` WRITE;
/*!40000 ALTER TABLE `bulls` DISABLE KEYS */;
/*!40000 ALTER TABLE `bulls` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `inputs`
--

DROP TABLE IF EXISTS `inputs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `inputs` (
  `quantity_received` decimal(10,2) NOT NULL,
  `escalarilla` varchar(100) NOT NULL,
  `bull_id` int NOT NULL,
  `status_id` enum('pending','processing','completed','cancelled') NOT NULL,
  `lote` varchar(50) NOT NULL,
  `fv` datetime NOT NULL,
  `quantity_taken` decimal(10,2) NOT NULL,
  `total` decimal(10,2) NOT NULL,
  `user_id` int NOT NULL,
  `id` int NOT NULL AUTO_INCREMENT,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `bull_id` (`bull_id`),
  KEY `user_id` (`user_id`),
  KEY `ix_inputs_id` (`id`),
  CONSTRAINT `inputs_ibfk_1` FOREIGN KEY (`bull_id`) REFERENCES `bulls` (`id`),
  CONSTRAINT `inputs_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inputs`
--

LOCK TABLES `inputs` WRITE;
/*!40000 ALTER TABLE `inputs` DISABLE KEYS */;
/*!40000 ALTER TABLE `inputs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `opus`
--

DROP TABLE IF EXISTS `opus`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `opus` (
  `id` int NOT NULL AUTO_INCREMENT,
  `cliente_id` int NOT NULL,
  `donante_id` int DEFAULT NULL,
  `fecha` date NOT NULL,
  `toro` varchar(100) NOT NULL,
  `gi` int NOT NULL,
  `gii` int NOT NULL,
  `giii` int NOT NULL,
  `viables` int NOT NULL,
  `otros` int NOT NULL,
  `total_oocitos` int NOT NULL,
  `ctv` int NOT NULL,
  `clivados` int NOT NULL,
  `porcentaje_cliv` varchar(10) NOT NULL,
  `prevision` int NOT NULL,
  `porcentaje_prevision` varchar(10) NOT NULL,
  `empaque` int NOT NULL,
  `porcentaje_empaque` varchar(10) NOT NULL,
  `vt_dt` int DEFAULT NULL,
  `porcentaje_vtdt` varchar(10) DEFAULT NULL,
  `total_embriones` int NOT NULL,
  `porcentaje_total_embriones` varchar(10) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `toro_id` int NOT NULL,
  `lugar` varchar(100) DEFAULT NULL,
  `finca` varchar(100) DEFAULT NULL,
  `race` varchar(50) NOT NULL,
  `donante_code` varchar(100) NOT NULL,
  `produccion_embrionaria_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `cliente_id` (`cliente_id`),
  KEY `donante_id` (`donante_id`),
  KEY `ix_opus_id` (`id`),
  KEY `fk_opus_toro_id_bulls` (`toro_id`),
  KEY `produccion_embrionaria_id` (`produccion_embrionaria_id`),
  CONSTRAINT `fk_opus_toro_id_bulls` FOREIGN KEY (`toro_id`) REFERENCES `bulls` (`id`),
  CONSTRAINT `opus_ibfk_1` FOREIGN KEY (`cliente_id`) REFERENCES `users` (`id`),
  CONSTRAINT `opus_ibfk_2` FOREIGN KEY (`donante_id`) REFERENCES `bulls` (`id`),
  CONSTRAINT `opus_ibfk_3` FOREIGN KEY (`produccion_embrionaria_id`) REFERENCES `produccion_embrionaria` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `opus`
--

LOCK TABLES `opus` WRITE;
/*!40000 ALTER TABLE `opus` DISABLE KEYS */;
/*!40000 ALTER TABLE `opus` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `outputs`
--

DROP TABLE IF EXISTS `outputs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `outputs` (
  `input_id` int NOT NULL,
  `output_date` datetime NOT NULL,
  `quantity_output` decimal(10,2) NOT NULL,
  `remark` text,
  `id` int NOT NULL AUTO_INCREMENT,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `input_id` (`input_id`),
  KEY `ix_outputs_id` (`id`),
  CONSTRAINT `outputs_ibfk_1` FOREIGN KEY (`input_id`) REFERENCES `inputs` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `outputs`
--

LOCK TABLES `outputs` WRITE;
/*!40000 ALTER TABLE `outputs` DISABLE KEYS */;
/*!40000 ALTER TABLE `outputs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `produccion_embrionaria`
--

DROP TABLE IF EXISTS `produccion_embrionaria`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `produccion_embrionaria` (
  `id` int NOT NULL AUTO_INCREMENT,
  `cliente_id` int NOT NULL,
  `fecha_opu` date NOT NULL,
  `lugar` varchar(100) NOT NULL,
  `hora_inicio` time DEFAULT NULL,
  `hora_final` time DEFAULT NULL,
  `envase` varchar(100) NOT NULL,
  `fecha_transferencia` date NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `finca` varchar(100) NOT NULL,
  `output_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `cliente_id` (`cliente_id`),
  KEY `ix_produccion_embrionaria_id` (`id`),
  CONSTRAINT `produccion_embrionaria_ibfk_1` FOREIGN KEY (`cliente_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `produccion_embrionaria`
--

LOCK TABLES `produccion_embrionaria` WRITE;
/*!40000 ALTER TABLE `produccion_embrionaria` DISABLE KEYS */;
/*!40000 ALTER TABLE `produccion_embrionaria` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `races`
--

DROP TABLE IF EXISTS `races`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `races` (
  `name` varchar(100) NOT NULL,
  `description` varchar(255) DEFAULT NULL,
  `code` varchar(10) NOT NULL,
  `id` int NOT NULL AUTO_INCREMENT,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ix_races_code` (`code`),
  KEY `ix_races_id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `races`
--

LOCK TABLES `races` WRITE;
/*!40000 ALTER TABLE `races` DISABLE KEYS */;
/*!40000 ALTER TABLE `races` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `role_user`
--

DROP TABLE IF EXISTS `role_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `role_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `role_id` int NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `role_id` (`role_id`),
  KEY `user_id` (`user_id`),
  KEY `ix_role_user_id` (`id`),
  CONSTRAINT `role_user_ibfk_1` FOREIGN KEY (`role_id`) REFERENCES `roles` (`id`),
  CONSTRAINT `role_user_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `role_user`
--

LOCK TABLES `role_user` WRITE;
/*!40000 ALTER TABLE `role_user` DISABLE KEYS */;
INSERT INTO `role_user` VALUES (1,1,1,'2025-05-27 14:22:05','2025-05-27 14:22:05'),(2,2,2,'2025-05-27 14:22:05','2025-05-27 14:22:05'),(3,3,3,'2025-05-27 14:22:06','2025-05-27 14:22:06'),(4,4,1,'2025-06-10 13:55:28','2025-06-10 13:55:28'),(6,5,2,'2025-06-10 14:03:01','2025-06-10 14:03:01'),(7,6,3,'2025-06-10 14:53:15','2025-06-10 14:53:15'),(8,7,3,'2025-06-10 14:58:40','2025-06-10 14:58:40');
/*!40000 ALTER TABLE `role_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `roles`
--

DROP TABLE IF EXISTS `roles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `roles` (
  `name` varchar(50) NOT NULL,
  `id` int NOT NULL AUTO_INCREMENT,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ix_roles_name` (`name`),
  KEY `ix_roles_id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `roles`
--

LOCK TABLES `roles` WRITE;
/*!40000 ALTER TABLE `roles` DISABLE KEYS */;
INSERT INTO `roles` VALUES ('Admin',1,'2025-05-27 14:22:05','2025-05-27 14:22:05'),('Veterinario',2,'2025-05-27 14:22:05','2025-05-27 14:22:05'),('Client',3,'2025-05-27 14:22:05','2025-05-27 14:22:05');
/*!40000 ALTER TABLE `roles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sexes`
--

DROP TABLE IF EXISTS `sexes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sexes` (
  `name` varchar(50) NOT NULL,
  `code` int NOT NULL,
  `id` int NOT NULL AUTO_INCREMENT,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ix_sexes_code` (`code`),
  KEY `ix_sexes_id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sexes`
--

LOCK TABLES `sexes` WRITE;
/*!40000 ALTER TABLE `sexes` DISABLE KEYS */;
INSERT INTO `sexes` VALUES ('SX',1,1,NULL,NULL),('CV',2,2,NULL,NULL);
/*!40000 ALTER TABLE `sexes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `number_document` varchar(20) NOT NULL,
  `specialty` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `phone` varchar(20) NOT NULL,
  `full_name` varchar(100) NOT NULL,
  `type_document` enum('identity_card','passport','other') NOT NULL,
  `pass_hash` varchar(255) NOT NULL,
  `id` int NOT NULL AUTO_INCREMENT,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ix_users_email` (`email`),
  UNIQUE KEY `ix_users_number_document` (`number_document`),
  KEY `ix_users_id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES ('1234567890','Administrador','admin@biogenetic.com','1234567890','Administrador','identity_card','$2b$12$GOwit.KkHcGB8BFJSRV2IuSddin/M5TtwI9E7RvD9Vus/4sjJFvua',1,'2025-05-27 14:22:05','2025-05-27 14:22:05'),('9876543210','Veterinario','user@biogenetic.com','9876543210','Usuario Normal','identity_card','$2b$12$cKPgT5zyh8DoGjstjS7youzV14XSLtTXcrT6XK0zyYXcocmNh6Q4e',2,'2025-05-27 14:22:05','2025-05-27 14:22:05'),('5678901234','Ganadero','client@biogenetic.com','5678901234','Cliente Regular','identity_card','$2b$12$XDW4G8j9beP9wQyZXt8bBOyPRFoSnPPDZDwsv00tKXmYhmgGSntZW',3,'2025-05-27 14:22:06','2025-05-27 14:22:06'),('12345678901','Admin','antom95@gmail.com','3002155199','Antonieta Medina','identity_card','$2b$12$itUHtD3Owhf2TFELj6LZHOSBROwygP0enYk/RnWuKVzROkgW8Hehm',4,'2025-06-10 13:55:28','2025-06-10 13:55:28'),('1140887673','Dr Veterinario','jhosephvillalba@gmail.com','3002155188','Joseph Enrique Villalba Osorio','identity_card','$2b$12$GtojSaJUwFT41lHtFS.S7OOIb3FNfCg6LhN8JwAMDJzool.9IZQCm',5,'2025-06-10 13:58:30','2025-06-10 13:58:30'),('1140887689','Client','enriquevillalba@gmail.com','3002155188','Enrique Villalba Osorio','identity_card','$2b$12$vmYZii3R3hrjziyvkD.t1eaQ5qnkThQLsNock87O9rxyuA7/zVbj6',6,'2025-06-10 14:53:15','2025-06-10 14:53:15'),('1140887674','Client','carolvillalba@gmail.com','3002155177','Carol Villalba Osorio','identity_card','$2b$12$sYw95JYDRyNgvpLT8QPxweMzDEOC1MkPBASQ5lt5j7EDLqVH2vLlW',7,'2025-06-10 14:58:40','2025-06-10 14:58:40');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'biogenetic'
--

--
-- Dumping routines for database 'biogenetic'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-06-18  4:28:08
