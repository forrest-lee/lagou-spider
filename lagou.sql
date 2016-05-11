-- MySQL dump 10.15  Distrib 10.0.21-MariaDB, for Linux (x86_64)
--
-- Host: localhost    Database: lagou
-- ------------------------------------------------------
-- Server version	5.6.27

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `ignored_word`
--

DROP TABLE IF EXISTS `ignored_word`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ignored_word` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `word` char(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `word` (`word`)
) ENGINE=InnoDB AUTO_INCREMENT=105 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ignored_word`
--

LOCK TABLES `ignored_word` WRITE;
/*!40000 ALTER TABLE `ignored_word` DISABLE KEYS */;
INSERT INTO `ignored_word` VALUES (1,''),(2,'('),(3,')'),(4,'*'),(5,'+'),(6,','),(7,'-'),(8,'.'),(9,'/'),(10,'0'),(11,'1'),(12,'1.3'),(13,'2'),(14,'3'),(15,'3.3'),(16,'4'),(17,'5'),(18,'6'),(19,'7'),(20,'8'),(21,'9'),(22,':'),(23,'a'),(24,'b'),(25,'“'),(26,'”'),(27,'、'),(28,'。'),(29,'《'),(30,'》'),(31,'【'),(32,'】'),(33,'一'),(34,'一项'),(35,'不'),(36,'与'),(37,'且'),(38,'中'),(39,'主要'),(40,'于'),(41,'交换'),(42,'人'),(43,'以下'),(44,'任职'),(45,'会'),(46,'你'),(47,'做'),(48,'其'),(49,'内'),(50,'化'),(51,'及'),(52,'可'),(53,'各'),(54,'后'),(55,'向'),(56,'和'),(57,'在'),(58,'均'),(59,'多'),(60,'大'),(61,'天'),(62,'好'),(63,'如'),(64,'对'),(65,'将'),(66,'岗位'),(67,'年'),(68,'年限'),(69,'广'),(70,'必'),(71,'或'),(72,'把'),(73,'控'),(74,'描述'),(75,'整'),(76,'新'),(77,'更'),(78,'曾'),(79,'最'),(80,'有'),(81,'由'),(82,'的'),(83,'端'),(84,'等'),(85,'编'),(86,'者'),(87,'而'),(88,'能'),(89,'自'),(90,'观'),(91,'让'),(92,'设'),(93,'该'),(94,'较'),(95,'过'),(96,'运'),(97,'里'),(98,'间'),(99,'需'),(100,'（'),(101,'）'),(102,'，'),(103,'：'),(104,'；');
/*!40000 ALTER TABLE `ignored_word` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `job_desc`
--

DROP TABLE IF EXISTS `job_desc`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `job_desc` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `position_id` int(10) unsigned DEFAULT NULL,
  `dept` char(255) DEFAULT NULL,
  `job_desc` text,
  `job_responsibility` text,
  `job_requirement` text,
  `time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `job_desc`
--

LOCK TABLES `job_desc` WRITE;
/*!40000 ALTER TABLE `job_desc` DISABLE KEYS */;
/*!40000 ALTER TABLE `job_desc` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `position`
--

DROP TABLE IF EXISTS `position`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `position` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `search_keyword` char(50) DEFAULT NULL,
  `company_id` int(10) unsigned DEFAULT NULL,
  `company_short` char(255) DEFAULT NULL,
  `company` char(255) DEFAULT NULL,
  `company_size` char(50) DEFAULT NULL,
  `finance_stage` char(50) DEFAULT NULL,
  `industry` char(100) DEFAULT NULL,
  `city` char(50) DEFAULT NULL,
  `position_id` int(10) unsigned DEFAULT NULL,
  `position_type` char(50) DEFAULT NULL,
  `position_name` char(50) DEFAULT NULL,
  `advantage` char(255) DEFAULT NULL,
  `salary` char(50) DEFAULT NULL,
  `work_year` char(50) DEFAULT NULL,
  `education` char(50) DEFAULT NULL,
  `time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `position`
--

LOCK TABLES `position` WRITE;
/*!40000 ALTER TABLE `position` DISABLE KEYS */;
/*!40000 ALTER TABLE `position` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `word_frequency`
--

DROP TABLE IF EXISTS `word_frequency`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `word_frequency` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `search_keyword` char(50) DEFAULT NULL,
  `word` char(255) DEFAULT NULL,
  `cnt` int(10) unsigned DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `word_frequency`
--

LOCK TABLES `word_frequency` WRITE;
/*!40000 ALTER TABLE `word_frequency` DISABLE KEYS */;
/*!40000 ALTER TABLE `word_frequency` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-02-28 13:01:37
