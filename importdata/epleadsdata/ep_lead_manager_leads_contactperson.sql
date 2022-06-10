-- MySQL dump 10.13  Distrib 8.0.26, for Win64 (x86_64)
--
-- Host: localhost    Database: ep_lead_manager
-- ------------------------------------------------------
-- Server version	8.0.26

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
-- Table structure for table `leads_contactperson`
--

DROP TABLE IF EXISTS `leads_contactperson`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `leads_contactperson` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `source_id` bigint DEFAULT NULL,
  `position_id` bigint NOT NULL,
  `active` tinyint(1) NOT NULL,
  `centre_id` bigint NOT NULL,
  `primary` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `leads_contactperson_centre_id_primary_7145e52f_uniq` (`centre_id`,`primary`),
  KEY `leads_contactperson_source_id_c8fdd2a5_fk_leads_datasource_id` (`source_id`),
  KEY `leads_contactperson_position_id_aa41ff25_fk_leads_con` (`position_id`),
  KEY `leads_contactperson_centre_id_ab71d774` (`centre_id`),
  CONSTRAINT `leads_contactperson_centre_id_ab71d774_fk_leads_centre_id` FOREIGN KEY (`centre_id`) REFERENCES `leads_centre` (`id`),
  CONSTRAINT `leads_contactperson_position_id_aa41ff25_fk_leads_con` FOREIGN KEY (`position_id`) REFERENCES `leads_contactpersonposition` (`id`),
  CONSTRAINT `leads_contactperson_source_id_c8fdd2a5_fk_leads_datasource_id` FOREIGN KEY (`source_id`) REFERENCES `leads_datasource` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=44646 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `leads_contactperson`
--

LOCK TABLES `leads_contactperson` WRITE;
/*!40000 ALTER TABLE `leads_contactperson` DISABLE KEYS */;
/*!40000 ALTER TABLE `leads_contactperson` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-02-17 13:29:51
