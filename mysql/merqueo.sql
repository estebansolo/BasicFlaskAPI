-- MySQL dump 10.13  Distrib 5.7.26, for Linux (x86_64)
--
-- Host: 192.168.55.2    Database: merqueo
-- ------------------------------------------------------
-- Server version	5.7.26

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
-- Table structure for table `orders`
--

DROP TABLE IF EXISTS `orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `orders` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `priority` int(11) NOT NULL,
  `address` varchar(255) NOT NULL,
  `user` varchar(255) NOT NULL,
  `deliveryDate` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders`
--

LOCK TABLES `orders` WRITE;
/*!40000 ALTER TABLE `orders` DISABLE KEYS */;
INSERT INTO `orders` VALUES (1,1,'KR 14 # 87 - 20','Sofia','2019-03-01'),(2,1,'KR 20 # 164A - 5','Angel','2019-03-01'),(3,3,'KR 13 # 74 - 38','Hocks','2019-03-01'),(4,1,'CL 93 # 12 - 9','Michael','2019-03-01'),(5,1,'CL 71 # 3 - 74','Bar de Alex','2019-03-01'),(6,2,'KR 20 # 134A - 5','Sabor Criollo','2019-03-01'),(7,2,'CL 80 # 14 - 38','El Pollo Rojo','2019-03-01'),(8,7,'KR 14 # 98 - 74','All Salad','2019-03-01'),(9,1,'KR 58 # 93 - 1','Parrilla y sabor','2019-03-01'),(10,9,'KR 14 # 87 - 20','Sofia','2019-03-01'),(11,1,'CL 93B # 17 - 12','restaurante yerbabuena','2019-03-01'),(12,10,'KR 68D # 98A - 11','Luis David','2019-03-01'),(13,2,'AC 72 # 20 - 45','David Carruyo','2019-03-01'),(14,3,'KR 22 # 122 - 57','MARIO','2019-03-01'),(15,8,'KR 88 # 72A - 26','Harold','2019-03-01');
/*!40000 ALTER TABLE `orders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orders_products`
--

DROP TABLE IF EXISTS `orders_products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `orders_products` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `product_id` int(11) NOT NULL,
  `order_id` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=56 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders_products`
--

LOCK TABLES `orders_products` WRITE;
/*!40000 ALTER TABLE `orders_products` DISABLE KEYS */;
INSERT INTO `orders_products` VALUES (1,1,1),(2,2,1),(3,3,1),(4,4,1),(5,37,1),(6,5,2),(7,6,2),(8,7,3),(9,8,3),(10,9,3),(11,10,3),(12,11,3),(13,12,4),(14,13,4),(15,14,4),(16,15,4),(17,4,4),(18,16,5),(19,17,6),(20,18,6),(21,19,6),(22,20,6),(23,15,6),(24,21,7),(25,22,7),(26,23,7),(27,24,7),(28,39,7),(29,25,8),(30,26,8),(31,27,8),(32,22,8),(33,5,8),(34,22,9),(35,28,10),(36,7,11),(37,41,12),(38,19,12),(39,29,12),(40,17,12),(41,30,12),(42,7,13),(43,25,13),(44,5,13),(45,31,13),(46,43,14),(47,30,14),(48,32,14),(49,33,14),(50,28,14),(51,16,15),(52,34,15),(53,35,15),(54,12,15),(55,36,15);
/*!40000 ALTER TABLE `orders_products` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products`
--

DROP TABLE IF EXISTS `products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `products` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `quantity` int(11) NOT NULL,
  `date` date NOT NULL,
  `provider_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=42 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products`
--

LOCK TABLES `products` WRITE;
/*!40000 ALTER TABLE `products` DISABLE KEYS */;
INSERT INTO `products` VALUES (1,'Leche',3,'2019-03-01',1),(2,'Huevos',3,'2019-03-01',1),(3,'Manzana Verde',7,'2019-03-01',1),(4,'Pepino Cohombro',8,'2019-03-01',1),(5,'Piment\\u00f3n Rojo',10,'2019-03-01',1),(6,'Kiwi',15,'2019-03-01',3),(7,'Cebolla Cabezona Blanca Limpia',26,'2019-03-01',3),(8,'Habichuela',11,'2019-03-01',3),(9,'Mango Tommy Maduro',1,'2019-03-01',3),(10,'Tomate Chonto Pint\\u00f3n',8,'2019-03-01',3),(11,'Zanahoria Grande',7,'2019-03-01',3),(12,'Aguacate Maduro',8,'2019-03-01',3),(13,'Kale o Col Rizada',2,'2019-03-01',3),(14,'Cebolla Cabezona Roja Limpia',1,'2019-03-01',3),(15,'Tomate Chonto Maduro',1,'2019-03-01',3),(16,'Acelga',9,'2019-03-01',2),(17,'Espinaca Bogotana x 500grs',17,'2019-03-01',2),(18,'Ahuyama',8,'2019-03-01',3),(19,'Cebolla Cabezona Blanca Sin Pelar',9,'2019-03-01',3),(20,'Mel\\u00f3n',9,'2019-03-01',3),(21,'Cebolla Cabezona Roja Sin Pelar',3,'2019-03-01',3),(22,'Cebolla Larga Junca x 500grs',6,'2019-03-01',3),(23,'Hierbabuena x 500grs',9,'2019-03-01',3),(24,'Lechuga Crespa Verde',9,'2019-03-01',1),(25,'Lim\\u00f3n Tahit\\u00ed',10,'2019-03-01',1),(26,'Mora de Castilla',40,'2019-03-01',1),(27,'Piment\\u00f3n Verde',2,'2019-03-01',1),(28,'Tomate Larga Vida Maduro',3,'2019-03-01',2),(29,'Cilantro x 500grs',2,'2019-03-01',2),(30,'Fresa Jugo',1,'2019-03-01',2),(31,'Papa R-12 Mediana',9,'2019-03-01',2),(32,'Curuba',10,'2019-03-01',2),(33,'Br\\u00f3coli',2,'2019-03-01',2),(34,'Aguacate Hass Pint\\u00f3n',3,'2019-03-01',2),(35,'Aguacate Hass Maduro',3,'2019-03-01',2),(36,'Aguacate Pint\\u00f3n',6,'2019-03-01',2),(37,'Pan Bimbo',0,'2019-03-01',NULL),(39,'Lechuga Crespa Morada',0,'2019-03-01',NULL),(41,'banano',0,'2019-03-01',NULL);
/*!40000 ALTER TABLE `products` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `providers`
--

DROP TABLE IF EXISTS `providers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `providers` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `providers`
--

LOCK TABLES `providers` WRITE;
/*!40000 ALTER TABLE `providers` DISABLE KEYS */;
INSERT INTO `providers` VALUES (1,'Ruby'),(2,'Raul'),(3,'Angelica');
/*!40000 ALTER TABLE `providers` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-08-23 23:41:07
