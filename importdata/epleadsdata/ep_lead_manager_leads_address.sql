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
-- Table structure for table `leads_address`
--

DROP TABLE IF EXISTS `leads_address`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `leads_address` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `address` varchar(500) NOT NULL,
  `city` varchar(200) NOT NULL,
  `state` varchar(200) NOT NULL,
  `postcode` varchar(10) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `centre_id` bigint NOT NULL,
  `country_id` varchar(2) NOT NULL,
  `source_id` bigint DEFAULT NULL,
  `type_id` bigint NOT NULL,
  `lattitude` decimal(8,6) NOT NULL,
  `longitude` decimal(9,6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `leads_address_centre_id_type_id_abafbb20_uniq` (`centre_id`,`type_id`),
  KEY `leads_address_country_id_049d451e_fk_leads_country_code` (`country_id`),
  KEY `leads_address_source_id_09eb24e0_fk_leads_datasource_id` (`source_id`),
  KEY `leads_address_type_id_1b9df73d_fk_leads_addresstype_id` (`type_id`),
  KEY `leads_address_centre_id_8a06111f` (`centre_id`),
  CONSTRAINT `leads_address_centre_id_8a06111f_fk_leads_centre_id` FOREIGN KEY (`centre_id`) REFERENCES `leads_centre` (`id`),
  CONSTRAINT `leads_address_country_id_049d451e_fk_leads_country_code` FOREIGN KEY (`country_id`) REFERENCES `leads_country` (`code`),
  CONSTRAINT `leads_address_source_id_09eb24e0_fk_leads_datasource_id` FOREIGN KEY (`source_id`) REFERENCES `leads_datasource` (`id`),
  CONSTRAINT `leads_address_type_id_1b9df73d_fk_leads_addresstype_id` FOREIGN KEY (`type_id`) REFERENCES `leads_addresstype` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=183210 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `leads_address`
--

LOCK TABLES `leads_address` WRITE;
/*!40000 ALTER TABLE `leads_address` DISABLE KEYS */;
/*!40000 ALTER TABLE `leads_address` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-02-17 13:29:49
