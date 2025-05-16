-- MySQL dump 10.13  Distrib 8.0.40, for Win64 (x86_64)
--
-- Host: localhost    Database: bankmanagement
-- ------------------------------------------------------
-- Server version	8.0.40

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
-- Table structure for table `cards`
--

DROP TABLE IF EXISTS `cards`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cards` (
  `accountID` int NOT NULL,
  `clientID` int NOT NULL,
  `cardType` varchar(50) NOT NULL,
  `cardIssued` date NOT NULL,
  PRIMARY KEY (`accountID`,`clientID`),
  KEY `clientID` (`clientID`),
  CONSTRAINT `cards_ibfk_1` FOREIGN KEY (`accountID`) REFERENCES `accounts` (`accountId`),
  CONSTRAINT `cards_ibfk_2` FOREIGN KEY (`clientID`) REFERENCES `clients` (`clientId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cards`
--

LOCK TABLES `cards` WRITE;
/*!40000 ALTER TABLE `cards` DISABLE KEYS */;
INSERT INTO `cards` VALUES (1,1,'Debit','2023-01-15'),(2,2,'Credit','2023-02-20'),(3,3,'Debit','2023-03-10'),(4,4,'Credit','2023-04-05'),(5,5,'Debit','2023-05-25'),(6,6,'Credit','2023-06-18'),(7,7,'Debit','2023-07-22'),(8,8,'Credit','2023-08-13'),(9,9,'Debit','2023-09-30'),(10,10,'Credit','2023-10-11'),(11,11,'Debit','2023-11-01'),(12,12,'Credit','2023-12-20'),(13,13,'Debit','2024-01-02'),(14,14,'Credit','2024-02-15'),(15,15,'Debit','2024-03-22'),(16,16,'Credit','2024-04-18'),(17,17,'Debit','2024-05-10'),(18,18,'Credit','2024-06-30'),(19,19,'Debit','2024-07-17'),(20,20,'Credit','2024-08-25');
/*!40000 ALTER TABLE `cards` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-05-12 22:24:34
