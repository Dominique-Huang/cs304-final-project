--
-- Current Database: `loft`
--

CREATE DATABASE `loft`;

USE `loft`;

--
-- Table structure for table `host`
--

DROP TABLE IF EXISTS `host`;
CREATE TABLE `host` (
  `userID` int(15) unsigned unsigned NOT NULL AUTO_INCREMENT,
  `propID` int(10) unsigned NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`userID`,`propID`),
  -- KEY `userID` (`userID`),
  -- KEY `nm` (`nm`),
  FOREIGN KEY (`userID`) REFERENCES `users` (`userID`) ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY (`propID`) REFERENCES `properties` (`propID`) ON DELETE CASCADE ON UPDATE CASCADE
  -- CONSTRAINT `credit_ibfk_2` FOREIGN KEY (`nm`) REFERENCES `person` (`nm`) ON DELETE CASCADE ON UPDATE CASCADE,
  -- CONSTRAINT `credit_ibfk_3` FOREIGN KEY (`tt`) REFERENCES `movie` (`tt`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `host`
--

LOCK TABLES `host` WRITE;
INSERT INTO `host` VALUES (1,1), (1, 2);
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
  `name` varchar(20) DEFAULT NULL,
  /* `email` varchar(30) DEFAULT NULL,
  `pw` varchar(60) DEFAULT NULL, */
  `university` varchar(40) DEFAULT NULL,
  `userID` int(15) unsigned unsigned NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`userID`),
) 

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
INSERT INTO `users` VALUES ('Freddie(host)','Boston University',1), ('Freddie2(not host)','Massachusetts Institute of Technology',2);
UNLOCK TABLES;

--
-- Table structure for table `properties`
--

DROP TABLE IF EXISTS `properties`;
/* How to store images, gender, availability? */;
CREATE TABLE `properties` (
  `propName` varchar(30) DEFAULT NULL,
  `propDescrip` varchar(150) DEFAULT NULL,
  `propLocation` varchar(150) DEFAULT NULL,
  `propPrice` int(10) unsigned DEFAULT NULL,
  `propID` int(10) unsigned NOT NULL AUTO_INCREMENT
  PRIMARY KEY (`propID`),
) 

--
-- Dumping data for table `properties`
--

LOCK TABLES `properties` WRITE;
INSERT INTO `properties` VALUES ('1 BR near Kendall','Single bedroom in apartment near Kendall Square','Kendall Square, Cambridge','1000',1), ('3 BR apartment near Central','Entire apartment include 3 BR located in Central','Central Square, Cambridge','4000',2),
UNLOCK TABLES;
