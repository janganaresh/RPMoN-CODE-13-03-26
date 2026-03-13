-- MySQL dump 10.13  Distrib 8.0.41, for Win64 (x86_64)
--
-- Host: localhost    Database: remedydb
-- ------------------------------------------------------
-- Server version	8.0.41

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `remedy`
--

DROP TABLE IF EXISTS `remedy`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `remedy` (
  `Remedy ID` varchar(10) NOT NULL,
  `Area ID` varchar(15) DEFAULT NULL,
  `User ID` varchar(255) DEFAULT NULL,
  `Table ID` varchar(255) DEFAULT NULL,
  `Pile No` int DEFAULT NULL,
  `Task Date` date NOT NULL,
  `Allotted Date` date NOT NULL,
  `Allotted By` varchar(255) DEFAULT NULL,
  `Date Completed` date DEFAULT NULL,
  `Assessed Case` varchar(255) DEFAULT NULL,
  `Remedy Status` text,
  `Remedy Text` varchar(255) DEFAULT NULL,
  `Picture1 Name` varchar(255) DEFAULT NULL,
  `Picture2 Name` varchar(255) DEFAULT NULL,
  `Picture3 Name` varchar(255) DEFAULT NULL,
  `Picture4 Name` varchar(255) DEFAULT NULL,
  `Picture Location` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Remedy ID`),
  KEY `User ID` (`User ID`),
  KEY `Pile ID` (`Table ID`),
  KEY `Allotted By` (`Allotted By`),
  CONSTRAINT `remedy_ibfk_1` FOREIGN KEY (`User ID`) REFERENCES `users` (`User ID`),
  CONSTRAINT `remedy_ibfk_3` FOREIGN KEY (`Allotted By`) REFERENCES `users` (`User ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `remedy`
--

LOCK TABLES `remedy` WRITE;
/*!40000 ALTER TABLE `remedy` DISABLE KEYS */;
INSERT INTO `remedy` VALUES ('RM00001','A001','U011','C63S24',1,'2025-05-25','2025-05-25','U001',NULL,'Not Assessed','In Progress','',NULL,NULL,NULL,NULL,NULL),('RM00002','A001','U011','C63S24',2,'2025-05-25','2025-05-25','U001',NULL,'Not Assessed','In Progress','',NULL,NULL,NULL,NULL,NULL),('RM00003','A001','U011','C63S24',3,'2025-05-25','2025-05-25','U001',NULL,'Not Assessed','In Progress','',NULL,NULL,NULL,NULL,NULL),('RM00004','A001','U011','C63S24',4,'2025-05-25','2025-05-25','U001',NULL,'Not Assessed','In Progress','',NULL,NULL,NULL,NULL,NULL),('RM00005','A001','U011','C62S24',1,'2025-05-25','2025-05-25','U001',NULL,'Not Assessed','In Progress','',NULL,NULL,NULL,NULL,NULL),('RM00006','A001','U011','C62S24',2,'2025-05-25','2025-05-25','U001',NULL,'Not Assessed','In Progress','',NULL,NULL,NULL,NULL,NULL),('RM00007','A001','U011','C62S24',3,'2025-05-25','2025-05-25','U001',NULL,'Not Assessed','In Progress','',NULL,NULL,NULL,NULL,NULL),('RM00008','A001','U011','C62S24',4,'2025-05-25','2025-05-25','U001',NULL,'Not Assessed','In Progress','',NULL,NULL,NULL,NULL,NULL),('RM00009','A001','U011','C61S24',1,'2025-05-25','2025-05-25','U001',NULL,'Not Assessed','In Progress','',NULL,NULL,NULL,NULL,NULL),('RM00010','A001','U011','C61S24',2,'2025-05-25','2025-05-25','U001',NULL,'Not Assessed','In Progress','',NULL,NULL,NULL,NULL,NULL),('RM00011','A001','U011','C61S24',3,'2025-05-25','2025-05-25','U001',NULL,'Not Assessed','In Progress','',NULL,NULL,NULL,NULL,NULL),('RM00012','A001','U011','C61S24',4,'2025-05-25','2025-05-25','U001',NULL,'Not Assessed','In Progress','',NULL,NULL,NULL,NULL,NULL),('RM00013','A001','U011','C60S24',1,'2025-05-25','2025-05-25','U001',NULL,'Not Assessed','In Progress','',NULL,NULL,NULL,NULL,NULL),('RM00014','A001','U011','C60S24',2,'2025-05-25','2025-05-25','U001',NULL,'Not Assessed','In Progress','',NULL,NULL,NULL,NULL,NULL),('RM00015','A001','U011','C60S24',3,'2025-05-25','2025-05-25','U001',NULL,'Not Assessed','In Progress','',NULL,NULL,NULL,NULL,NULL),('RM00016','A001','U011','C60S24',4,'2025-05-25','2025-05-25','U001',NULL,'Not Assessed','In Progress','',NULL,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `remedy` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-05-26 16:36:58
