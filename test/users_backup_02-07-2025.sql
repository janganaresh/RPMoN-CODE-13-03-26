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
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `User ID` varchar(255) NOT NULL,
  `Site ID` varchar(255) DEFAULT NULL,
  `User Name` varchar(255) NOT NULL,
  `Email` varchar(45) DEFAULT NULL,
  `Password` varchar(45) DEFAULT NULL,
  `User Designation` varchar(255) NOT NULL,
  `User Phone number` varchar(10) DEFAULT NULL,
  `User Type` varchar(255) NOT NULL,
  `Reports To` varchar(255) NOT NULL,
  `Date created` date DEFAULT NULL,
  `Date removed` date DEFAULT NULL,
  PRIMARY KEY (`User ID`),
  KEY `Site ID` (`Site ID`),
  CONSTRAINT `users_ibfk_1` FOREIGN KEY (`Site ID`) REFERENCES `site` (`Site ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES ('U001','S001','Naresh','nareshjanga966@gmail.com','111','Software Developer','1234567899','Admin','sunder raj sir','2025-01-04',NULL),('U002','S001','naresh','nareshjanga@gmail.com','222','Software Developer','1234567899','Normal User','123','2025-01-08',NULL),('U003','S001','Venkatesh','venkateshpeddagolla47@gmail.com','123','Software Developer','7674953083','Admin','U001','2025-02-08','2025-03-21'),('U008','S001','Sunder','sunder@indisolar.in','123','Software Developer','3243576451','Admin','U003','2025-03-15',NULL),('U009','S001','seenu','seenu.srinivasan558@gmail.com','maFi_25','OE Engineer','9677248303','Admin','U008','2025-04-01',NULL),('U010','S001','Mahendran','mahendran@indisolar.in','Thiyakrish2520$','Project Manager','9894027312','Admin','U008','2025-04-03',NULL),('U011','S001','Mahesh N','ganeshanavarm@gmail.com','Mahesh@123','QA Engineer','6361173535','Normal User','U010','2025-04-23',NULL);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-07-02 18:09:04
