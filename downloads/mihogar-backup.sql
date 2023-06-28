-- MariaDB dump 10.19  Distrib 10.5.19-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: mihogar
-- ------------------------------------------------------
-- Server version	10.5.19-MariaDB-0+deb11u2

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `ad_addresses`
--

DROP TABLE IF EXISTS `ad_addresses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ad_addresses` (
  `ad_id` varchar(36) NOT NULL,
  `ad_type` varchar(100) DEFAULT NULL,
  `ad_address` varchar(100) NOT NULL,
  `ad_reference` varchar(100) DEFAULT NULL,
  `ad_postalcode` varchar(20) NOT NULL,
  `ad_contact` varchar(50) DEFAULT NULL,
  `ad_status` tinyint(1) NOT NULL DEFAULT 1,
  `ad_regdate` datetime NOT NULL DEFAULT current_timestamp(),
  `ci_id` int(11) NOT NULL,
  `pe_id` varchar(36) NOT NULL,
  PRIMARY KEY (`ad_id`),
  KEY `pe_id` (`pe_id`),
  KEY `ci_id` (`ci_id`),
  CONSTRAINT `ad_addresses_ibfk_1` FOREIGN KEY (`pe_id`) REFERENCES `pe_persons` (`pe_id`),
  CONSTRAINT `ad_addresses_ibfk_2` FOREIGN KEY (`ci_id`) REFERENCES `ci_cities` (`ci_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ad_addresses`
--

LOCK TABLES `ad_addresses` WRITE;
/*!40000 ALTER TABLE `ad_addresses` DISABLE KEYS */;
INSERT INTO `ad_addresses` VALUES ('14089ca1-66b0-41df-975b-9448b0b2e00c','CLIENTE','4ta calle la garenas','MARCELA PEREZ','03012','58987545',1,'2023-06-25 23:50:44',100002,'6ee76bd0-2148-4ea4-8f81-3a49df825daa'),('20f14660-0694-45f8-94b7-bae5ee3bc0e5','referencia','500 country oaks dr','marcela perez','79932','48754565',1,'2023-06-26 14:57:11',100004,'6ee76bd0-2148-4ea4-8f81-3a49df825daa'),('6d3be486-22ed-40a2-bc8e-f7dc193944f8','Referencia','San lorenzo','Luis','hermano','42151231',1,'2023-06-26 22:53:49',100005,'2277109b-a877-4a89-a6d0-9a47b2ca97c6'),('8ed071ff-a757-44d0-8c19-2783426be533',NULL,'1383 s gibbs st',NULL,'91766',NULL,1,'2023-06-25 03:00:44',100003,'ea01b71f-51df-4e9a-a402-018e399e611b'),('e431fdb2-316a-4bc8-87bb-fa8e37f531cd',NULL,'500 country oaks dr',NULL,'79932',NULL,1,'2023-06-25 03:01:35',100004,'ea01b71f-51df-4e9a-a402-018e399e611b'),('f2e7dab8-ea72-4397-abbe-5788f813366d','REFERENCIA','San lorenzo el cubo','12','03012','58458754',0,'2023-06-25 23:56:15',100002,'6ee76bd0-2148-4ea4-8f81-3a49df825daa');
/*!40000 ALTER TABLE `ad_addresses` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `br_brands`
--

DROP TABLE IF EXISTS `br_brands`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `br_brands` (
  `br_id` int(11) NOT NULL AUTO_INCREMENT,
  `br_name` varchar(50) NOT NULL,
  `br_status` tinyint(1) NOT NULL DEFAULT 1,
  PRIMARY KEY (`br_id`),
  UNIQUE KEY `br_name` (`br_name`)
) ENGINE=InnoDB AUTO_INCREMENT=100002 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `br_brands`
--

LOCK TABLES `br_brands` WRITE;
/*!40000 ALTER TABLE `br_brands` DISABLE KEYS */;
INSERT INTO `br_brands` VALUES (100001,'Samsung',1);
/*!40000 ALTER TABLE `br_brands` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ca_categories`
--

DROP TABLE IF EXISTS `ca_categories`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ca_categories` (
  `ca_id` int(11) NOT NULL AUTO_INCREMENT,
  `ca_name` varchar(50) NOT NULL,
  `ca_status` tinyint(1) NOT NULL DEFAULT 1,
  PRIMARY KEY (`ca_id`),
  UNIQUE KEY `ca_name` (`ca_name`)
) ENGINE=InnoDB AUTO_INCREMENT=100002 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ca_categories`
--

LOCK TABLES `ca_categories` WRITE;
/*!40000 ALTER TABLE `ca_categories` DISABLE KEYS */;
INSERT INTO `ca_categories` VALUES (100001,'Televisores',1);
/*!40000 ALTER TABLE `ca_categories` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ci_cities`
--

DROP TABLE IF EXISTS `ci_cities`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ci_cities` (
  `ci_id` int(11) NOT NULL AUTO_INCREMENT,
  `ci_name` varchar(50) NOT NULL,
  `ci_status` tinyint(1) NOT NULL DEFAULT 0,
  `st_id` int(11) NOT NULL,
  PRIMARY KEY (`ci_id`),
  KEY `st_id` (`st_id`),
  CONSTRAINT `ci_cities_ibfk_1` FOREIGN KEY (`st_id`) REFERENCES `st_states` (`st_id`)
) ENGINE=InnoDB AUTO_INCREMENT=100006 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ci_cities`
--

LOCK TABLES `ci_cities` WRITE;
/*!40000 ALTER TABLE `ci_cities` DISABLE KEYS */;
INSERT INTO `ci_cities` VALUES (100001,'Arandas',0,100001),(100002,'Guatemala',1,100002),(100003,'Pomona',1,100003),(100004,'El paso',1,100004),(100005,'Ciudad vieja',0,100002);
/*!40000 ALTER TABLE `ci_cities` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cu_customers`
--

DROP TABLE IF EXISTS `cu_customers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cu_customers` (
  `cu_id` int(11) NOT NULL,
  `cu_status` tinyint(1) NOT NULL DEFAULT 1,
  `cu_regdate` datetime NOT NULL DEFAULT current_timestamp(),
  `pe_id` varchar(36) NOT NULL,
  PRIMARY KEY (`cu_id`),
  KEY `pe_id` (`pe_id`),
  CONSTRAINT `cu_customers_ibfk_1` FOREIGN KEY (`pe_id`) REFERENCES `pe_persons` (`pe_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cu_customers`
--

LOCK TABLES `cu_customers` WRITE;
/*!40000 ALTER TABLE `cu_customers` DISABLE KEYS */;
INSERT INTO `cu_customers` VALUES (756169,1,'2023-06-25 02:38:06','6ee76bd0-2148-4ea4-8f81-3a49df825daa'),(926655,1,'2023-06-26 22:52:32','2277109b-a877-4a89-a6d0-9a47b2ca97c6');
/*!40000 ALTER TABLE `cu_customers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lo_locations`
--

DROP TABLE IF EXISTS `lo_locations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lo_locations` (
  `lo_id` int(11) NOT NULL AUTO_INCREMENT,
  `lo_name` varchar(50) NOT NULL,
  `lo_status` tinyint(1) NOT NULL DEFAULT 0,
  PRIMARY KEY (`lo_id`)
) ENGINE=InnoDB AUTO_INCREMENT=100003 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lo_locations`
--

LOCK TABLES `lo_locations` WRITE;
/*!40000 ALTER TABLE `lo_locations` DISABLE KEYS */;
INSERT INTO `lo_locations` VALUES (100001,'Tienda 1',1),(100002,'Tienda 2',1);
/*!40000 ALTER TABLE `lo_locations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mem_memberships`
--

DROP TABLE IF EXISTS `mem_memberships`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `mem_memberships` (
  `mem_id` int(11) NOT NULL,
  `mem_name` varchar(30) NOT NULL,
  PRIMARY KEY (`mem_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mem_memberships`
--

LOCK TABLES `mem_memberships` WRITE;
/*!40000 ALTER TABLE `mem_memberships` DISABLE KEYS */;
INSERT INTO `mem_memberships` VALUES (111529,'Empleado'),(665590,'Normal');
/*!40000 ALTER TABLE `mem_memberships` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pe_persons`
--

DROP TABLE IF EXISTS `pe_persons`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `pe_persons` (
  `pe_id` varchar(36) NOT NULL,
  `pe_fullname` varchar(100) NOT NULL,
  `pe_email` varchar(100) NOT NULL,
  `pe_phone` varchar(20) NOT NULL,
  PRIMARY KEY (`pe_id`),
  UNIQUE KEY `pe_email` (`pe_email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pe_persons`
--

LOCK TABLES `pe_persons` WRITE;
/*!40000 ALTER TABLE `pe_persons` DISABLE KEYS */;
INSERT INTO `pe_persons` VALUES ('2277109b-a877-4a89-a6d0-9a47b2ca97c6','Luis Lopez','lsdaed@gmail.com','41875568'),('6ee76bd0-2148-4ea4-8f81-3a49df825daa','Mario Perez','pilosk3@gmas.com','48548754'),('80b2ebe2-ebdc-4e49-832d-362630105862','Mayoreo Distelsa','diste@gmail.com','45875456'),('86302e2b-809c-490c-819a-367f88f4af67','Jesus Navarro','jesusns1902@gmail.com','523481468309'),('c70dd5a9-f7a8-4964-a0c5-f6310bc1dddd','Gudiel Xulu','mariano@gmail.com','58975487'),('ea01b71f-51df-4e9a-a402-018e399e611b','Baldomero Arenales','baldoarenas8@gmail.com','3524-1396'),('f98ff4d9-a90c-44a2-9a11-2c3b492dc510','Hamilton Xulu','hamidaniel16@gmail.com','4184-7857');
/*!40000 ALTER TABLE `pe_persons` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pm_paymentmethods`
--

DROP TABLE IF EXISTS `pm_paymentmethods`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `pm_paymentmethods` (
  `pm_id` int(11) NOT NULL AUTO_INCREMENT,
  `pm_name` varchar(50) NOT NULL,
  `pm_per` float NOT NULL,
  `pm_status` tinyint(1) NOT NULL DEFAULT 0,
  PRIMARY KEY (`pm_id`)
) ENGINE=InnoDB AUTO_INCREMENT=100005 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pm_paymentmethods`
--

LOCK TABLES `pm_paymentmethods` WRITE;
/*!40000 ALTER TABLE `pm_paymentmethods` DISABLE KEYS */;
INSERT INTO `pm_paymentmethods` VALUES (100001,'Efectivo',0,1),(100002,'Tarjeta credito/debito',5,1),(100003,'Deposito bancario',0,1),(100004,'Transferencia',0,1);
/*!40000 ALTER TABLE `pm_paymentmethods` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pr_products`
--

DROP TABLE IF EXISTS `pr_products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `pr_products` (
  `pr_id` varchar(16) NOT NULL,
  `pr_barcode` varchar(50) NOT NULL,
  `pr_name` varchar(50) NOT NULL,
  `pr_model` varchar(50) NOT NULL,
  `pr_description` varchar(150) NOT NULL,
  `pr_cost` float NOT NULL,
  `pr_price` float NOT NULL,
  `pr_status` tinyint(1) NOT NULL DEFAULT 0,
  `pr_regdate` datetime NOT NULL DEFAULT current_timestamp(),
  `ca_id` int(11) NOT NULL,
  `br_id` int(11) NOT NULL,
  `pv_id` int(11) NOT NULL,
  PRIMARY KEY (`pr_id`),
  UNIQUE KEY `pr_barcode` (`pr_barcode`),
  KEY `ca_id` (`ca_id`),
  KEY `br_id` (`br_id`),
  KEY `pv_id` (`pv_id`),
  CONSTRAINT `pr_products_ibfk_1` FOREIGN KEY (`ca_id`) REFERENCES `ca_categories` (`ca_id`),
  CONSTRAINT `pr_products_ibfk_2` FOREIGN KEY (`br_id`) REFERENCES `br_brands` (`br_id`),
  CONSTRAINT `pr_products_ibfk_3` FOREIGN KEY (`pv_id`) REFERENCES `pv_providers` (`pv_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pr_products`
--

LOCK TABLES `pr_products` WRITE;
/*!40000 ALTER TABLE `pr_products` DISABLE KEYS */;
INSERT INTO `pr_products` VALUES ('AC242A038E61414B','45875456','Televisor samsung','55lk3nj','telvsi',3200,4500,1,'2023-06-25 02:50:43',100001,100001,231171);
/*!40000 ALTER TABLE `pr_products` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pv_providers`
--

DROP TABLE IF EXISTS `pv_providers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `pv_providers` (
  `pv_id` int(11) NOT NULL,
  `pv_status` tinyint(1) NOT NULL DEFAULT 1,
  `pv_regdate` datetime NOT NULL DEFAULT current_timestamp(),
  `pe_id` varchar(36) NOT NULL,
  PRIMARY KEY (`pv_id`) USING BTREE,
  KEY `pe_id` (`pe_id`),
  CONSTRAINT `pv_providers_ibfk_1` FOREIGN KEY (`pe_id`) REFERENCES `pe_persons` (`pe_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pv_providers`
--

LOCK TABLES `pv_providers` WRITE;
/*!40000 ALTER TABLE `pv_providers` DISABLE KEYS */;
INSERT INTO `pv_providers` VALUES (231171,1,'2023-06-25 02:45:28','80b2ebe2-ebdc-4e49-832d-362630105862');
/*!40000 ALTER TABLE `pv_providers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sa_sales`
--

DROP TABLE IF EXISTS `sa_sales`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sa_sales` (
  `sa_id` varchar(36) NOT NULL,
  `sa_subtotal` float NOT NULL,
  `sa_discount` float NOT NULL,
  `sa_amountpayments` int(11) NOT NULL,
  `sa_days` int(11) NOT NULL,
  `sa_status` tinyint(1) NOT NULL DEFAULT 1,
  `sa_regdate` datetime NOT NULL DEFAULT current_timestamp(),
  `lo_id` int(11) NOT NULL,
  `ts_id` int(11) NOT NULL,
  `cu_id` int(11) DEFAULT NULL,
  `us_id` int(11) NOT NULL,
  PRIMARY KEY (`sa_id`),
  KEY `us_id` (`us_id`),
  KEY `lo_id` (`lo_id`),
  KEY `ts_id` (`ts_id`),
  KEY `cu_id` (`cu_id`),
  CONSTRAINT `sa_sales_ibfk_1` FOREIGN KEY (`lo_id`) REFERENCES `lo_locations` (`lo_id`),
  CONSTRAINT `sa_sales_ibfk_2` FOREIGN KEY (`ts_id`) REFERENCES `ts_typessales` (`ts_id`),
  CONSTRAINT `sa_sales_ibfk_3` FOREIGN KEY (`cu_id`) REFERENCES `cu_customers` (`cu_id`),
  CONSTRAINT `sa_sales_ibfk_4` FOREIGN KEY (`us_id`) REFERENCES `us_users` (`us_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sa_sales`
--

LOCK TABLES `sa_sales` WRITE;
/*!40000 ALTER TABLE `sa_sales` DISABLE KEYS */;
INSERT INTO `sa_sales` VALUES ('128a5826-b704-431b-9d6c-b155140a582e',4500,90,1,0,0,'2023-06-27 21:13:41',100002,100001,756169,263899),('66bb4a1d-4e59-4467-a7ee-50b27f4869f9',4500,0,1,0,0,'2023-06-28 00:20:00',100001,100001,NULL,206506),('7de8df02-89c9-4ba4-9246-4edbf7a82dcf',4500,0,10,0,0,'2023-06-27 20:57:44',100001,100002,926655,263899),('ab090481-76a5-4419-9d7c-fc955303e2c2',4500,0,20,30,0,'2023-06-28 00:08:58',100001,100002,NULL,206506),('ddedac94-1b77-411c-812f-d393f2c11787',4500,0,10,0,0,'2023-06-27 21:25:56',100001,100002,926655,263899),('ecf2b985-41a2-4d5d-968e-07a23c525806',4500,0,12,30,0,'2023-06-27 22:50:24',100001,100002,926655,181549);
/*!40000 ALTER TABLE `sa_sales` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sd_saledetails`
--

DROP TABLE IF EXISTS `sd_saledetails`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sd_saledetails` (
  `sd_id` int(11) NOT NULL AUTO_INCREMENT,
  `sd_price` float NOT NULL,
  `sd_cost` float NOT NULL,
  `sd_quantity` float NOT NULL,
  `pr_id` varchar(16) NOT NULL,
  `sa_id` varchar(36) NOT NULL,
  PRIMARY KEY (`sd_id`),
  KEY `pr_id` (`pr_id`),
  KEY `sa_id` (`sa_id`),
  CONSTRAINT `sd_saledetails_ibfk_1` FOREIGN KEY (`pr_id`) REFERENCES `pr_products` (`pr_id`),
  CONSTRAINT `sd_saledetails_ibfk_2` FOREIGN KEY (`sa_id`) REFERENCES `sa_sales` (`sa_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10000007 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sd_saledetails`
--

LOCK TABLES `sd_saledetails` WRITE;
/*!40000 ALTER TABLE `sd_saledetails` DISABLE KEYS */;
INSERT INTO `sd_saledetails` VALUES (10000001,4500,3200,1,'AC242A038E61414B','7de8df02-89c9-4ba4-9246-4edbf7a82dcf'),(10000002,4500,3200,1,'AC242A038E61414B','128a5826-b704-431b-9d6c-b155140a582e'),(10000003,4500,3200,1,'AC242A038E61414B','ddedac94-1b77-411c-812f-d393f2c11787'),(10000004,4500,3200,1,'AC242A038E61414B','ecf2b985-41a2-4d5d-968e-07a23c525806'),(10000005,4500,3200,1,'AC242A038E61414B','ab090481-76a5-4419-9d7c-fc955303e2c2'),(10000006,4500,3200,1,'AC242A038E61414B','66bb4a1d-4e59-4467-a7ee-50b27f4869f9');
/*!40000 ALTER TABLE `sd_saledetails` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sess_usersessions`
--

DROP TABLE IF EXISTS `sess_usersessions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sess_usersessions` (
  `sess_id` varchar(36) NOT NULL,
  `sess_online` tinyint(1) NOT NULL DEFAULT 1,
  `sess_twofacauth` tinyint(1) NOT NULL DEFAULT 1,
  `sess_useragent` varchar(150) NOT NULL,
  `sess_date` datetime NOT NULL DEFAULT current_timestamp(),
  `us_id` int(11) NOT NULL,
  PRIMARY KEY (`sess_id`),
  KEY `us_id` (`us_id`),
  CONSTRAINT `sess_usersessions_ibfk_1` FOREIGN KEY (`us_id`) REFERENCES `us_users` (`us_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sess_usersessions`
--

LOCK TABLES `sess_usersessions` WRITE;
/*!40000 ALTER TABLE `sess_usersessions` DISABLE KEYS */;
INSERT INTO `sess_usersessions` VALUES ('5e9ab751-1354-4b7c-a954-bc441d9c287a',0,1,'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36','2023-06-26 04:16:03',206506),('61910809-0b16-4a99-a619-617b71d8405e',1,1,'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36','2023-06-28 00:28:03',206506),('8392274d-877d-4ee7-bf8a-f4d978310871',0,1,'Mozilla/5.0 (iPhone; CPU iPhone OS 16_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5.1 Mobile/15E148 Safari/604.1','2023-06-27 22:24:19',263899),('87d0c367-4261-4e4c-936e-939147fd4e8d',0,1,'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36','2023-06-27 14:20:20',263899),('885f0b6b-613c-4eeb-a7b3-c41af05d8a6b',0,1,'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36','2023-06-27 23:03:48',263899),('a53bad48-c8a9-4b65-aef3-0f98c634e9f1',0,1,'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36','2023-06-28 00:06:13',181549);
/*!40000 ALTER TABLE `sess_usersessions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sp_salepayments`
--

DROP TABLE IF EXISTS `sp_salepayments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sp_salepayments` (
  `sp_id` int(11) NOT NULL AUTO_INCREMENT,
  `sp_no` int(11) DEFAULT NULL,
  `sp_subtotal` float NOT NULL,
  `sp_commission` float NOT NULL,
  `sp_pay` float NOT NULL,
  `sp_limitdate` date DEFAULT NULL,
  `sp_regdate` datetime DEFAULT NULL,
  `pm_id` int(11) DEFAULT NULL,
  `us_id` int(11) DEFAULT NULL,
  `sa_id` varchar(36) NOT NULL,
  PRIMARY KEY (`sp_id`),
  UNIQUE KEY `sp_no` (`sp_no`),
  KEY `pm_id` (`pm_id`),
  KEY `sa_id` (`sa_id`),
  KEY `us_id` (`us_id`),
  CONSTRAINT `sp_salepayments_ibfk_1` FOREIGN KEY (`pm_id`) REFERENCES `pm_paymentmethods` (`pm_id`),
  CONSTRAINT `sp_salepayments_ibfk_2` FOREIGN KEY (`sa_id`) REFERENCES `sa_sales` (`sa_id`),
  CONSTRAINT `sp_salepayments_ibfk_3` FOREIGN KEY (`us_id`) REFERENCES `us_users` (`us_id`)
) ENGINE=InnoDB AUTO_INCREMENT=1000058 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sp_salepayments`
--

LOCK TABLES `sp_salepayments` WRITE;
/*!40000 ALTER TABLE `sp_salepayments` DISABLE KEYS */;
INSERT INTO `sp_salepayments` VALUES (1000001,NULL,450,0,0,'2023-06-27',NULL,NULL,NULL,'7de8df02-89c9-4ba4-9246-4edbf7a82dcf'),(1000002,NULL,450,0,0,'2023-06-27',NULL,NULL,NULL,'7de8df02-89c9-4ba4-9246-4edbf7a82dcf'),(1000003,NULL,450,0,0,'2023-06-27',NULL,NULL,NULL,'7de8df02-89c9-4ba4-9246-4edbf7a82dcf'),(1000004,NULL,450,0,0,'2023-06-27',NULL,NULL,NULL,'7de8df02-89c9-4ba4-9246-4edbf7a82dcf'),(1000005,NULL,450,0,0,'2023-06-27',NULL,NULL,NULL,'7de8df02-89c9-4ba4-9246-4edbf7a82dcf'),(1000006,NULL,450,0,0,'2023-06-27',NULL,NULL,NULL,'7de8df02-89c9-4ba4-9246-4edbf7a82dcf'),(1000007,NULL,450,0,0,'2023-06-27',NULL,NULL,NULL,'7de8df02-89c9-4ba4-9246-4edbf7a82dcf'),(1000008,NULL,450,0,0,'2023-06-27',NULL,NULL,NULL,'7de8df02-89c9-4ba4-9246-4edbf7a82dcf'),(1000009,NULL,450,0,0,'2023-06-27',NULL,NULL,NULL,'7de8df02-89c9-4ba4-9246-4edbf7a82dcf'),(1000010,NULL,450,0,200,'2023-08-27',NULL,NULL,NULL,'7de8df02-89c9-4ba4-9246-4edbf7a82dcf'),(1000011,1000001,4410,0,4410,'2023-06-27','2023-06-27 21:13:41',100001,263899,'128a5826-b704-431b-9d6c-b155140a582e'),(1000012,1000002,450,0,450,'2023-06-27','2023-06-27 21:25:56',100001,263899,'ddedac94-1b77-411c-812f-d393f2c11787'),(1000013,NULL,450,0,450,'2023-06-27',NULL,NULL,NULL,'ddedac94-1b77-411c-812f-d393f2c11787'),(1000014,NULL,450,0,0,'2023-06-27',NULL,NULL,NULL,'ddedac94-1b77-411c-812f-d393f2c11787'),(1000015,NULL,450,0,0,'2023-06-27',NULL,NULL,NULL,'ddedac94-1b77-411c-812f-d393f2c11787'),(1000016,NULL,450,0,0,'2023-06-27',NULL,NULL,NULL,'ddedac94-1b77-411c-812f-d393f2c11787'),(1000017,NULL,450,0,0,'2023-06-27',NULL,NULL,NULL,'ddedac94-1b77-411c-812f-d393f2c11787'),(1000018,1000005,450,0,450,'2023-06-27','2023-06-27 21:47:33',100001,263899,'ddedac94-1b77-411c-812f-d393f2c11787'),(1000019,1000004,450,0,450,'2023-06-27','2023-06-27 21:47:01',100001,263899,'ddedac94-1b77-411c-812f-d393f2c11787'),(1000020,1000003,450,0,450,'2023-06-27','2023-06-27 21:46:25',100001,263899,'ddedac94-1b77-411c-812f-d393f2c11787'),(1000021,NULL,450,0,0,'2023-06-27',NULL,NULL,NULL,'ddedac94-1b77-411c-812f-d393f2c11787'),(1000022,1000006,375,0,375,'2023-07-27','2023-06-27 22:50:24',100001,181549,'ecf2b985-41a2-4d5d-968e-07a23c525806'),(1000023,1000008,175,0,175,'2023-08-26','2023-06-27 22:55:26',100001,181549,'ecf2b985-41a2-4d5d-968e-07a23c525806'),(1000024,1000009,175,0,175,'2023-09-25','2023-06-27 22:58:11',100001,181549,'ecf2b985-41a2-4d5d-968e-07a23c525806'),(1000025,1000010,375,0,25,'2023-10-25','2023-06-27 22:58:11',100001,181549,'ecf2b985-41a2-4d5d-968e-07a23c525806'),(1000026,NULL,375,0,0,'2023-11-24',NULL,NULL,NULL,'ecf2b985-41a2-4d5d-968e-07a23c525806'),(1000027,NULL,375,0,0,'2023-12-24',NULL,NULL,NULL,'ecf2b985-41a2-4d5d-968e-07a23c525806'),(1000028,NULL,375,0,0,'2024-01-23',NULL,NULL,NULL,'ecf2b985-41a2-4d5d-968e-07a23c525806'),(1000029,NULL,375,0,0,'2024-02-22',NULL,NULL,NULL,'ecf2b985-41a2-4d5d-968e-07a23c525806'),(1000030,NULL,375,0,0,'2024-03-23',NULL,NULL,NULL,'ecf2b985-41a2-4d5d-968e-07a23c525806'),(1000031,NULL,275,0,0,'2024-04-22',NULL,NULL,NULL,'ecf2b985-41a2-4d5d-968e-07a23c525806'),(1000032,NULL,375,0,0,'2024-05-22',NULL,NULL,NULL,'ecf2b985-41a2-4d5d-968e-07a23c525806'),(1000033,NULL,375,0,0,'2024-06-21',NULL,NULL,NULL,'ecf2b985-41a2-4d5d-968e-07a23c525806'),(1000034,1000007,200,0,200,'2023-07-27','2023-06-27 22:55:26',100001,181549,'ecf2b985-41a2-4d5d-968e-07a23c525806'),(1000035,NULL,100,0,0,'2024-05-22',NULL,NULL,NULL,'ecf2b985-41a2-4d5d-968e-07a23c525806'),(1000036,NULL,200,0,0,'2023-10-26',NULL,NULL,NULL,'ecf2b985-41a2-4d5d-968e-07a23c525806'),(1000037,1000011,225,0,100,'2023-07-28','2023-06-28 00:08:58',100001,206506,'ab090481-76a5-4419-9d7c-fc955303e2c2'),(1000038,NULL,225,0,0,'2023-08-27',NULL,NULL,NULL,'ab090481-76a5-4419-9d7c-fc955303e2c2'),(1000039,NULL,225,0,0,'2023-01-26',NULL,NULL,NULL,'ab090481-76a5-4419-9d7c-fc955303e2c2'),(1000040,NULL,225,0,0,'2023-10-26',NULL,NULL,NULL,'ab090481-76a5-4419-9d7c-fc955303e2c2'),(1000041,NULL,225,0,0,'2023-11-25',NULL,NULL,NULL,'ab090481-76a5-4419-9d7c-fc955303e2c2'),(1000042,NULL,225,0,0,'2023-12-25',NULL,NULL,NULL,'ab090481-76a5-4419-9d7c-fc955303e2c2'),(1000043,NULL,225,0,0,'2024-01-24',NULL,NULL,NULL,'ab090481-76a5-4419-9d7c-fc955303e2c2'),(1000044,NULL,225,0,0,'2024-02-23',NULL,NULL,NULL,'ab090481-76a5-4419-9d7c-fc955303e2c2'),(1000045,NULL,225,0,0,'2024-03-24',NULL,NULL,NULL,'ab090481-76a5-4419-9d7c-fc955303e2c2'),(1000046,NULL,225,0,0,'2024-04-23',NULL,NULL,NULL,'ab090481-76a5-4419-9d7c-fc955303e2c2'),(1000047,NULL,225,0,0,'2024-05-23',NULL,NULL,NULL,'ab090481-76a5-4419-9d7c-fc955303e2c2'),(1000048,NULL,225,0,0,'2024-06-22',NULL,NULL,NULL,'ab090481-76a5-4419-9d7c-fc955303e2c2'),(1000049,NULL,225,0,0,'2024-07-22',NULL,NULL,NULL,'ab090481-76a5-4419-9d7c-fc955303e2c2'),(1000050,NULL,225,0,0,'2024-08-21',NULL,NULL,NULL,'ab090481-76a5-4419-9d7c-fc955303e2c2'),(1000051,NULL,225,0,0,'2024-09-20',NULL,NULL,NULL,'ab090481-76a5-4419-9d7c-fc955303e2c2'),(1000052,NULL,225,0,0,'2024-10-20',NULL,NULL,NULL,'ab090481-76a5-4419-9d7c-fc955303e2c2'),(1000053,NULL,225,0,0,'2024-11-19',NULL,NULL,NULL,'ab090481-76a5-4419-9d7c-fc955303e2c2'),(1000054,NULL,225,0,0,'2024-12-19',NULL,NULL,NULL,'ab090481-76a5-4419-9d7c-fc955303e2c2'),(1000055,NULL,225,0,0,'2025-01-18',NULL,NULL,NULL,'ab090481-76a5-4419-9d7c-fc955303e2c2'),(1000056,NULL,225,0,0,'2025-02-17',NULL,NULL,NULL,'ab090481-76a5-4419-9d7c-fc955303e2c2'),(1000057,1000012,4500,0,4500,'2023-06-28','2023-06-28 00:20:00',100001,206506,'66bb4a1d-4e59-4467-a7ee-50b27f4869f9');
/*!40000 ALTER TABLE `sp_salepayments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `st_states`
--

DROP TABLE IF EXISTS `st_states`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `st_states` (
  `st_id` int(11) NOT NULL AUTO_INCREMENT,
  `st_name` varchar(50) NOT NULL,
  `st_status` tinyint(1) NOT NULL DEFAULT 0,
  PRIMARY KEY (`st_id`)
) ENGINE=InnoDB AUTO_INCREMENT=100005 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `st_states`
--

LOCK TABLES `st_states` WRITE;
/*!40000 ALTER TABLE `st_states` DISABLE KEYS */;
INSERT INTO `st_states` VALUES (100001,'Jalisco',0),(100002,'Sacatepequez',1),(100003,'California',1),(100004,'Texas',1);
/*!40000 ALTER TABLE `st_states` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ts_typessales`
--

DROP TABLE IF EXISTS `ts_typessales`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ts_typessales` (
  `ts_id` int(11) NOT NULL AUTO_INCREMENT,
  `ts_name` varchar(50) NOT NULL,
  PRIMARY KEY (`ts_id`)
) ENGINE=InnoDB AUTO_INCREMENT=100004 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ts_typessales`
--

LOCK TABLES `ts_typessales` WRITE;
/*!40000 ALTER TABLE `ts_typessales` DISABLE KEYS */;
INSERT INTO `ts_typessales` VALUES (100001,'De contado'),(100002,'Abonos'),(100003,'Fuera de tienda');
/*!40000 ALTER TABLE `ts_typessales` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `us_users`
--

DROP TABLE IF EXISTS `us_users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `us_users` (
  `us_id` int(11) NOT NULL,
  `us_password` varchar(70) NOT NULL,
  `us_permissions` text DEFAULT NULL,
  `us_status` tinyint(1) NOT NULL DEFAULT 0,
  `us_regdate` datetime NOT NULL DEFAULT current_timestamp(),
  `pe_id` varchar(36) NOT NULL,
  `mem_id` int(11) NOT NULL DEFAULT 665590,
  PRIMARY KEY (`us_id`),
  KEY `mem_id` (`mem_id`),
  KEY `pe_id` (`pe_id`),
  CONSTRAINT `us_users_ibfk_1` FOREIGN KEY (`mem_id`) REFERENCES `mem_memberships` (`mem_id`),
  CONSTRAINT `us_users_ibfk_2` FOREIGN KEY (`pe_id`) REFERENCES `pe_persons` (`pe_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `us_users`
--

LOCK TABLES `us_users` WRITE;
/*!40000 ALTER TABLE `us_users` DISABLE KEYS */;
INSERT INTO `us_users` VALUES (181549,'$2b$12$OpB5dQXT2dBErSIPlg3AJuUzvdrFSqtdMUws426Pb/h6I17vs9qLy','[\'/pos/statistics\', \'/pos/manage/customers\', \'/pos/manage/products\', \'/pos/manage/providers\', \'/pos/manage/categories\', \'/pos/manage/brands\', \'/pos/manage/sales\', \'/pos/manage/addresses\', \'/pos/manage/sale/payments\', \'/pos/manage/sale/payments/edit\']',1,'2023-06-25 23:59:54','f98ff4d9-a90c-44a2-9a11-2c3b492dc510',111529),(206506,'$2b$12$c5QpRpxLh/OYZNM9M5KCQecnCpsKqs45WK1QHJscUN6MFpF45dsnC','[\'/pos/statistics\', \'/pos/manage/users\', \'/pos/manage/customers\', \'/pos/manage/paymentmethods\', \'/pos/manage/locations\', \'/pos/manage/products\', \'/pos/manage/providers\', \'/pos/manage/categories\', \'/pos/manage/brands\', \'/pos/manage/cities\', \'/pos/manage/states\', \'/pos/manage/sales\', \'/pos/manage/dbbackup\', \'/pos/manage/addresses\', \'/pos/manage/sale/payments\', \'/pos/manage/sale/payments/edit\']',1,'2023-06-21 13:15:07','86302e2b-809c-490c-819a-367f88f4af67',111529),(263899,'$2b$12$yVDiidAQtukMm1gBY.OL1.s7m4scr47NCzzWGtYmKjMtrRyOC.weC','[\'/pos/statistics\', \'/pos/manage/users\', \'/pos/manage/customers\', \'/pos/manage/paymentmethods\', \'/pos/manage/locations\', \'/pos/manage/products\', \'/pos/manage/providers\', \'/pos/manage/categories\', \'/pos/manage/brands\', \'/pos/manage/cities\', \'/pos/manage/states\', \'/pos/manage/sales\', \'/pos/manage/dbbackup\', \'/pos/manage/addresses\', \'/pos/manage/sale/payments\', \'/pos/manage/sale/payments/edit\']',1,'2023-06-23 11:32:06','ea01b71f-51df-4e9a-a402-018e399e611b',111529),(791950,'$2b$12$KIzwtHxeY.h97KqM1xcmVeKiDa5ZOe.dCDQ89zG9FVymEJnJfSKVa','[\'/pos/manage/customers\', \'/pos/manage/sales\', \'/pos/manage/addresses\', \'/pos/manage/sale/payments\']',1,'2023-06-25 23:58:58','c70dd5a9-f7a8-4964-a0c5-f6310bc1dddd',111529);
/*!40000 ALTER TABLE `us_users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-06-28  0:28:08
