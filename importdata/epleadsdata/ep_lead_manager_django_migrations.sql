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
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=40 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2022-02-04 05:50:04.864875'),(2,'auth','0001_initial','2022-02-04 05:50:05.375744'),(3,'admin','0001_initial','2022-02-04 05:50:05.516745'),(4,'admin','0002_logentry_remove_auto_add','2022-02-04 05:50:05.529745'),(5,'admin','0003_logentry_add_action_flag_choices','2022-02-04 05:50:05.547750'),(6,'contenttypes','0002_remove_content_type_name','2022-02-04 05:50:05.643557'),(7,'auth','0002_alter_permission_name_max_length','2022-02-04 05:50:05.707859'),(8,'auth','0003_alter_user_email_max_length','2022-02-04 05:50:05.741904'),(9,'auth','0004_alter_user_username_opts','2022-02-04 05:50:05.754903'),(10,'auth','0005_alter_user_last_login_null','2022-02-04 05:50:05.817911'),(11,'auth','0006_require_contenttypes_0002','2022-02-04 05:50:05.821911'),(12,'auth','0007_alter_validators_add_error_messages','2022-02-04 05:50:05.833913'),(13,'auth','0008_alter_user_username_max_length','2022-02-04 05:50:05.907002'),(14,'auth','0009_alter_user_last_name_max_length','2022-02-04 05:50:06.001002'),(15,'auth','0010_alter_group_name_max_length','2022-02-04 05:50:06.039042'),(16,'auth','0011_update_proxy_permissions','2022-02-04 05:50:06.054002'),(17,'auth','0012_alter_user_first_name_max_length','2022-02-04 05:50:06.119777'),(18,'leads','0001_initial','2022-02-04 05:50:07.918739'),(19,'leads','0002_centretype_description_alter_centretype_subtype_and_more','2022-02-04 05:50:08.079725'),(20,'leads','0003_alter_country_options_alter_centre_age_range_and_more','2022-02-04 05:50:08.255153'),(21,'leads','0004_centre_p_address_centre_p_email_centre_p_person_and_more','2022-02-04 05:50:08.705438'),(22,'leads','0005_remove_centrecontactperson_position_and_more','2022-02-04 05:50:08.882852'),(23,'leads','0006_remove_centre_p_address_address_primary_address_and_more','2022-02-04 05:50:09.050174'),(24,'leads','0007_alter_centrecontactperson_unique_together_and_more','2022-02-04 05:50:09.687723'),(25,'leads','0008_centre_contact_persons','2022-02-04 05:50:09.699725'),(26,'leads','0009_remove_centre_contact_persons_contactperson_active_and_more','2022-02-04 05:50:10.123027'),(27,'leads','0010_alter_contactperson_primary_contact_and_more','2022-02-04 05:50:10.263929'),(28,'leads','0011_alter_centre_gov_id','2022-02-04 05:50:10.357559'),(29,'leads','0012_rename_primary_contact_contactperson_primary_and_more','2022-02-04 05:50:10.897182'),(30,'leads','0013_remove_phone_area_code_alter_phone_number','2022-02-04 05:50:11.048978'),(31,'leads','0014_alter_addresstype_type','2022-02-04 05:50:11.088939'),(32,'leads','0015_openinghours_source','2022-02-04 05:50:11.198035'),(33,'leads','0011_centregroup_centre_group','2022-02-04 05:50:11.335891'),(34,'leads','0016_merge_20220204_1545','2022-02-04 05:50:11.340938'),(35,'scrapers','0001_initial','2022-02-04 05:50:11.613465'),(36,'scrapers','0002_scrapequeue_priority','2022-02-04 05:50:11.658429'),(37,'sessions','0001_initial','2022-02-04 05:50:11.711426'),(38,'leads','0017_govbody_centregroup_description_alter_centre_gov_id_and_more','2022-02-04 05:53:34.259329'),(39,'leads','0018_alter_centre_google_place_id_alter_centre_gov_body_and_more','2022-02-07 01:43:03.205234');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
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
