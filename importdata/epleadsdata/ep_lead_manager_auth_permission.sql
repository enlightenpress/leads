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
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=89 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add address type',7,'add_addresstype'),(26,'Can change address type',7,'change_addresstype'),(27,'Can delete address type',7,'delete_addresstype'),(28,'Can view address type',7,'view_addresstype'),(29,'Can add centre',8,'add_centre'),(30,'Can change centre',8,'change_centre'),(31,'Can delete centre',8,'delete_centre'),(32,'Can view centre',8,'view_centre'),(33,'Can add centre type',9,'add_centretype'),(34,'Can change centre type',9,'change_centretype'),(35,'Can delete centre type',9,'delete_centretype'),(36,'Can view centre type',9,'view_centretype'),(37,'Can add contact person',10,'add_contactperson'),(38,'Can change contact person',10,'change_contactperson'),(39,'Can delete contact person',10,'delete_contactperson'),(40,'Can view contact person',10,'view_contactperson'),(41,'Can add contact person position',11,'add_contactpersonposition'),(42,'Can change contact person position',11,'change_contactpersonposition'),(43,'Can delete contact person position',11,'delete_contactpersonposition'),(44,'Can view contact person position',11,'view_contactpersonposition'),(45,'Can add country',12,'add_country'),(46,'Can change country',12,'change_country'),(47,'Can delete country',12,'delete_country'),(48,'Can view country',12,'view_country'),(49,'Can add data source',13,'add_datasource'),(50,'Can change data source',13,'change_datasource'),(51,'Can delete data source',13,'delete_datasource'),(52,'Can view data source',13,'view_datasource'),(53,'Can add phone',14,'add_phone'),(54,'Can change phone',14,'change_phone'),(55,'Can delete phone',14,'delete_phone'),(56,'Can view phone',14,'view_phone'),(57,'Can add opening hours',15,'add_openinghours'),(58,'Can change opening hours',15,'change_openinghours'),(59,'Can delete opening hours',15,'delete_openinghours'),(60,'Can view opening hours',15,'view_openinghours'),(61,'Can add email',16,'add_email'),(62,'Can change email',16,'change_email'),(63,'Can delete email',16,'delete_email'),(64,'Can view email',16,'view_email'),(65,'Can add address',17,'add_address'),(66,'Can change address',17,'change_address'),(67,'Can delete address',17,'delete_address'),(68,'Can view address',17,'view_address'),(69,'Can add no contact',18,'add_nocontact'),(70,'Can change no contact',18,'change_nocontact'),(71,'Can delete no contact',18,'delete_nocontact'),(72,'Can view no contact',18,'view_nocontact'),(73,'Can add centre group',19,'add_centregroup'),(74,'Can change centre group',19,'change_centregroup'),(75,'Can delete centre group',19,'delete_centregroup'),(76,'Can view centre group',19,'view_centregroup'),(77,'Can add scraper',20,'add_scraper'),(78,'Can change scraper',20,'change_scraper'),(79,'Can delete scraper',20,'delete_scraper'),(80,'Can view scraper',20,'view_scraper'),(81,'Can add scrape queue',21,'add_scrapequeue'),(82,'Can change scrape queue',21,'change_scrapequeue'),(83,'Can delete scrape queue',21,'delete_scrapequeue'),(84,'Can view scrape queue',21,'view_scrapequeue'),(85,'Can add governing body',22,'add_govbody'),(86,'Can change governing body',22,'change_govbody'),(87,'Can delete governing body',22,'delete_govbody'),(88,'Can view governing body',22,'view_govbody');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
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
