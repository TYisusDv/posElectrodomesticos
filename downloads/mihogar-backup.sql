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
  `ad_dpi` varchar(20) NOT NULL,
  `ad_fullname` varchar(100) NOT NULL,
  `ad_address` varchar(100) NOT NULL,
  `ad_relationship` varchar(50) NOT NULL,
  `ad_phone` varchar(20) NOT NULL,
  `ad_workaddress` varchar(150) NOT NULL,
  `ad_status` tinyint(1) NOT NULL DEFAULT 1,
  `ad_regdate` datetime NOT NULL DEFAULT current_timestamp(),
  `at_id` int(11) NOT NULL,
  `ci_id` int(11) NOT NULL,
  `pe_id` varchar(36) NOT NULL,
  PRIMARY KEY (`ad_id`),
  KEY `pe_id` (`pe_id`),
  KEY `ci_id` (`ci_id`),
  KEY `at_id` (`at_id`),
  CONSTRAINT `ad_addresses_ibfk_1` FOREIGN KEY (`pe_id`) REFERENCES `pe_persons` (`pe_id`),
  CONSTRAINT `ad_addresses_ibfk_2` FOREIGN KEY (`ci_id`) REFERENCES `ci_cities` (`ci_id`),
  CONSTRAINT `ad_addresses_ibfk_3` FOREIGN KEY (`at_id`) REFERENCES `at_addresstypes` (`at_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ad_addresses`
--

LOCK TABLES `ad_addresses` WRITE;
/*!40000 ALTER TABLE `ad_addresses` DISABLE KEYS */;
INSERT INTO `ad_addresses` VALUES ('54c25d83-d22c-4909-b5e2-1b2ad62d047a','3656046-4','Mario Andrade','Km 38.5 carretera interamericana','','5902-1958','',1,'2023-07-08 19:49:31',1001,1002,'00168a7f-444c-4d59-8a9f-bcb3bbc62da8'),('7fbf5186-2225-4c36-9935-62504571931a','97976-7','Kevin Rodolfo Herrera Garza','1 calle 7-66 zona 9 edificio plaza uno','','5710-2562','Guatemala',1,'2023-07-08 19:42:55',1001,1001,'0f3ab69b-b9ef-45b8-b6d5-2c3b983b2f41'),('cd7d0733-7a27-47cd-9a2c-4f5fe56f4b6a','0','Raul Guevara','Av petapa 34-17 zona 12','','000-000','Guatemala',1,'2023-07-08 19:45:39',1001,1001,'36e90fb9-583d-474f-ad85-08f4eacf05ad');
/*!40000 ALTER TABLE `ad_addresses` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `at_addresstypes`
--

DROP TABLE IF EXISTS `at_addresstypes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `at_addresstypes` (
  `at_id` int(11) NOT NULL AUTO_INCREMENT,
  `at_name` varchar(50) NOT NULL,
  PRIMARY KEY (`at_id`)
) ENGINE=InnoDB AUTO_INCREMENT=1004 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `at_addresstypes`
--

LOCK TABLES `at_addresstypes` WRITE;
/*!40000 ALTER TABLE `at_addresstypes` DISABLE KEYS */;
INSERT INTO `at_addresstypes` VALUES (1001,'Dirección'),(1002,'Referencia'),(1003,'Fiador');
/*!40000 ALTER TABLE `at_addresstypes` ENABLE KEYS */;
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
) ENGINE=InnoDB AUTO_INCREMENT=1031 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `br_brands`
--

LOCK TABLES `br_brands` WRITE;
/*!40000 ALTER TABLE `br_brands` DISABLE KEYS */;
INSERT INTO `br_brands` VALUES (1001,'Samsung',1),(1002,'Lg',1),(1003,'Rca',1),(1004,'Hisense',1),(1005,'Toshiba',1),(1006,'Compaq',1),(1007,'Acros',1),(1008,'Mabe',1),(1009,'Oster',1),(1010,'Iml',1),(1011,'Grs',1),(1012,'Whirlpool',1),(1013,'Frigidaire',1),(1014,'Black & decker',1),(1015,'Aiwa',1),(1016,'Sony',1),(1017,'Muebles helen',1),(1018,'Olympia',1),(1019,'Facenco',1),(1020,'Remington',1),(1021,'Maiesta',1),(1022,'Hamilton beach',1),(1023,'Proctor silex',1),(1024,'Picca',1),(1025,'Motorola',1),(1026,'Hp',1),(1027,'Black &amp; decker',1),(1028,'Genico',1),(1029,'Hot plate',1),(1030,'Shimano',1);
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
) ENGINE=InnoDB AUTO_INCREMENT=1037 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ca_categories`
--

LOCK TABLES `ca_categories` WRITE;
/*!40000 ALTER TABLE `ca_categories` DISABLE KEYS */;
INSERT INTO `ca_categories` VALUES (1001,'Televisores',1),(1002,'Estufas',1),(1003,'Refrigeradoras',1),(1004,'Lavadoras',1),(1005,'Microondas',1),(1006,'Horno tostador',1),(1007,'Plancha de ropa',1),(1008,'Licuadoras',1),(1009,'Barra de sonido',1),(1010,'Bocina',1),(1011,'Torre de sonido',1),(1012,'Minicomponente',1),(1013,'Muebles',1),(1014,'Camas',1),(1015,'Belleza',1),(1016,'Soporte tv',1),(1017,'Cafeteras',1),(1018,'Percoladoras',1),(1019,'Batidoras',1),(1020,'Procesador de alimentos',1),(1021,'Olla de presion',1),(1022,'Utileria de cocina',1),(1023,'Ventiladores',1),(1024,'Celulares',1),(1025,'Computadoras',1),(1026,'Tablet',1),(1027,'Almohada',1),(1028,'Olla electrica',1),(1029,'Frigobar',1),(1030,'Congelador horizontal',1),(1031,'Licuadora portatil',1),(1032,'Estufas electricas',1),(1033,'Computadoras laptop',1),(1034,'Estufas de mesa',1),(1035,'Funda para cama',1),(1036,'Bicicletas',1);
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
) ENGINE=InnoDB AUTO_INCREMENT=1003 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ci_cities`
--

LOCK TABLES `ci_cities` WRITE;
/*!40000 ALTER TABLE `ci_cities` DISABLE KEYS */;
INSERT INTO `ci_cities` VALUES (1001,'Guatemala',1,1001),(1002,'',0,1002);
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
  `cu_dpi` varchar(20) NOT NULL,
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
INSERT INTO `cu_customers` VALUES (217295,'000',1,'2023-07-09 01:07:23','10b9d983-db1e-4606-b069-368682b5afa1');
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
) ENGINE=InnoDB AUTO_INCREMENT=1003 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lo_locations`
--

LOCK TABLES `lo_locations` WRITE;
/*!40000 ALTER TABLE `lo_locations` DISABLE KEYS */;
INSERT INTO `lo_locations` VALUES (1001,'Tienda 1',1),(1002,'Tienda 2',1);
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
INSERT INTO `pe_persons` VALUES ('00168a7f-444c-4d59-8a9f-bcb3bbc62da8','Multiesponjas, Sociedad Anonima','sincorreo@gmail.com','5902-1958'),('04c85492-590c-4861-a392-cc17cb76be9c','Sepsa','sin2@gmail.com','4211-1678'),('0634147a-a9ee-48d2-a3a5-7c972c6ce94c','Agencias Way','sincorreo1@gmail.com','000-000'),('0f3ab69b-b9ef-45b8-b6d5-2c3b983b2f41','Mayoreo Distelsa','kherrera@distelsa.com.gt','5710-2562'),('10b9d983-db1e-4606-b069-368682b5afa1','Jose Alejandro Gonzalez Romero','sincorreo1@gsail.com','000-000'),('116da2fb-2ac9-483a-8c6b-2f46b4b4b6e2','Diveco, Sociedad Anonima','sin@gmail.com','4013-9968'),('11984714-7fdd-402c-9e96-ae8e14a563af','Slc Trade','aguerra@slc.com.gt','3424-4526'),('34c2315d-b0b3-4be1-862f-1db6168d5880','Genico','genico@gmail.com','000-000'),('36e90fb9-583d-474f-ad85-08f4eacf05ad','Bodegangas','sac@bodegangas.com.gt','2474-2851'),('54786e44-eb51-4b14-ad95-d54539cd0a0f','Muebles Helen','muebles_helen@hotmail.com','4883-1398'),('64116745-badb-4eda-9a55-246cb34d380b','El Gallo Mas Gallo','atencionalcliente@grupom.net','7882-4081'),('837f62ed-560d-464c-ba2a-06ddf76e1c03','Tecno Facil Outlet','tf.outletsanjuan@distelsa.com.gt','2432-6286'),('86302e2b-809c-490c-819a-367f88f4af67','Jesus Navarro','jesusns1902@gmail.com','523481468309'),('b03edfb9-84ae-482c-a600-432cfdad6aa9','La Bodegona','sincorre@gmail.com','5454-5025'),('c70dd5a9-f7a8-4964-a0c5-f6310bc1dddd','Gudiel Xulu','mariano@gmail.com','58975487'),('dab4a868-dd48-4363-bcaa-14619938406e','Distribuidora Acuario','4@gmaiul.com','5413-3643'),('e63803eb-bba1-4191-917a-8320849fbd20','Billion Home','sinjo2@gmail.com','000-000'),('ea01b71f-51df-4e9a-a402-018e399e611b','Baldomero Arenales','baldoarenas8@gmail.com','3524-1396'),('f98ff4d9-a90c-44a2-9a11-2c3b492dc510','Hamilton Xulu','hamidaniel16@gmail.com','4184-7857');
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
) ENGINE=InnoDB AUTO_INCREMENT=1005 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pm_paymentmethods`
--

LOCK TABLES `pm_paymentmethods` WRITE;
/*!40000 ALTER TABLE `pm_paymentmethods` DISABLE KEYS */;
INSERT INTO `pm_paymentmethods` VALUES (1001,'Efectivo',0,1),(1002,'Tarjeta credito/debito',5,1),(1003,'Deposito bancario',0,1),(1004,'Transferencia',0,1);
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
  `pr_name` varchar(150) NOT NULL,
  `pr_model` varchar(50) NOT NULL,
  `pr_description` text NOT NULL,
  `pr_cost` float NOT NULL,
  `pr_price` float NOT NULL,
  `pr_pricetopayments` float NOT NULL,
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
INSERT INTO `pr_products` VALUES ('04BBC945496F4A08','7','LICUADORA OSTER 8 VELOCIDADES VASO DE VIDRIO BLANCO','BLSTMG-W00','8 velocidades, vaso de vidrio.',340,490,590,1,'2023-07-08 23:01:44',1008,1009,170372),('0508603A57FE4AB9','50','ESTUFA CON HORNO ACROS 20\" NEGRA TOP NEGRO','LNAW1001B00','4 hornillas color negro',1460,2050,3050,1,'2023-07-11 17:18:08',1002,1007,170372),('08880B600B0D49AF','53','PLANCHA OSTER A VAPOR CON SUELA ANTIADHERENTE PALO ROSA','GCSTBS3801','a vapor suela antiadherente palo rosa',170,300,360,1,'2023-07-11 17:21:31',1007,1009,571770),('08E8815178F64A8B','12','ROPERO NOVO MUEBLES HELEN','ROPNOVO','ropero',2400,3300,4620,1,'2023-07-08 23:11:23',1013,1017,813063),('098E6298EE46420F','26','LICUADORA BLACK&DECKER 10 VELOCIDADES JARRA DE PLASTICO ROJO','BLBD210PP','10 velocidades , roja , jarra vidrio.',209.3,420,500,1,'2023-07-08 23:30:30',1008,1027,415958),('0A53251C5C4646DA','1','ESTUFA CON HORNO OSTER 20\" GRAFITO TOP INOXIDABLE','OS-GSBCT20BS','ESTUFA CON HORNO OSTER 20\" GRAFITO TOP INOXIDABLE',1260,1920,2950,1,'2023-07-08 22:42:32',1002,1009,571770),('0C5FACC960FD4D23','48','BARRA DE SONIDO AIWA 40 W (BT/AUX/USB/HDMI)','AWSBH1','40 watts con bluetooth auxiliar usb y hdmi',595,850,1380,1,'2023-07-11 17:15:46',1009,1015,170372),('0CE2F51125A247F2','93','ESTUFA DE MESA IML 4 HORNILLAS MARFIL TOP INOXIDABLE','C-4M','4 hornillas de mesa',422,650,930,1,'2023-07-11 18:11:21',1034,1010,571770),('0D34DEAE83F74276','27','BATIDORA MANUAL OSTER 6 VELOCIDADES BLANCA','FPSTHM3532','6 velocidades, blanca.',315,425,500,1,'2023-07-08 23:31:34',1019,1009,160039),('0E1BF3CD91F54847','51','ESTUFA CON HORNO RCA 20\" GRIS TOP INOXIDABLE','RCCR24','4 hornillas gris inoxidable',1349,2000,3000,1,'2023-07-11 17:19:11',1002,1003,571770),('119A0F8D25484193','38','TELEVISOR TOSHIBA 32\" SMART HD LED','32V35KB','televisor de 32 pulgadas high definition led',1676.92,2490,3350,1,'2023-07-11 16:56:21',1001,1005,207812),('163F4251944846ED','60','PLANCHA OSTER A VAPOR CON SUELA ANTIADHERENTE ROJO','GCSTBS5004','a vapor color rojo antiadherente',197,300,360,1,'2023-07-11 17:29:26',1007,1009,571770),('17B5FC1821D94156','34','PLANCHA PARA CABELLO REMINGTON ALISADORA EDICION LIMITADA (OBSEQUIOS) NEGRO','S3500','plancha de cabello',315,499,740,1,'2023-07-08 23:40:19',1015,1020,170372),('184D49A4D8444EAD','6','LICUADORA BLACK&DECKER 10 VELOCIDADES JARRA DE VIDRIO NEGRO','BLBD210GB','10 velocidades negra, de vidrio.',198,450,550,1,'2023-07-08 23:00:17',1008,1027,190196),('19B32FE3B9AD4EED','2','ESTUFA CON HORNO ACROS 20\" NEGRO Y GRIS TOP NEGRO','LAW5300S00','color gris con negro',1615,2050,3050,1,'2023-07-08 22:45:00',1002,1007,170372),('1BEAA6617B1A4408','14','ROPERO ESPAÑOL MUEBLES HELEN','ROPESPANOL','ropero',2725,3650,5580,1,'2023-07-08 23:15:30',1013,1017,813063),('1E6CFE52CDC74CB9','41','CAMA OLYMPIA ANTIESTRES ORTOPEDICA MATRIMONIAL ANTIZANCUDOS','ANTIESTRESORTMATRI','ortopedica matrimonial con tratamiento anti-zancudos',1888.45,2890,3950,1,'2023-07-11 17:02:18',1014,1018,109822),('1F70004FC1C34E42','19','PLANCHA PARA CABELLO REMINGTON PRO-ION STRAIGHT ','S7710','plancha de cabello',279,499,700,1,'2023-07-08 23:23:07',1015,1020,415958),('20D76F4847AB4D54','15','ROPERO MILAN MUEBLES HELEN','ROPMILAN','ROPERO',2425,3450,5280,1,'2023-07-08 23:17:32',1013,1017,813063),('219F92BBC474450C','17','TRINCHANTE ZENIA MUEBLES HELEN','TRINZENIA','trinchante',3075,4150,6000,1,'2023-07-08 23:19:57',1013,1017,813063),('223B3F321B7049E0','74','VENTILADOR DE 12\"  PEDESTAL ROJO ','VEN12ROJO','12 pulgadas color rojo',160,250,250,1,'2023-07-11 17:48:15',1023,1028,864663),('24462CC7CCCB45A2','69','CAMA OLYMPIA EDICIÓN ESPECIAL CHAPINA MATRIMONIAL BOX TOP','EECHMATRI1BTS','edición julio chapina matrimonial',1272,1920,2850,1,'2023-07-11 17:42:13',1014,1018,109822),('259EDE7359C14D6A','96','PLANCHA OSTER A VAPOR CON SUELA ANTIADHERENTE LILA','GCSTBS6005','a vapor antiadherente color lila',260,360,410,1,'2023-07-11 18:14:49',1007,1009,571770),('275D83AEBC19460B','98','LAVADORA MABE DE 44 LBS CON TECNOLOGÍA AQUA SAVER GREEN BLANCA','LMA70213CBAB0','44 libras color blanca',3313,4450,6420,1,'2023-07-11 18:16:55',1004,1008,207812),('282B9B8BA3EB4799','30','PROCESADOR DE ALIMENTOS BLACK&DECKER 8 TAZAS BLANCO','FP1337','procesador 8 tazas',390,590,750,1,'2023-07-08 23:35:42',1020,1027,170372),('2973B2D55CD04745','65','TELEVISOR COMPAQ 32\" SMART ANDROIDTV','QLG32','32 pulgadas con sistema android',1395,2195,3200,1,'2023-07-11 17:37:42',1001,1006,170372),('2DB64881CF144F24','20','SECADORA DE CABELLO REMINGTON THERMACARE','D12A','secadora de cabello',281.8,399,520,1,'2023-07-08 23:23:59',1015,1020,415958),('3389135FF94949D6','58','REFRIGERADORA MABE 8 PIES FROST 1 PUERTA CON DISPENSADOR SILVER','RMU210FANU','8 pies 1 puerta con dispensador color silver',2049,2960,4200,1,'2023-07-11 17:27:42',1003,1008,207812),('3561AE8C34CB4A13','47','OLLA DE PRESIÓN PICCA 5 LITROS MARMOL GRIS','PI00050PG','5 litros de mármol color gris',265,500,600,1,'2023-07-11 17:13:53',1021,1024,170372),('382F4FFD093D4AB7','67','HORNO MICROONDAS OSTER 1,1 PIES CUBICOS MARCO DE ACERO','OGGM61002','1,1 pies marco de acero',699,1100,1440,1,'2023-07-11 17:39:52',1005,1009,207812),('3AD4D64160CE4028','86','CAMA OLYMPIA EDICIÓN ESPECIAL CHAPINA MATRIMONIAL DOBLE BOX TOP','EECHMATRI2BTS','doble box top edición julio chapina',1570,2195,3100,1,'2023-07-11 18:01:06',1014,1018,109822),('3AFBED8FAFEC4D7D','88','BOCINA BLUETOOTH ABS COLORES','MS-2678BT','bocina con bluetooth y luces',153,250,999,1,'2023-07-11 18:03:45',1010,1028,308689),('407CF69A132F4264','28','OLLA MULTIUSO BLACK&DECKER 3 LITROS','MCH14','multifuncion para 3 litros',450,715,870,1,'2023-07-08 23:33:10',1028,1027,190196),('40E6DA39C004482E','99','PROTECTOR DE CAMA OLYMPIA QUEEN','EDREDONQUEEN','funda para cama queen',80,150,999,1,'2023-07-11 18:18:14',1035,1018,109822),('427F765F23944413','59','REFRIGERADORA MABE 10 PIES TOP MOUNT CON DISPENSADOR SILVER','RMA250PJMRU1','10 pies con dispensador',3085,4190,5340,1,'2023-07-11 17:28:37',1003,1008,207812),('4284EB52D1124C6F','11','MINICOMPONENTE LG Xboom CJ45 8500 WATTS CON WOOFER (USB/CD/BT)','LG-CJ45','8500 watts, 2 bocinas mas el woofer',1899,2595,3600,1,'2023-07-08 23:09:07',1012,1002,190196),('4349362C8D814D10','36','COMBO DE ALISADORA, ONDULADORA Y SECADORA REMINGTON ROJO','S5520-D3015MP','alisadora, onduladora y secadora',550,799,1000,1,'2023-07-11 16:52:30',1015,1020,170372),('439D87D29ED24B31','10','ALMOHADA DE FIBRA ESTANDAR ','ALM3','almohada',1,25,25,1,'2023-07-08 23:06:58',1027,1018,109822),('52F44C4F3E9043CD','40','LAVADORA MABE DE 42 LBS CON TECNOLOGÍA AQUA SAVER GREEN BLANCA','LMA79113VBAB0 ','lavadora de 42 libras color blanca',3289,4250,6120,1,'2023-07-11 16:58:51',1004,1008,207812),('53BCD6AB3B5C410B','455621','HORNO MICROONDAS WHIRLPOOL DE 0.7 PIES CUBICOS SILVER','WM1807D','Color gris',612,890,1110,1,'2023-07-08 22:55:10',1005,1012,207812),('5569E58281A14752','43','PROCESADOR DE PULSO PROCTOR SILEX 1.5 TAZAS BLANCO','PS72500PS','1.5 tazas color blanco',145,200,200,1,'2023-07-11 17:05:40',1020,1023,571770),('58057F18F7EB4B2C','79','TELEVISOR HISENSE 32\" SMART HD LED','32A4KV','32 pulgadas hd led',1146,1950,3000,1,'2023-07-11 17:54:04',1001,1004,207812),('581A4C9BEB8742C5','29','LAVADORA WHIRLPOOL DE 48 LBS TAPA DE VIDRIO CON XPERT CYCLE BLANCA','8MWTW2224WJM','48 libras',3525,4790,6840,1,'2023-07-08 23:34:31',1004,1012,207812),('5B381E02A3BE466D','92','COMPUTADORA PORTATIL HP 14DQ0509LA','HP14DQ0509LA','laptop hp',2798,3499,5400,1,'2023-07-11 18:10:26',1033,1026,190196),('5FEF440C5E774E26','62','HORNO TOSTADOR BLACK&DECKER BLANCO','TO134W','horno tostador',355,590,660,1,'2023-07-11 17:33:10',1006,1027,170372),('65C667755CC74BB5','80','TELEVISOR HISENSE 43\" SMART UHD-4K HDR LED','43A7GV','43 pulgadas uhd 4k led',2120,3090,4680,1,'2023-07-11 17:54:47',1001,1004,207812),('67FD2B5F7EE6429A','73','REFRIGERADORA MABE 8 PIES 1 PUERTA CON DISPENSADOR FROST GRIS','RMC181PYMRXO','8 pies 1 puerta con dispensador',1900,2890,4200,1,'2023-07-11 17:46:27',1003,1008,367486),('6BBB0BCC5DB845D3','13','ROPERO BELIAN MUEBLES HELEN','ROPBELIAN','ropero',2850,3745,5760,1,'2023-07-08 23:13:12',1013,1017,813063),('6C0B4D18C6B14596','61','PLANCHA OSTER A VAPOR CON SUELA ANTIADHERENTE GRIS','GCSTBS5001','a vapor color gris antiadherente',197,300,360,1,'2023-07-11 17:30:13',1007,1009,571770),('6C1FEBDEBE36402F','52','PLANCHA SECA LIVIANA OSTER CELESTE Y BLANCO','GCSTBV4112','sin vapor color celeste y blanco',197,295,350,1,'2023-07-11 17:20:22',1007,1009,571770),('6CE44EE20A6A4143','18','CUCHILLA PARA LICUADORA OSTER ORIGINAL','BLSTAA4961','cuchilla para licuadora',44,80,0,1,'2023-07-08 23:21:36',1008,1009,571770),('6D160E13A67947CC','71','TELEVISOR SAMSUNG 55\" SMART LED 4K UHD ','UN55AU7000P','55 pulgadas smart led 4k UHD',4800,5850,7800,1,'2023-07-11 17:44:14',1001,1001,170372),('6EF3630D6BF74808','57','TELEVISOR SAMSUNG 43\" SMART LED 4K ULTRA HD','UN43AU7000P','43 pulgadas ultra hd 4k',3400,4250,5640,1,'2023-07-11 17:26:34',1001,1001,170372),('70A20FA34E0A40B6','31','BATIDORA BLACK&DECKER MANUAL Y DE TAZÓN BLANCA','MX900','tazon de vidrio',365,590,750,1,'2023-07-08 23:36:53',1019,1027,170372),('739A7DBE77D74134','25','LICUADORA BLACK&DECKER 10 VELOCIDADES JARRA DE VIDRIO BLANCO','BLBD210GW','10 velocidades, blanca, jarra de vidrio.',244.3,450,550,1,'2023-07-08 23:29:30',1008,1027,415958),('743ACCACD37E40E1','22','SOPORTE DE PARED MAIESTA PARA TV DE 26\"-63\" FIJO','RACKF26-63','soporte tv',35,120,0,1,'2023-07-08 23:26:15',1016,1021,308689),('79D3C5FEEEF34EE5','77','ESTUFA CON HORNO MABE 30\" NEGRO CON PARILLAS DE HIERRO FUNDIDO','EM7658BFIN1','6 hornillas con parrillas de hierro fundido',2708,3650,4740,1,'2023-07-11 17:52:18',1002,1008,207812),('7E27382FA06242BA','81','TELEVISOR TOSHIBA 55\" SMART UHD-4K HDR','55C350LS','55 pulgadas smart UHD 4K',3116,4110,5580,1,'2023-07-11 17:55:39',1001,1005,207812),('7F0A93011DBD4498','8','LICUADORA OSTER 8 VELOCIDADES VASO DE VIDRIO VERDE','BLSTMG-K15','8 velocidades, verde, vaso vidrio.',364.95,490,590,1,'2023-07-08 23:04:08',1008,1009,170372),('801688DEFFFE4E22','42','PROCESADOR DE PULSO PROCTOR SILEX 1.5 TAZAS NEGRO','PS72507','1.5 tazas color negro',145,200,200,1,'2023-07-11 17:04:48',1020,1023,571770),('82A65252FBF44C7B','85','CONGELADOR HORIZONTAL HISENSE DE 15 PIES CUBICOS BLANCO','FC15D6BWX','horizontal de 15 pies color blanco',3446,4490,6600,1,'2023-07-11 17:59:59',1030,1004,207812),('8C4D3361881E41B0','89','ESTUFA ELECTRICA 1 HORNILLA 1000W','JX-1010B','1 hornilla electrica',93.9,175,999,1,'2023-07-11 18:04:49',1032,1029,308689),('8F06CF32E4D943BA','21','SOPORTE DE PARED MAIESTA PARA TV DE 14\"-42\" FIJO','S-5505CP','colgar tv',24,80,0,1,'2023-07-08 23:25:22',1016,1021,308689),('93D43B7B12744D41','24','CAFETERA BLACK&DECKER 12 TAZAS JARRA DE VIDRIO PANEL DIGITAL NEGRO','CM1105B','12 tazas jarra de vidrio',200.83,440,500,1,'2023-07-08 23:28:05',1017,1027,415958),('98316E28CB1A4993','78','HORNO MICROONDAS OSTER DE 0,7 PIES CUBICOS NEGRO','OGKEW2702','0.7 pies color negro',565,825,1050,1,'2023-07-11 17:53:11',1005,1009,207812),('98966392F6904ECD','72','CAMA OLYMPIA EDICIÓN ESPECIAL CHAPINA IMPERIAL BOX TOP','EECHIMPERIAL1BTS','edición julio chapina imperial box top',1033,1490,2160,1,'2023-07-11 17:45:21',1014,1018,109822),('9897398DB1244D31','84','FRIGOBAR HISENSE 3,3\" 2 PUERTAS GRIS','RT33D6AAE','3,3 2 puertas color gris',1366,1890,2900,1,'2023-07-11 17:58:38',1029,1004,207812),('995B35B719F044E1','49','ESTUFA CON HORNO ACROS 30\" GRIS TOP INOXIDABLE','LAF5333D','6 horinillas con horno inoxidable',2339,3530,4620,1,'2023-07-11 17:17:07',1002,1007,170372),('997450717323425F','16','ROPERO ZADA MUEBLES HELEN','ROPZADA','ropero',2625,3590,5400,1,'2023-07-08 23:18:44',1013,1017,813063),('A2E00980A9914729','54','LAVADORA SAMSUNG BLANCA 42 LBS CON TECONOLOGIA DUAL STORM','WA19A3353GW','capacidad para 42 libras color blanca',3391,4390,6300,1,'2023-07-11 17:22:35',1004,1001,207812),('A5275D06C19C48D4',' 4','ESTUFA CON HORNO MABE 30\" NEGRO Y GRIS TOP NEGRO','EM7622BAPS','color gris con negro',2072,3120,4260,1,'2023-07-08 22:29:36',1002,1001,207812),('A9F972B4EF7E4508','83','TORRE DE SONIDO SONY DE 450W CON DVD/CD/FM/USB/BLUETOOTH NCF E ILUMINACIÓN','MHCV43D','450w con ncf iluminación y woofer max',3210,4290,5700,1,'2023-07-11 17:57:30',1011,1016,207812),('AAC17EAA12664518','63','HORNO TOSTADOR BLACK&DECKER NEGRO','TO134B','horno tostador',355,590,660,1,'2023-07-11 17:33:53',1006,1027,170372),('AB68731198214EDA','44','ESTUFA CON HORNO ACROS 30\" NEGRO TOP INOXIDABLE','LAF5333B00','6 hornillas parrillas de alambron',2715,3530,4620,1,'2023-07-11 17:07:39',1002,1007,170372),('ADD6F54D055D43EA','91','COLCHON COMFORTEX PLUS IMPERIAL','COLCHCOMFORTEX','plus imperial',799,1099,1099,1,'2023-07-11 18:08:56',1014,1019,190196),('AF3E8B3C75E54F86','95','PLANCHA OSTER A VAPOR CON SUELA ANTIADHERENTE CELESTE','GCSTBS6004','a vapor suela antiadherente celeste',250,360,410,1,'2023-07-11 18:13:29',1007,1009,571770),('B03725D0D57548AE','97','PLANCHA OSTER A VAPOR CON SUELA ANTIADHERENTE MENTA','GCSTBS5002','a vapor antiaherente color menta',197,300,360,1,'2023-07-11 18:15:47',1007,1009,571770),('B0BEC05418474437','75','VENTILADOR DE 10\" PEDESTAL AMARILLO','VEN10AMARILLO','de pedestal color amarillo',150,230,230,1,'2023-07-11 17:50:26',1023,1028,864663),('B85255FDFE60431E','87','VASO EXPRIMIDOR DE JUGOS 380ml','HM-03','vaso licuadora portatil 380 ml',62.18,125,999,1,'2023-07-11 18:02:51',1031,1028,308689),('BA384E4E76F04409','55','TELEVISOR SAMSUNG 32\" SMART HD','UN32T4300','32 pulgadas smart hd',1800,2600,3550,1,'2023-07-11 17:24:23',1001,1001,170372),('BBB8B203245B4741','37','COMBO DE SECADORA Y ALISADORA DE CABELLO REMINGTON ROSE GOLD','D3015-S1520','secadora, alisadora.',450,699,900,1,'2023-07-11 16:53:42',1015,1020,170372),('BC5E2241D5AA432F','45','CAMA OLYMPIA EDICIÓN ESPECIAL ONE PHILLOW IMPERIAL','EEONEPHILLIMP','one pillow imperial (economica)',868,1290,1880,1,'2023-07-11 17:10:02',1014,1018,109822),('BF2A96989E714B58','68','HORNO MICROONDAS FRIGIDAIRE DE 0,7 PIES CUBICOS SILVER','FMDO20S3GSPG','0,7 pies color gris',590,890,1110,1,'2023-07-11 17:40:50',1005,1013,207812),('C2E127BD1ED34FA4','3','REFRIGERADOR MABE 9 PIES TOP MOUNT GRIS MATE ','RMA230PVMRG1','Color gris mate',2708,3690,4920,1,'2023-07-08 22:47:00',1003,1008,207812),('C33095A2D20343F4','33','LICUADORA OSTER TRADICIONAL 2 VELOCIDADES VASO PLASTICO','4170','vaso de plastico',425,655,840,1,'2023-07-08 23:38:58',1008,1009,170372),('C818D1242A9247C6','94','ESTUFA DE MESA IML 4 HORNILLAS GRIS TOP INOXIDABLE','C-4G','4 hornillas inoxidable color gris',422,650,930,1,'2023-07-11 18:12:16',1034,1010,571770),('C9222F249609435C','70','CAMA OLYMPIA EDICIÓN ESPECIAL CHAPINA KING BOX TOP','EECHKING1BTS','edición julio chapina King box top',1987,2840,3950,1,'2023-07-11 17:43:14',1014,1018,109822),('CBF0BD46B0F243E2','100','BICICLETA SHIMANO RELAMPAGO NO. 26 NEGRO Y ROJO','RELAMPAGO26','no 26 color combinado rojo y negro',1000,1600,2500,1,'2023-07-11 18:19:50',1036,1030,367486),('CE970787F7054FD5','66','LAVADORA WHIRLPOOL DE 44 LBS CON XPERT SYSTEM BLANCA','8MWTW2024MJM','capacidad 44 libras color blanca con panel gris',3352,4520,6480,1,'2023-07-11 17:38:44',1004,1012,207812),('CFF1278785E84735','46','CAMA OLYMPIA EDICIÓN ESPECIAL ONE PHILLOW MATRIMONIAL','EEONEPHILLMATRI','one phillow matrimonial (economica)',1160,1750,2700,1,'2023-07-11 17:11:06',1014,1018,109822),('D3CE6985E1FE45DC','35','TELEVISOR HISENSE 43\" SMART UHD-4K HDR LED','43A7GV','43 pulgadas ultra hd con 4k',2120,3090,4680,1,'2023-07-08 23:42:10',1001,1004,207812),('D7AB03B5B528446B','5','CAFETERA BLACK&DECKER 10 TAZAS JARRA DE VIDRIO NEGRO','DCM1100B','para 10 tazas, jarra de vidrio.',150,320,390,1,'2023-07-08 22:58:48',1017,1027,190196),('DA5308C4F6A84FAB','39','REFRIGERADOR WHIRLPOOL 9 PIES TOP MOUNT CON DISPENSADOR GRIS','WRW25CKTWW','refrigeradora de 9 pies con dispensador ',3297,4290,5400,1,'2023-07-11 16:57:29',1003,1012,207812),('DAB0B3FC4E1048C5','76','REFRIGERADORA MABE 11 PIES TOP MOUNT CON DISPENSADOR SILVER','RMA300FXNU','11 pies con dispensador color Silver',3446,4450,5700,1,'2023-07-11 17:51:19',1003,1008,207812),('E0AAC39434F946FE','32','LICUADORA OSTER CROMADA 2 VELOCIDADES VASO DE VIDRIO','46515','vaso de vidrio',695,990,1200,1,'2023-07-08 23:38:01',1008,1009,170372),('E6DF9B2938E14FE7','64','PLANCHA A VAPOR BLACK&DECKER TRUEGLIDE NEGRA','IRBD300','a vapor color negra',140,275,350,1,'2023-07-11 17:36:36',1007,1027,170372),('EA7053AC92284D55','56','TELEVISOR SAMSUNG 43\" SMART LED  HD','UN43AU5300','43 pulgadas led hd',2875,3950,5400,1,'2023-07-11 17:25:13',1001,1001,170372),('F76831DD09144B0B','23','SOPORTE DE PARED MAIESTA PARA TV DE 40\"-80\" FIJO','RACKF40-80','40-80 fijo',65,145,0,1,'2023-07-08 23:26:59',1016,1021,308689),('F9D4185A13204250','90','ALMOHADA DE FIBRA OLYMPIA EXIBHICIÓN','ALMOHADAOLYMPIA',' EXIBHICIÓN EXIBHICIÓN EXIBHICIÓN EXIBHICIÓN',1,999,999,1,'2023-07-11 18:07:33',1027,1018,109822),('FF909EAE806B49F2','82','TELEVISOR HISENSE 70\" SMART UHD-4K HDR ANDROID TV','70H6500G','70 pulgadas smart uhd 4k con android tv',5016,6190,8400,1,'2023-07-11 17:56:28',1001,1004,207812);
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
INSERT INTO `pv_providers` VALUES (109822,1,'2023-07-08 19:51:22','116da2fb-2ac9-483a-8c6b-2f46b4b4b6e2'),(160039,1,'2023-07-08 19:48:13','b03edfb9-84ae-482c-a600-432cfdad6aa9'),(170372,1,'2023-07-08 19:52:27','dab4a868-dd48-4363-bcaa-14619938406e'),(190196,1,'2023-07-08 19:47:32','64116745-badb-4eda-9a55-246cb34d380b'),(207812,1,'2023-07-08 18:48:00','0f3ab69b-b9ef-45b8-b6d5-2c3b983b2f41'),(308689,1,'2023-07-08 19:52:00','e63803eb-bba1-4191-917a-8320849fbd20'),(367486,1,'2023-07-08 19:50:08','0634147a-a9ee-48d2-a3a5-7c972c6ce94c'),(415958,1,'2023-07-08 19:51:42','04c85492-590c-4861-a392-cc17cb76be9c'),(525311,1,'2023-07-08 19:48:47','00168a7f-444c-4d59-8a9f-bcb3bbc62da8'),(564338,1,'2023-07-08 19:52:50','11984714-7fdd-402c-9e96-ae8e14a563af'),(571770,1,'2023-07-08 19:44:48','36e90fb9-583d-474f-ad85-08f4eacf05ad'),(575180,1,'2023-07-08 19:46:23','837f62ed-560d-464c-ba2a-06ddf76e1c03'),(813063,1,'2023-07-08 19:50:54','54786e44-eb51-4b14-ad95-d54539cd0a0f'),(864663,1,'2023-07-11 17:48:45','34c2315d-b0b3-4be1-862f-1db6168d5880');
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
INSERT INTO `sa_sales` VALUES ('bf3505a7-6f7b-4647-9c79-852498b55d6e',3090,0,3,31,1,'2023-07-09 01:08:48',1002,1002,217295,263899);
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
) ENGINE=InnoDB AUTO_INCREMENT=1002 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sd_saledetails`
--

LOCK TABLES `sd_saledetails` WRITE;
/*!40000 ALTER TABLE `sd_saledetails` DISABLE KEYS */;
INSERT INTO `sd_saledetails` VALUES (1001,3090,2120,1,'D3CE6985E1FE45DC','bf3505a7-6f7b-4647-9c79-852498b55d6e');
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
INSERT INTO `sess_usersessions` VALUES ('182deaf4-e4a3-4485-aed0-749d073e5f92',0,1,'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36','2023-07-11 18:22:22',263899),('354836aa-8456-472b-ba84-69f667cb10c7',0,1,'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36','2023-07-11 17:42:35',206506),('d828cfd7-e382-47dd-aa00-9c1144a5b83a',1,1,'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36','2023-07-15 22:34:33',263899),('dae26fe5-ec47-4595-818e-e3126b158885',0,1,'Mozilla/5.0 (iPhone; CPU iPhone OS 16_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5.1 Mobile/15E148 Safari/604.1','2023-07-12 15:19:06',263899),('e5f1853a-8da3-4bbb-af85-9155fd0ae567',0,1,'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36','2023-07-10 18:00:08',206506),('f52bfe3d-3af2-4854-95ca-3c022373c070',0,1,'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36','2023-07-14 19:38:55',206506);
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
) ENGINE=InnoDB AUTO_INCREMENT=1005 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sp_salepayments`
--

LOCK TABLES `sp_salepayments` WRITE;
/*!40000 ALTER TABLE `sp_salepayments` DISABLE KEYS */;
INSERT INTO `sp_salepayments` VALUES (1001,1000001,1030,0,1030,'2023-07-09','2023-07-09 01:08:48',1001,263899,'bf3505a7-6f7b-4647-9c79-852498b55d6e'),(1002,NULL,686,0,0,'2023-08-09',NULL,NULL,NULL,'bf3505a7-6f7b-4647-9c79-852498b55d6e'),(1003,NULL,686,0,0,'2023-09-09',NULL,NULL,NULL,'bf3505a7-6f7b-4647-9c79-852498b55d6e'),(1004,NULL,688,0,0,'2023-10-10',NULL,NULL,NULL,'bf3505a7-6f7b-4647-9c79-852498b55d6e');
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
) ENGINE=InnoDB AUTO_INCREMENT=1003 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `st_states`
--

LOCK TABLES `st_states` WRITE;
/*!40000 ALTER TABLE `st_states` DISABLE KEYS */;
INSERT INTO `st_states` VALUES (1001,'Guatemala',1),(1002,'',0);
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
) ENGINE=InnoDB AUTO_INCREMENT=1004 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ts_typessales`
--

LOCK TABLES `ts_typessales` WRITE;
/*!40000 ALTER TABLE `ts_typessales` DISABLE KEYS */;
INSERT INTO `ts_typessales` VALUES (1001,'De contado'),(1002,'Abonos'),(1003,'Fuera de tienda');
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
INSERT INTO `us_users` VALUES (181549,'$2b$12$OpB5dQXT2dBErSIPlg3AJuUzvdrFSqtdMUws426Pb/h6I17vs9qLy','[\'/pos/statistics\', \'/pos/manage/customers\', \'/pos/manage/products\', \'/pos/manage/providers\', \'/pos/manage/categories\', \'/pos/manage/brands\', \'/pos/manage/sales\', \'/pos/manage/addresses\', \'/pos/manage/sale/payments\', \'/pos/manage/sale/payments/edit\']',1,'2023-06-25 23:59:54','f98ff4d9-a90c-44a2-9a11-2c3b492dc510',111529),(206506,'$2b$12$c5QpRpxLh/OYZNM9M5KCQecnCpsKqs45WK1QHJscUN6MFpF45dsnC','[\'/pos/statistics\', \'/pos/manage/users\', \'/pos/manage/customers\', \'/pos/manage/paymentmethods\', \'/pos/manage/locations\', \'/pos/manage/products\', \'/pos/manage/providers\', \'/pos/manage/categories\', \'/pos/manage/brands\', \'/pos/manage/cities\', \'/pos/manage/states\', \'/pos/manage/sales\', \'/pos/manage/dbbackup\', \'/pos/manage/addresses\', \'/pos/manage/sale/payments\', \'/pos/manage/sale/payments/edit\']',1,'2023-06-21 13:15:07','86302e2b-809c-490c-819a-367f88f4af67',111529),(263899,'$2b$12$PluQojW52KsQOmZe/.F8f.f7sbJcbM9AYlOyqA1hlLptSoGqA9LaO','[\'/pos/statistics\', \'/pos/manage/users\', \'/pos/manage/customers\', \'/pos/manage/paymentmethods\', \'/pos/manage/locations\', \'/pos/manage/products\', \'/pos/manage/providers\', \'/pos/manage/categories\', \'/pos/manage/brands\', \'/pos/manage/cities\', \'/pos/manage/states\', \'/pos/manage/sales\', \'/pos/manage/dbbackup\', \'/pos/manage/addresses\', \'/pos/manage/sale/payments\', \'/pos/manage/sale/payments/edit\']',1,'2023-06-23 11:32:06','ea01b71f-51df-4e9a-a402-018e399e611b',111529),(791950,'$2b$12$KIzwtHxeY.h97KqM1xcmVeKiDa5ZOe.dCDQ89zG9FVymEJnJfSKVa','[\'/pos/manage/customers\', \'/pos/manage/sales\', \'/pos/manage/addresses\', \'/pos/manage/sale/payments\']',1,'2023-06-25 23:58:58','c70dd5a9-f7a8-4964-a0c5-f6310bc1dddd',111529);
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

-- Dump completed on 2023-07-15 22:34:38
