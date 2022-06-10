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
-- Table structure for table `scrapers_scrapequeue`
--

DROP TABLE IF EXISTS `scrapers_scrapequeue`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `scrapers_scrapequeue` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `centre_id` bigint NOT NULL,
  `scraper_id` bigint NOT NULL,
  `priority` varchar(2) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `scrapers_scrapequeue_scraper_id_centre_id_76e02581_uniq` (`scraper_id`,`centre_id`),
  KEY `scrapers_scrapequeue_centre_id_ee29c0bd_fk_leads_centre_id` (`centre_id`),
  CONSTRAINT `scrapers_scrapequeue_centre_id_ee29c0bd_fk_leads_centre_id` FOREIGN KEY (`centre_id`) REFERENCES `leads_centre` (`id`),
  CONSTRAINT `scrapers_scrapequeue_scraper_id_c5f451ee_fk_scrapers_scraper_id` FOREIGN KEY (`scraper_id`) REFERENCES `scrapers_scraper` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `scrapers_scrapequeue`
--

LOCK TABLES `scrapers_scrapequeue` WRITE;
/*!40000 ALTER TABLE `scrapers_scrapequeue` DISABLE KEYS */;
/*!40000 ALTER TABLE `scrapers_scrapequeue` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-02-17 13:29:52
