-- MySQL dump 10.13  Distrib 5.5.57, for debian-linux-gnu (x86_64)
--
-- Host: 0.0.0.0    Database: loft
-- ------------------------------------------------------
-- Server version	5.5.57-0ubuntu0.14.04.1

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
-- Current Database: `loft`
--

/*!40000 DROP DATABASE IF EXISTS `loft`*/;

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `loft` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `loft`;

--
-- Table structure for table `dates`
--

DROP TABLE IF EXISTS `dates`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dates` (
  `PID` int(10) DEFAULT NULL,
  `startDate` date DEFAULT NULL,
  `endDate` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dates`
--

LOCK TABLES `dates` WRITE;
/*!40000 ALTER TABLE `dates` DISABLE KEYS */;
INSERT INTO `dates` VALUES (1,'2019-01-01','2019-01-31'),(2,'2019-05-01','2019-09-01'),(3,'2019-01-01','2019-12-31'),(4,'2019-01-01','2019-01-31');
/*!40000 ALTER TABLE `dates` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `featuresProperties`
--

DROP TABLE IF EXISTS `featuresProperties`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `featuresProperties` (
  `PID` int(10) DEFAULT NULL,
  `features` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `featuresProperties`
--

LOCK TABLES `featuresProperties` WRITE;
/*!40000 ALTER TABLE `featuresProperties` DISABLE KEYS */;
/*!40000 ALTER TABLE `featuresProperties` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `featuresTenants`
--

DROP TABLE IF EXISTS `featuresTenants`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `featuresTenants` (
  `UID` int(10) DEFAULT NULL,
  `features` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `featuresTenants`
--

LOCK TABLES `featuresTenants` WRITE;
/*!40000 ALTER TABLE `featuresTenants` DISABLE KEYS */;
/*!40000 ALTER TABLE `featuresTenants` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `host_prop`
--

DROP TABLE IF EXISTS `host_prop`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `host_prop` (
  `UID` int(11) NOT NULL DEFAULT '0',
  `PID` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`UID`,`PID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `host_prop`
--

LOCK TABLES `host_prop` WRITE;
/*!40000 ALTER TABLE `host_prop` DISABLE KEYS */;
INSERT INTO `host_prop` VALUES (4,1),(6,2),(6,3),(6,4);
/*!40000 ALTER TABLE `host_prop` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `properties`
--

DROP TABLE IF EXISTS `properties`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `properties` (
  `propName` varchar(100) DEFAULT NULL,
  `propDescription` varchar(100) DEFAULT NULL,
  `propLocation` varchar(150) DEFAULT NULL,
  `propPrice` int(10) unsigned DEFAULT NULL,
  `propSmoker` int(1) DEFAULT NULL,
  `propGender` int(1) DEFAULT NULL,
  `propPet` int(1) DEFAULT NULL,
  `propFilename` varchar(50) DEFAULT NULL,
  `PID` int(10) unsigned NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`PID`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `properties`
--

LOCK TABLES `properties` WRITE;
/*!40000 ALTER TABLE `properties` DISABLE KEYS */;
INSERT INTO `properties` VALUES ('Litter box','Nice litter box','North End',50,0,3,1,'4-Litter_box.jpeg',1),('Spacious Apartment','75 sq ft room near Central St','Central',900,0,3,0,'6-Spacious_Apartment.jpeg',2),('Dog House','Dog House near Wellesley','Wellesley',400,1,2,0,'6-Dog_House.jpeg',3),('MIT Living Quarter','Close to campus','MIT',900,0,1,0,'6-MIT_Living_Quarter.jpeg',4);
/*!40000 ALTER TABLE `properties` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `renter_prop`
--

DROP TABLE IF EXISTS `renter_prop`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `renter_prop` (
  `UID` int(11) NOT NULL DEFAULT '0',
  `PID` int(11) NOT NULL DEFAULT '0',
  `startDate` date DEFAULT NULL,
  `endDate` date DEFAULT NULL,
  PRIMARY KEY (`UID`,`PID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `renter_prop`
--

LOCK TABLES `renter_prop` WRITE;
/*!40000 ALTER TABLE `renter_prop` DISABLE KEYS */;
INSERT INTO `renter_prop` VALUES (4,2,'2019-01-01','2019-01-31');
/*!40000 ALTER TABLE `renter_prop` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tenants`
--

DROP TABLE IF EXISTS `tenants`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tenants` (
  `smoker` bit(1) DEFAULT b'0',
  `gender` int(1) DEFAULT '0',
  `pet` bit(1) DEFAULT b'0',
  `UID` int(15) unsigned DEFAULT NULL,
  KEY `UID` (`UID`),
  CONSTRAINT `tenants_ibfk_1` FOREIGN KEY (`UID`) REFERENCES `users` (`UID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tenants`
--

LOCK TABLES `tenants` WRITE;
/*!40000 ALTER TABLE `tenants` DISABLE KEYS */;
INSERT INTO `tenants` VALUES ('\0',2,'\0',1);
/*!40000 ALTER TABLE `tenants` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `name` varchar(20) DEFAULT NULL,
  `email` varchar(30) DEFAULT NULL,
  `pw` varchar(60) DEFAULT NULL,
  `university` varchar(40) DEFAULT NULL,
  `UID` int(15) unsigned NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`UID`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES ('Freddie','freddie@bu.edu','password','Boston University',1),('Mary','mary@mit.edu','password','Massachusetts Institute of Technology',2),('James','james@bc.edu','$2b$12$E1QEtU243.MNpxXZL1rZFe/xPLOCl4ZtHprJmCP0uzb57X7n4Oe0m','Boston College',4),('Lucy','lucy@mit.edu','$2b$12$JRC8FUBavQC0D0cU8nHb9eZbTf4rLiePbpVNTvvQkRptIQVGJO1mi','MIT',5),('Amy','amy@mit.edu','$2b$12$ts9Zyii9Bd0K2ZVF9gp0zOagEsXvlsi0ForS0xLpqJ7p0oCnLgcpC','MIT',6);
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

-- Dump completed on 2018-12-13 17:39:52
