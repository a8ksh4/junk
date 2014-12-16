-- MySQL dump 10.13  Distrib 5.1.63, for debian-linux-gnu (i486)
--
-- Host: localhost    Database: Web_game
-- ------------------------------------------------------
-- Server version	5.1.63-0ubuntu0.10.04.1

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
-- Table structure for table `PlanetTypes`
--

DROP TABLE IF EXISTS `PlanetTypes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `PlanetTypes` (
  `PTypeID` int(5) NOT NULL,
  `Name` varchar(12) NOT NULL,
  `MineralCount` int(5) NOT NULL,
  `WaterCount` int(5) NOT NULL,
  `BioCount` int(5) NOT NULL,
  PRIMARY KEY (`PTypeID`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `PlanetTypes`
--

LOCK TABLES `PlanetTypes` WRITE;
/*!40000 ALTER TABLE `PlanetTypes` DISABLE KEYS */;
INSERT INTO `PlanetTypes` VALUES (0,'Non-Planet',0,0,0),(1,'Gas Giant',1,2,3),(2,'Terrestrial',4,6,5);
/*!40000 ALTER TABLE `PlanetTypes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Players`
--

DROP TABLE IF EXISTS `Players`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Players` (
  `ID` int(10) NOT NULL,
  `Name` varchar(12) NOT NULL,
  `Email` varchar(50) NOT NULL,
  `PasswdHash` varchar(50) NOT NULL,
  `StartDate` date NOT NULL,
  `Score` int(5) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Players`
--

LOCK TABLES `Players` WRITE;
/*!40000 ALTER TABLE `Players` DISABLE KEYS */;
INSERT INTO `Players` VALUES (1,'Aria','aria.kraft@gmail.com','xxxx','2012-01-01',0),(2,'Brian','brian.barnes@gmail.com','xxxx','2012-01-01',0),(3,'Dan','spam.dn@gmail.com','xxxx','2012-01-01',0);
/*!40000 ALTER TABLE `Players` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ShipGroups`
--

DROP TABLE IF EXISTS `ShipGroups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ShipGroups` (
  `PlayerID` int(5) NOT NULL,
  `GroupID` int(5) NOT NULL,
  `Name` varchar(30) DEFAULT NULL,
  `SystemID` int(5) NOT NULL,
  `PlanetID` int(5) NOT NULL,
  PRIMARY KEY (`PlayerID`,`GroupID`),
  KEY `SystemID` (`SystemID`,`PlanetID`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ShipGroups`
--

LOCK TABLES `ShipGroups` WRITE;
/*!40000 ALTER TABLE `ShipGroups` DISABLE KEYS */;
INSERT INTO `ShipGroups` VALUES (1,0,'Home Ship',0,0),(1,1,'Squad A',0,1),(1,2,'Squad B',4,1),(1,3,'Squad C',4,0),(2,0,'Home Ship',0,0),(2,1,'Squad A',3,2),(2,2,'Squad B',3,3),(2,3,'Squad C',3,1),(3,0,'Home Ship',3,2),(3,1,'Squad A',4,0),(3,2,'Squad B',4,1),(3,3,'Squad C',1,0);
/*!40000 ALTER TABLE `ShipGroups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `SolarSystems`
--

DROP TABLE IF EXISTS `SolarSystems`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `SolarSystems` (
  `SystemID` int(5) NOT NULL,
  `XLocation` int(5) NOT NULL,
  `YLocation` int(5) NOT NULL,
  `IsBlackHole` varchar(3) NOT NULL,
  PRIMARY KEY (`SystemID`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `SolarSystems`
--

LOCK TABLES `SolarSystems` WRITE;
/*!40000 ALTER TABLE `SolarSystems` DISABLE KEYS */;
INSERT INTO `SolarSystems` VALUES (0,0,0,'YES'),(1,0,1,'NO'),(2,1,0,'NO'),(3,1,1,'NO'),(4,0,2,'NO');
/*!40000 ALTER TABLE `SolarSystems` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `SystemPlanets`
--

DROP TABLE IF EXISTS `SystemPlanets`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `SystemPlanets` (
  `SystemID` int(5) NOT NULL,
  `PlanetID` int(5) NOT NULL,
  `PTypeID` int(5) NOT NULL,
  `MineralUsed` int(5) NOT NULL,
  `WaterUsed` int(5) NOT NULL,
  `BioUsed` int(5) NOT NULL,
  PRIMARY KEY (`SystemID`,`PlanetID`),
  KEY `PTypeID` (`PTypeID`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `SystemPlanets`
--

LOCK TABLES `SystemPlanets` WRITE;
/*!40000 ALTER TABLE `SystemPlanets` DISABLE KEYS */;
INSERT INTO `SystemPlanets` VALUES (0,0,0,0,0,0),(0,1,1,4,2,0),(1,0,0,0,0,0),(2,0,0,0,0,0),(3,0,0,2,1,3),(3,1,0,5,9,0),(3,2,1,5,5,5),(3,3,2,6,0,0),(4,0,0,0,0,0),(4,1,1,2,6,3);
/*!40000 ALTER TABLE `SystemPlanets` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2012-08-20 23:07:14
