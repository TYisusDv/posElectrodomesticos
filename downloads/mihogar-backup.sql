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
INSERT INTO `ad_addresses` VALUES ('02012bd7-a2fa-4992-8b87-92c1cc1dd5d2','2388 75237 0301','Luis Alfredo Fernández','6 calle 3-03 zona 1','','3012-0301','Ideas creativas ciudad vieja',1,'2023-07-19 17:13:23',1001,1003,'969a16b4-2bda-4a8a-b18c-d9b25c25af34'),('0538d9aa-7c5f-4e99-91bd-43dd69484391','1598 32098 0501','Leonel Francisco Florez Hernandez','Calle principal casa 47 aldea guadalupe el zapote','','sin telefono','Panificador, finca el zapote',1,'2023-07-25 14:42:01',1001,1006,'110f5b95-d887-4217-94aa-011ae3a74406'),('075a382f-b43b-47d5-b99f-40f619b04647','3062 46422 0311','Miriam Fabiola Ciriaco Sunún','Callejon pechugas 4 l. 6 aldea san lorenzo el cubo','','4260-9403','',1,'2023-07-18 18:56:53',1001,1003,'ebfce75c-674f-4773-805a-f219f9f9ca98'),('08d5c670-19ee-4ad1-84a1-ad2a2f068d98',' ','Silvia Jiménez','','','4748-0153','',1,'2023-07-19 17:20:34',1002,1002,'a240c6f0-b3c4-4d32-9ae8-52f0441e9560'),('090e73f5-2202-437e-89ff-6543bf667681',' ','Blanca Salama','Ciudad vieja','Vecina','5053-6813','',1,'2023-07-18 16:52:22',1002,1003,'72255d26-f2c7-40db-a314-2a77dd37f8c2'),('0a9eeebe-68c0-4996-a12c-a18d3ff3c0d2','2846 24977 0301','Israel Alejandro Pol Lopez','Calle principal san lorenzo el cubo ciudad vieja sac','','3273-4861','Comerciante, taller electrico alfa y omega',1,'2023-07-25 15:16:17',1001,1003,'0e2f5cff-9708-4b7b-9ea3-aff816377176'),('0b7a456f-dac5-401f-bd32-1230e18ee461','2709 46063 0313','Handersson Geovany Perez Arenales','San lorenzo el cubo','','4268-5314','',1,'2023-07-18 18:55:34',1001,1003,'a5cdb768-5b85-4db0-837b-a4fbd8c145ad'),('0ea7c9cd-d387-4dc2-96af-f2c0eb0514d1',' ','Daniel Lopez','','','5056-4215','',1,'2023-07-25 15:16:48',1002,1002,'0e2f5cff-9708-4b7b-9ea3-aff816377176'),('0fc68427-18fe-4442-b118-dc4c28fb4ce0',' ','Victor Taj','','','3486-2568','',1,'2023-07-19 20:22:13',1002,1002,'091a809e-edd6-4213-ae79-7ef4505ff530'),('12514d76-dcea-4ddf-9f81-3da9fbd60654',' ','Brenda Pérez Hernández','','','3383-9641','',1,'2023-07-19 20:27:52',1002,1002,'9729f6f7-27a5-4a3f-896f-e872e0e1c63b'),('15825a9d-1acd-4262-b9b5-de1d044f1d96','3062 78790 0312','Josue Nehemias Godinez Gomez','Camino a san antonio no.15 aldea san lorenzo el cubo','','4474-3314','Pollo campero',1,'2023-07-25 17:36:04',1001,1003,'68d2815d-1075-406d-bac6-cd4faea8dd0b'),('17b89250-f183-4b53-ab84-7b7a54ec044d',' ','Elvia Vega','','','4389-9538','',1,'2023-07-19 20:38:55',1002,1002,'e47e1ec9-f331-4ce4-ac20-3b8e14d9945f'),('17d280f4-90af-481d-94f5-35519fb3dec7',' ','Bernardo Lopez','','','5555-9024','',1,'2023-07-25 16:27:30',1002,1002,'58f37bcf-3f14-4b0b-b264-3f3b9e0fa91a'),('17f9b0c7-00be-4fe5-8fd2-416d920c3a09',' ','Francisca Ordoñez','','','3086-9338','',1,'2023-07-19 17:17:37',1002,1002,'68a42481-5c71-4550-bfbe-cd299488c9bb'),('1b795018-350f-485f-ab59-9437a7b44c5f',' ','Paola Herrera Caná','','','5635-9549','',1,'2023-07-19 20:26:20',1002,1002,'89f6d914-2124-429e-ae10-bd92a4e27a76'),('1c42af52-4a5b-41c5-a141-1065d345987d',' ','Irma Caná','','','5074-7006','',1,'2023-07-19 20:51:00',1002,1002,'1d298f36-ba20-44f3-b9ec-fefcb05e02e4'),('1c7423b6-2868-4766-980f-af613838d70b',' ','Merbelyn Yadira Galindo','','','3700-8635','',1,'2023-07-25 17:19:46',1002,1002,'b2521ae2-6862-4d7c-9214-8dfb2ba60e7c'),('1f69f225-04c5-4402-b0b8-643232643da4',' ','Diviam','','','5497-4803','',1,'2023-07-19 20:22:00',1002,1002,'091a809e-edd6-4213-ae79-7ef4505ff530'),('212c88bd-cee2-4567-8671-a50babedfff6','2183 74976 0312','Martin Celada Voz','Segundo callejon atras de la iglesia catolica  5 av 3-46 san lorenzo el cubo','','4197-4168','Albañil, antigua gardens',1,'2023-07-24 14:49:20',1001,1003,'735c6789-5199-46aa-a0b9-94a5bbabc2d8'),('2157c76a-ccfb-4058-87dd-94f5de63bd44',' ','Lady Castellanos','','','5568-0501','',1,'2023-07-25 14:11:15',1002,1002,'81c2f770-6e69-46f3-819c-f56c3e33a0dd'),('219ba18c-4858-4ad4-bfd3-96d2d207a801',' ','Edgar Daniel López Ramírez','','','4535-8636','',1,'2023-07-19 17:24:43',1002,1002,'b3d64882-65da-492e-94cd-7d721cf8b069'),('226b7084-e48e-472f-ba4a-f3051985c432',' ','Arib Lopez','','','5421-0107','',1,'2023-07-25 15:16:32',1002,1002,'0e2f5cff-9708-4b7b-9ea3-aff816377176'),('2380a69c-56de-4a98-a3dc-03e56e5dcfa4','2459 92596 0301','Luis Jeremías Pérez Jiménez','3 calle zona 3 ciudad vieja','','5003-6320','Comerciante',1,'2023-07-19 17:18:51',1001,1003,'75674e31-bdc3-47ab-aa5a-5879313c2fac'),('2432e309-2585-4472-a3b5-26036bcc4b12',' ','Lourdes Camargo','Ciudad vieja','Hermana','3898-7069','',1,'2023-07-18 16:53:36',1001,1003,'72255d26-f2c7-40db-a314-2a77dd37f8c2'),('24500c14-2caa-400e-9aac-e364f17242b1','2638 05786 0312','Edgar Eduardo Caná Perez','Calle del cause no. 3 san lorenzo el cubo','','5191-5388','Jornalero',1,'2023-07-19 20:25:32',1001,1003,'89f6d914-2124-429e-ae10-bd92a4e27a76'),('24c87a05-8b2a-47df-8947-eb90d333e1db','2229 92344 1710','Edras Calet Velez Monrroy','Escuela de la comunidad, san lorenzo el cubo','','4285-0985','Ayudante de ferretería, ferreteria bethesda',1,'2023-07-25 14:52:56',1001,1003,'5bbbf059-4879-41a9-bd39-4b441ba5ea95'),('261e0e57-09a4-44fd-a992-3964d36d9cd4',' ','Pedro Pú','','','sin numero','',1,'2023-07-19 17:22:24',1002,1002,'748e9fdc-7514-4b02-b49a-6c500136c8ea'),('26d46875-53f7-49e8-83f6-2b9fda4f7077',' ','Rafael Hernández','','','3780-9338','',1,'2023-07-19 17:17:15',1002,1002,'68a42481-5c71-4550-bfbe-cd299488c9bb'),('2afd6d28-7c68-4b13-a1eb-6f6759861e2b',' ','Mayra Perez','','','3134-2668','',1,'2023-07-25 16:27:17',1002,1002,'58f37bcf-3f14-4b0b-b264-3f3b9e0fa91a'),('2bc68f67-47ae-4150-a64e-01a478a4767b',' ','Marleni Vega','','','4137-8819','',1,'2023-07-19 20:38:41',1002,1002,'e47e1ec9-f331-4ce4-ac20-3b8e14d9945f'),('2d24b64a-73ed-41e2-a7bd-ed0a7981699c',' ','Elizabeth Caná','','','4894-7937','',1,'2023-07-19 20:51:21',1002,1002,'1d298f36-ba20-44f3-b9ec-fefcb05e02e4'),('30956faf-130c-48fe-8d5e-0ec743bc0c36',' ','Marta Gómez','','','5434-5697','',1,'2023-07-19 20:42:42',1002,1002,'608a7794-1deb-4e6b-876a-9e1d123ad6e4'),('30aee3b4-2e41-4a48-8030-7c7350cc563a','1787 30467 0313','Carlos Humberto Otoy Quexel','2 av. 6-38 a san lorenzo el cubo','','4943-1902','Operador, finca medina, ruta 14',1,'2023-07-19 20:46:55',1001,1003,'bafe5bef-9684-4249-9a06-23462c9a1afc'),('30b7b3a1-9671-4e0b-8b18-7764d04a4615','1981 81329 0312','Wilfredo González Rodríguez','C. principal no. 17 san lorenzo el cubo','','5535-5150','Comerciante, aserradero san miguel',1,'2023-07-25 17:19:10',1001,1003,'b2521ae2-6862-4d7c-9214-8dfb2ba60e7c'),('3107ef77-821e-45d6-aa2e-1177666b9e3e',' ','Gloria Godinez','','','4349-9748','',1,'2023-07-25 17:36:33',1002,1002,'68d2815d-1075-406d-bac6-cd4faea8dd0b'),('32c94248-c395-47c7-8472-fdce8b7c09b8','CF','Patricia Vasquez','San lorenzo el cubo','','3199-6119','',1,'2023-07-22 01:05:00',1001,1003,'c1b07586-b53a-45e3-9142-031062ac7875'),('366ccd1c-cf9a-47fb-bf6b-5e5b56bdd80a',' ','Esmeralda Flores','','','4054-6325','',1,'2023-07-25 15:08:01',1002,1002,'17bb4930-3ccb-498f-b07c-1d6b6ee3084d'),('36d00da7-2ce1-4a76-a38e-1b8f692bcd47',' ','Jenifer Tereso Gómez López','','','5861-4806','',1,'2023-07-19 20:42:14',1002,1002,'608a7794-1deb-4e6b-876a-9e1d123ad6e4'),('38580834-df7c-45c9-9c04-ab914cb45378',' ','Magda Caná','','','4772-4912','',1,'2023-07-19 20:47:32',1002,1002,'bafe5bef-9684-4249-9a06-23462c9a1afc'),('39aec905-4924-49d4-b570-4c873a2ef0c7','CF','Yesica Doriselda Hernandez Cruz','San lorenzo el cubo','',' ','',1,'2023-07-21 00:32:51',1001,1003,'3b6aa0c3-13d9-4c6a-9410-ea1e2e9c816a'),('3a37bac6-a473-42f1-a5b5-7a839a4cdf65','000','Prueba','Street view 1','Persona','1222','Street 1',1,'2023-07-16 06:08:34',1001,1001,'10b9d983-db1e-4606-b069-368682b5afa1'),('3ae478aa-4043-4f71-a461-47259239d2a5',' ','Norvi Velez','','','4676-2504','',1,'2023-07-25 14:53:36',1002,1002,'5bbbf059-4879-41a9-bd39-4b441ba5ea95'),('3c2fe2f8-0330-4fca-ade1-5f8efcdff230',' ','Javier Figueroa','','','3626-3754','',1,'2023-07-25 16:57:55',1002,1002,'7d900c5a-dfe7-48b8-8f74-db2c71457de9'),('3c3c55c3-ba21-4c35-aabb-486ab9fe5976',' ','Filomena Gonzalez','','','4064-7868','',1,'2023-07-25 17:19:56',1002,1002,'b2521ae2-6862-4d7c-9214-8dfb2ba60e7c'),('3c978ab3-dde0-41df-927d-33132769fda1',' ','Jose Alfredo Chutá','','','4569-7184','',1,'2023-07-25 15:03:20',1002,1002,'083d7c0e-0a16-44df-b813-d15098089d29'),('3d33108a-9f69-4aaf-9c79-508086982ea8','1584 28307 0312','Timoteo Paredes Hernandez','Calle de medina casa 1 aldea san lorenzo el cubo','','5592-9550','Albañil',1,'2023-07-25 14:58:05',1001,1003,'4ba80cdd-2902-4ec3-b72d-ac07b014f09d'),('3fd883b1-881d-4a18-adb6-96f3bf31ca9f',' ','Selvin Ramirez','','','5691-8382','',1,'2023-07-19 20:49:27',1002,1002,'148e27a0-b5b5-442c-b87d-4968ec353333'),('41c93ac6-1353-4bf5-8fb1-8de406c00f01',' ','Eliza Cordova','','','5357-3954','',1,'2023-07-25 14:42:22',1002,1002,'110f5b95-d887-4217-94aa-011ae3a74406'),('45369b17-ff5e-4d4a-b1c7-50767d0028fe','1935 81507 0312','Esvin Lorenzo Flores Lopez','Calle real san lorezo el cubo, callejon ferca','','5385-5523','Carpintero',1,'2023-07-25 15:07:50',1001,1003,'17bb4930-3ccb-498f-b07c-1d6b6ee3084d'),('45f5a49b-0aff-4ebf-9f0b-4dc5c5e35e95',' ','Forjas Noemí Solís López','','','5430-3841','',1,'2023-07-19 20:44:29',1002,1002,'f468c827-8a81-48ab-8031-b08562b986ba'),('47546c66-be73-46f8-a5f7-c4669fc0b694',' ','Vivian Perez Jimenez','','','4494-4248','',1,'2023-07-25 16:27:06',1002,1002,'58f37bcf-3f14-4b0b-b264-3f3b9e0fa91a'),('47e4b0d4-0df3-41bd-9f76-44eeb85a079d',' ','Elizabeth Gómez','','','5537-3719','',1,'2023-07-19 20:24:29',1002,1002,'84993d6e-cf70-488b-a92e-51154be22c36'),('47fb4ded-1045-45a6-9519-cfd7cfac977e',' ','Henry Flores','','','4845-3354','',1,'2023-07-19 20:24:55',1002,1002,'84993d6e-cf70-488b-a92e-51154be22c36'),('49d92cb3-9baa-4af6-b9d3-42a2e415c6ab',' ','Giovanny Gómez','','','3860-4488','',1,'2023-07-19 20:39:06',1002,1002,'e47e1ec9-f331-4ce4-ac20-3b8e14d9945f'),('4adec762-b9d9-43ea-ae9f-c5669cb86d71',' ','Ana Gabriela Pérez Hernández','','','4282-8242','',1,'2023-07-19 20:27:42',1002,1002,'9729f6f7-27a5-4a3f-896f-e872e0e1c63b'),('4e2e6cb9-c19e-40ef-a9e4-4bc95a7532e0',' ','Jhonatan Perez','','','5929-8781','',1,'2023-07-25 17:36:42',1002,1002,'68d2815d-1075-406d-bac6-cd4faea8dd0b'),('4f21c4c9-5932-4962-bdb8-7d5c09af7d87','2205 50867 1224','Geiny Osberto Gómez Ortiz','Calle principal segunda esquina, san lorenzo el cubo','','5203-6320','Taqueria san lorenzo',1,'2023-07-19 17:20:03',1001,1003,'a240c6f0-b3c4-4d32-9ae8-52f0441e9560'),('4f864cf9-51a9-4d9e-aaba-35b1ec5718e5','1675 87544 0920','Marvin Rocael Ramírez Pérez','Callejon los pechugas casa numero 15 san lorenzo el cubo','','4817-6459','Albañil',1,'2023-07-19 20:48:46',1001,1003,'148e27a0-b5b5-442c-b87d-4968ec353333'),('54c25d83-d22c-4909-b5e2-1b2ad62d047a','3656046-4','Mario Andrade','Km 38.5 carretera interamericana','','5902-1958','',1,'2023-07-08 19:49:31',1001,1002,'00168a7f-444c-4d59-8a9f-bcb3bbc62da8'),('55c8068d-9255-4299-b027-306b9e892d31',' ','Rutilia Ortíz','','','4812-1249','',1,'2023-07-19 17:20:45',1002,1002,'a240c6f0-b3c4-4d32-9ae8-52f0441e9560'),('570c9f56-3c58-4e44-bd99-10e01157c0c5',' ','Ingrid Gomez','','','3581-3394','',1,'2023-07-25 17:36:18',1002,1002,'68d2815d-1075-406d-bac6-cd4faea8dd0b'),('5b6118cc-b5f8-44d3-bf29-fb5d66ea13f5','3162 11559 0504','Milvia Vivas Lopez','Calle principal lote 40 aldea guadalupe el zapote','','4088-4313','',1,'2023-07-22 00:25:39',1001,1006,'81afa2a8-9b92-4cf6-b1a4-8c9dc27b6257'),('5bd3456b-3781-4818-a59c-d1a42e3ed257','2257 36241 0312','Nelson Estuardo Bosarreyes López','2 calle 1-90, zona 1, san lorenzo el cubo','','5996-5372','Electricista, cooperativa agricola integral unión de 4 pinos',1,'2023-07-19 20:26:56',1001,1003,'9729f6f7-27a5-4a3f-896f-e872e0e1c63b'),('5c5c9b22-d2c9-4c69-8757-d17d7718cbe9','2251 92160 0312','Ana Patricia Gómez Rodríguez','Calle de medina no. 34 san lorenzo el cubo','','5592-3093','Cocinera, jardines pérez, san andres ceballos',1,'2023-07-19 20:23:47',1001,1003,'84993d6e-cf70-488b-a92e-51154be22c36'),('5d99db2d-5888-4b85-bb38-3f69069fe0a0',' ','Doriselda Rodriguez','','','5369-7003','',1,'2023-07-25 14:42:44',1002,1002,'110f5b95-d887-4217-94aa-011ae3a74406'),('5da3de01-d02e-4acc-a525-85bb6bb722e0',' ','Maynor Flores','','','3954-9746','',1,'2023-07-25 15:08:14',1002,1002,'17bb4930-3ccb-498f-b07c-1d6b6ee3084d'),('5dff6d79-477e-403e-b172-8a3294208e48',' ','Yakelin Reyes','','','5367-6805','',1,'2023-07-19 17:12:06',1002,1002,'221ddeea-f9b6-44be-ae34-403148b9d605'),('5e0346fa-4a0e-466c-ab54-3b83f98db267',' ','Dora Caná  Pérez','','','3621-7465','',1,'2023-07-19 20:26:07',1002,1002,'89f6d914-2124-429e-ae10-bd92a4e27a76'),('5f51fc81-2e28-4e4e-8b54-2aa0071248f1',' ','José Veliz','','','3040-3898','',1,'2023-07-19 17:14:27',1002,1002,'969a16b4-2bda-4a8a-b18c-d9b25c25af34'),('614bf782-26b4-4230-9ebe-ebe43dedd53e','3057 28180 0301','Juan Fernando Lopez Ramirez','8 calle 1-50 a zona 2, ciudad vieja','','5123-6325','Electricista',1,'2023-07-19 17:24:04',1001,1003,'b3d64882-65da-492e-94cd-7d721cf8b069'),('6320cbd2-5664-4cab-960f-eae06eda174f',' ','Edgar Caguay','','','5201-5640','',1,'2023-07-19 17:12:24',1002,1002,'221ddeea-f9b6-44be-ae34-403148b9d605'),('653795b1-6113-4606-8015-cccb2a209247',' ','Melvin Caná','','','5440-2223','',1,'2023-07-19 20:51:09',1002,1002,'1d298f36-ba20-44f3-b9ec-fefcb05e02e4'),('6dc2912e-ed08-4376-b04d-c2eeac7d4bd2',' ','Hector Velez','','','3586-6259','',1,'2023-07-25 14:53:14',1002,1002,'5bbbf059-4879-41a9-bd39-4b441ba5ea95'),('6ec32d0b-ca79-48fc-9fc0-4b87b03eacb8','2359 47725 0312','Ervin Geovani Gómez López','Calle del cause no. 35, aldea san lorenzo el cubo','','3860-4488','Municipalidad de ciudad vieja',1,'2023-07-19 20:41:55',1001,1003,'608a7794-1deb-4e6b-876a-9e1d123ad6e4'),('6ec989ad-473d-4e93-b317-8bf29b95153c','1950 15274 0312','María Magdalena Caná Cucuy','Calle de la pila seca casa 40 san lorenzo el cubo','','sin numero','Ama de casa',1,'2023-07-19 20:50:43',1001,1003,'1d298f36-ba20-44f3-b9ec-fefcb05e02e4'),('6fc725e7-3c12-4e70-be45-a948d638e1a3','1796 67157 0312','Lilian Esperanza Lopez Perez De Gomez','San lorenzo el cubo','','5203-6320','',1,'2023-07-25 15:41:24',1001,1003,'63ced801-99a8-48fb-b2ed-f613d2581bda'),('71229893-3a35-4dd5-80f0-3b63747d81aa',' ','Silvia Nohemi Ciriaco','','','5787-9822','',1,'2023-07-19 20:35:17',1002,1002,'ebfce75c-674f-4773-805a-f219f9f9ca98'),('72a1f444-ab45-43bf-a787-5adb97ef7a44','1842 07789 0301','Estuardo Alejandro Perez Jimenez','Caserio bosarreyes no. 17-b san lorenzo el cubo','','4503-0259','Técnico de aprovisamiento, innova',1,'2023-07-25 16:25:51',1001,1003,'58f37bcf-3f14-4b0b-b264-3f3b9e0fa91a'),('7b64c3c1-45f5-4c90-b9c0-434a2cdad1fc',' ','Dora Elizabeth Con García','','','5964-2796','',1,'2023-07-25 14:31:51',1002,1002,'8953ab35-3c34-4673-90ff-0e9ec806d819'),('7ce252f5-c6ef-431f-96fe-fa7d817d308a','1733 83270 0708','Abelino Salazar Churunel','Callejon la comunidad primer callejon lado derecho san lorenzo el cubo','','3809-4059','Tienda frente al callejon la comunidad',1,'2023-07-18 18:50:42',1001,1003,'5b12d439-1ef0-40df-a8b4-66645a7c8e24'),('7df23de1-0b1b-41dd-b02f-6f73831a06a4',' ','Damaris Hernández','','','5339-7737','',1,'2023-07-19 17:11:49',1002,1002,'221ddeea-f9b6-44be-ae34-403148b9d605'),('7f9dcc1d-9296-4eed-a207-c4c48db5b31e','2615 63106 0312','Jenifer Tereso Gómez López','Calle principal callejon la limonada, aldea san lorenzo el cubo','','5861-4806','Electricista',1,'2023-07-19 20:38:31',1001,1003,'e47e1ec9-f331-4ce4-ac20-3b8e14d9945f'),('7fbf5186-2225-4c36-9935-62504571931a','97976-7','Kevin Rodolfo Herrera Garza','1 calle 7-66 zona 9 edificio plaza uno','','5710-2562','Guatemala',1,'2023-07-08 19:42:55',1001,1001,'0f3ab69b-b9ef-45b8-b6d5-2c3b983b2f41'),('80907fc2-5e48-4fc8-8052-95c669df02f8','0','Alejandro Soch','','','4273-8486','',1,'2023-07-18 22:18:59',1001,1004,'3e967167-f7cc-4844-a9da-793e4c61fce5'),('81a859d0-c75a-4a79-b525-04ad8c80e8e2','2446 32421 0303','Manuel Amilcar Chún García','Calle de medina callejon al campo casa no. 26 san lorenzo el cubo','','3678-9508','Carpintero',1,'2023-07-19 20:40:36',1001,1003,'f461c98e-33f4-42c4-ba99-c39ea3ba3b58'),('824704ae-5f40-447b-97ff-d8c3a70878a4',' ','Nilda Damaris Velez','','','4734-6686','',1,'2023-07-25 14:53:23',1002,1002,'5bbbf059-4879-41a9-bd39-4b441ba5ea95'),('846b958e-b37b-4c83-b8d9-acc4c2f9af72',' ','Cristofer Gabriel Hernández Jiménez','','','3141-2953','',1,'2023-07-25 15:02:51',1002,1002,'083d7c0e-0a16-44df-b813-d15098089d29'),('852cf616-42cb-46fd-801f-6768fbec6aec',' ','Erick Lorenzana','','Esposo','4088-4313','',1,'2023-07-22 00:26:54',1002,1007,'81afa2a8-9b92-4cf6-b1a4-8c9dc27b6257'),('854ae172-bac2-4e10-b8b2-a199650ea5fb',' ','Elvis Taj','','','5542-4924','',1,'2023-07-19 20:22:26',1002,1002,'091a809e-edd6-4213-ae79-7ef4505ff530'),('91a6be9f-f0ce-448f-98be-6d9f93b312df',' ','Marlon Estuardon López Taj','','','4200-5650','',1,'2023-07-25 14:32:02',1002,1002,'8953ab35-3c34-4673-90ff-0e9ec806d819'),('999fb2a8-7046-4aa4-83e3-f4665dd3f8f9','2553 18715 0312','Benda Isabel Hernandez Perez De Chavac','6 calle 1-62 b apt a zona 2 san lorenzo el cubo','','5836-4322','Ama de casa',1,'2023-07-24 14:27:06',1001,1003,'c3785d2e-4340-47d2-a59c-7f88bb732623'),('9ac2efa7-36cf-4f4b-8c0e-339eb9031c2c',' ','Yeni Ramirez','','','3589-1185','',1,'2023-07-19 20:49:17',1002,1002,'148e27a0-b5b5-442c-b87d-4968ec353333'),('9df65870-426f-465b-87c3-96f64dc805bf',' ','William Moran','','','4279-7933','',1,'2023-07-25 16:58:16',1002,1002,'7d900c5a-dfe7-48b8-8f74-db2c71457de9'),('9ea01c55-8032-454c-b67e-883e833942c3','1813 24563 0312','Wellington Vinicio Felipe Tuchan','5 av. 5-31 b zona 1','','4770-9570','Comerciante, car wash los amigos, ciudad vieja',1,'2023-07-25 14:10:22',1001,1003,'81c2f770-6e69-46f3-819c-f56c3e33a0dd'),('9eeb615f-4af7-4b1c-89e8-e85f352c5377',' ','Kimberly Yesenia Hernández Jiménez','','','3016-7369','',1,'2023-07-25 15:03:09',1002,1002,'083d7c0e-0a16-44df-b813-d15098089d29'),('a1630a93-0356-4fed-8d73-4959d04365fa',' ','Priscila Pú','','','3138-1189','',1,'2023-07-19 17:22:08',1002,1002,'748e9fdc-7514-4b02-b49a-6c500136c8ea'),('a2836bd3-3777-4d18-a7f1-099ef43073a5',' ','Wendy Gonzalez','','','5538-8467','',1,'2023-07-19 17:13:55',1002,1002,'969a16b4-2bda-4a8a-b18c-d9b25c25af34'),('a3612dfe-2029-4544-9411-d18b7ad36fb2','1979 71393 0316','Aaron Ordoñez López','C. principal no. 30 santa catarina barahona','','5927-7958','Piloto tuc tuc en santa catarina barahona',1,'2023-07-19 17:15:43',1001,1004,'68a42481-5c71-4550-bfbe-cd299488c9bb'),('a592b3e1-a4c3-466d-9447-593276e551b4',' ','Susana Maribel López Ramírez','','','5337-0157','',1,'2023-07-19 17:25:11',1002,1002,'b3d64882-65da-492e-94cd-7d721cf8b069'),('a6f40208-38ed-4cec-8a00-78c249ce7deb',' ','Irma Caná','','','5074-7006','',1,'2023-07-19 20:47:20',1002,1002,'bafe5bef-9684-4249-9a06-23462c9a1afc'),('abed7bb9-5556-41bd-a4c6-4ea823d5d687',' ','Francisco Pú','','','5119-6007','',1,'2023-07-19 17:21:54',1002,1002,'748e9fdc-7514-4b02-b49a-6c500136c8ea'),('aecb6991-1c4d-4c08-af13-010e4d06078a','3057 55366 0301','Luis Eduardo Orenos Morán','2 av. 9-63 zona 1','','5004-7133','Mantenimiento,municipalidad de ciudad vieja',1,'2023-07-25 16:57:43',1001,1003,'7d900c5a-dfe7-48b8-8f74-db2c71457de9'),('af78ab47-3a73-4b16-904e-357ee52d5ab6',' ','Vilsan Damaris Pérez','','','5636-7705','',1,'2023-07-25 17:19:22',1002,1002,'b2521ae2-6862-4d7c-9214-8dfb2ba60e7c'),('b2285e6f-31fb-4a5e-beb9-09342a7d3e16','3057 32374 0301','Steven Alejandro Santos Conjolón','4c. c 1-64 san lorenzo el cubo','','3000-9989','Hotel santo domingo',1,'2023-07-19 17:08:48',1001,1003,'221ddeea-f9b6-44be-ae34-403148b9d605'),('b473c9ec-6736-4ef2-891c-fbfba88e5252',' ','Argelia Cardenas','','','4234-7472','',1,'2023-07-22 00:28:10',1002,1002,'81afa2a8-9b92-4cf6-b1a4-8c9dc27b6257'),('b82ce48f-aa19-4eee-ba4e-8b355dac1a21',' ','Verónica Vega','','','4137-8819','',1,'2023-07-19 20:42:30',1002,1002,'608a7794-1deb-4e6b-876a-9e1d123ad6e4'),('b89f099a-c72a-4b0d-acfc-0c00e76c9220','3271 54136 1017','Dany Alberto Pú López','Segunda calle al fondo, san lorenzo el cubo','','5538-7488','Jornalero finca retana',1,'2023-07-19 17:21:34',1001,1003,'748e9fdc-7514-4b02-b49a-6c500136c8ea'),('bb9aa2e5-6537-4877-8abd-66d650d26861','1592 93324 0312','Amilcar Alfredo Garcia Vasquez','Callejon la comunidad san lorenzo el cubo','','5741-2195','Jades emmanuel',1,'2023-07-24 18:15:41',1001,1003,'7db60ec9-d0d6-4d7e-bdea-797698d3d1a7'),('bd3250b9-7769-47f9-a2ec-9ce05fe78280','1928 51330 0301','Saúl Estuardo Almengor Pereira','C. principal casa 21 aldea san lorenzo el cubo','','5702-6346','Carpintero',1,'2023-07-19 20:54:43',1001,1003,'c5e0220c-398e-47fc-b344-44f209ca77ab'),('be297434-509a-4b10-8701-4dfffdd263d4',' ','Julisa Oviedo','Ciudad vieja','Nuera','5451-5920','',1,'2023-07-18 16:53:05',1001,1003,'72255d26-f2c7-40db-a314-2a77dd37f8c2'),('bef8280e-b201-4e05-9447-fb08e38b1b70',' ','Abia Lopez','','','4429-7821','',1,'2023-07-25 15:16:59',1002,1002,'0e2f5cff-9708-4b7b-9ea3-aff816377176'),('bfe7e6f5-2275-4a48-87eb-af7214eb9202',' ','Eddy Lopez','','','5299-1820','',1,'2023-07-25 15:08:27',1002,1002,'17bb4930-3ccb-498f-b07c-1d6b6ee3084d'),('c2905dc6-c555-4f14-8868-a5b8620d1239',' ','Emanuel Rodríguez','','','3782-3830','',1,'2023-07-19 20:24:42',1002,1002,'84993d6e-cf70-488b-a92e-51154be22c36'),('c39c1e79-ceea-48ce-b19d-2a781eaa9ac0','1749 01984 0312','María Imelda Gonzalez Yuc De Sul','Callejon de la comunidad lote 17 san lorenzo el cubo','Vecina','4235-1338','Ama de casa',1,'2023-07-19 20:36:28',1003,1003,'ebfce75c-674f-4773-805a-f219f9f9ca98'),('c4e91c08-0037-4118-818f-74e4580c444f',' ','Byron Horacio González Santos','','','5503-3978','',1,'2023-07-19 20:44:08',1002,1002,'f468c827-8a81-48ab-8031-b08562b986ba'),('c5ae82d5-1d9f-4977-b2db-1727676d4902',' ','Elizabeth Hernandez','','','4203-5851','',1,'2023-07-22 00:27:32',1002,1002,'81afa2a8-9b92-4cf6-b1a4-8c9dc27b6257'),('c75b8cf1-ac8a-4360-928c-825ed31df3dd',' ','Josue Orenos','','','3141-6336','',1,'2023-07-25 16:58:06',1002,1002,'7d900c5a-dfe7-48b8-8f74-db2c71457de9'),('c7622f95-3abe-4199-914e-69bd3c7d7db5',' ','Claudia Caná Pérez','','','5010-3461','',1,'2023-07-19 20:25:55',1002,1002,'89f6d914-2124-429e-ae10-bd92a4e27a76'),('c7e10894-7e5b-4dad-83f3-e75187df693b','1603 61842 0312','Vilma Aracely Jiménez López','Calle detrás de la iglesia, san lorenzo el cubo','','4604-4197','Comerciante',1,'2023-07-25 15:02:36',1001,1003,'083d7c0e-0a16-44df-b813-d15098089d29'),('c9909a3e-d00a-4e2e-9ddf-cd0e11a23f12','1990 94020 0301','Milner Leonel Pérez Payolá','2 av. 2-08 san andres ceballos','','4173-5393','',1,'2023-07-18 18:18:34',1001,1005,'4ceae599-40aa-4a72-811d-e6faac16539d'),('c9b20694-3583-4365-984d-7e7da166ca11','1859 48162 0312','Walter Leonel Cucuy Taj','4 calle a 2-03 zona 3','','5372-3223','Agricultor',1,'2023-07-19 20:28:53',1001,1005,'653d9535-2440-4c68-9610-1773d6243dc7'),('cbcb8c61-c4f5-4dd2-b5e1-d0ab1366168c',' ','Juan Israel Lopez Zelada','','','5733-7406','',1,'2023-07-19 17:24:57',1002,1002,'b3d64882-65da-492e-94cd-7d721cf8b069'),('cd7d0733-7a27-47cd-9a2c-4f5fe56f4b6a','0','Raul Guevara','Av petapa 34-17 zona 12','','000-000','Guatemala',1,'2023-07-08 19:45:39',1001,1001,'36e90fb9-583d-474f-ad85-08f4eacf05ad'),('ce9a66b9-d6f4-47fc-b184-6d4ed281d3ab','CF','Gabriel Jimenez','San lorenzo el cubo','',' ','',1,'2023-07-22 00:50:26',1001,1003,'e1174e8f-33ed-4a42-9d89-ffce1b1f44d2'),('d4db185d-e7fd-45a4-b244-133ef2c977d2',' ','Marlon Ramirez','','','5164-1494','',1,'2023-07-19 20:49:38',1002,1002,'148e27a0-b5b5-442c-b87d-4968ec353333'),('d75f7b35-2713-428a-8a3a-8269bb1e1809',' ','Axel Bosarreyes','','','3800-9028','',1,'2023-07-19 20:28:07',1002,1002,'9729f6f7-27a5-4a3f-896f-e872e0e1c63b'),('d8488897-25d4-4746-b4e4-1035c8e88eb7','1585 694236 0301','Hector Armando Rodriguez Elias','San antonio aguas calientes','','3476-9020','Piloto de camioneta transportes brisas',1,'2023-07-19 17:47:43',1001,1005,'9b9286d6-1fc4-4cac-b5cb-89365d01b0b2'),('dcc3b1b8-015b-41d7-a5e8-438a45035a66',' ','Gabriel Ciriaco','','','3579-5966','',1,'2023-07-19 20:35:47',1002,1002,'ebfce75c-674f-4773-805a-f219f9f9ca98'),('e0a7812b-5a80-45d6-b6e2-fbaea8b1ceff',' ','Omar Veliz','','','3058-1267','',1,'2023-07-19 17:13:42',1002,1002,'969a16b4-2bda-4a8a-b18c-d9b25c25af34'),('e6fdbbca-c5fd-455f-a370-4e2492f7c8d4','1999 29114 0312','Ruth Raquel Solís López De Gonzalez','3 ave. 3-08 zona 0 san lorenzo el cubo','','5503-3978','Comerciante',1,'2023-07-19 20:43:51',1001,1003,'f468c827-8a81-48ab-8031-b08562b986ba'),('e7e8b505-1952-4dab-834f-eda9d63a2f9f',' ','Belser Cordova','','','4972-3207','',1,'2023-07-25 14:42:32',1002,1002,'110f5b95-d887-4217-94aa-011ae3a74406'),('e8a17d09-2598-4a1d-9fd3-56c03eedc174','2577 22378 0312','Lidia Maritza Camargo Hernandez De Gomez','3 calle c 5-94 zona 1','','5866-1444','',1,'2023-07-18 16:51:15',1001,1003,'72255d26-f2c7-40db-a314-2a77dd37f8c2'),('e90e4f25-5e92-478f-a2ba-fd8c17ed7c67',' ','Julia Ordoñez','','','3433-5938','',1,'2023-07-19 17:17:49',1002,1002,'68a42481-5c71-4550-bfbe-cd299488c9bb'),('e9edf6ca-6de5-413d-931f-50b38b5d5e04',' ','Lilian López','','','4993-4511','',1,'2023-07-19 17:20:20',1002,1002,'a240c6f0-b3c4-4d32-9ae8-52f0441e9560'),('ea6bfd65-31dd-4441-8e2a-17e4e6aefe92',' ','Mirna Marisol Caná','','','3715-4076','',1,'2023-07-19 20:47:11',1002,1002,'bafe5bef-9684-4249-9a06-23462c9a1afc'),('ec401b8e-f001-48aa-9a7c-077d2ac31e3f',' ','Marta Julia Cana','','','5865-5300','',1,'2023-07-25 14:10:43',1002,1002,'81c2f770-6e69-46f3-819c-f56c3e33a0dd'),('ec9693e5-058e-47d8-8303-a1b24e628194','2986 33949 0301','Ignacio Omar Hernández Nij','3 c. 3-70 aldea san lorenzo el cubo','','4430-9646','Comerciante',1,'2023-07-19 20:37:54',1001,1003,'4665aa40-8e63-4362-8f4b-0daccca5e0fa'),('edc0e780-f734-48ef-86c7-4e183d78c16a','1938 85735 0312','Dora Olimpia García Hernández','Calle real segunda parada, san lorenzo el cubo','','5964-2796','Ama de casa',1,'2023-07-25 14:31:29',1001,1003,'8953ab35-3c34-4673-90ff-0e9ec806d819'),('f033f5c2-6372-429a-87aa-97b7e4f35b54',' ','Sandra Roxana Ciriaco','','','3572-0294','',1,'2023-07-19 20:35:29',1002,1002,'ebfce75c-674f-4773-805a-f219f9f9ca98'),('f9e26929-bb9b-4e51-a062-c0ae4d60fa0a',' ','Mery Felipe','','','4843-6783','',1,'2023-07-25 14:11:03',1002,1002,'81c2f770-6e69-46f3-819c-f56c3e33a0dd'),('fe845cea-808e-4ee3-bce8-4a6b0fe7f48a','2745 07978 0312','Brandon Daniel Taj Poron','Calle principal zona 1 casa no. 44  santa catarinba barahona','','4255-1461','Comerciante',1,'2023-07-19 20:21:42',1001,1004,'091a809e-edd6-4213-ae79-7ef4505ff530'),('ff8568c1-51a8-4a8d-822b-fc21f5052309',' ','Zoila De La Cruz Morales','','','3585-5653','',1,'2023-07-19 20:44:18',1002,1002,'f468c827-8a81-48ab-8031-b08562b986ba'),('ffd76865-14cc-455f-83a6-74155c4f4977',' ','Irma Aracely Taj Guaran','','','3426-4205','',1,'2023-07-25 14:32:19',1002,1002,'8953ab35-3c34-4673-90ff-0e9ec806d819');
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
) ENGINE=InnoDB AUTO_INCREMENT=1035 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `br_brands`
--

LOCK TABLES `br_brands` WRITE;
/*!40000 ALTER TABLE `br_brands` DISABLE KEYS */;
INSERT INTO `br_brands` VALUES (1001,'Samsung',1),(1002,'Lg',1),(1003,'Rca',1),(1004,'Hisense',1),(1005,'Toshiba',1),(1006,'Compaq',1),(1007,'Acros',1),(1008,'Mabe',1),(1009,'Oster',1),(1010,'Iml',1),(1011,'Grs',1),(1012,'Whirlpool',1),(1013,'Frigidaire',1),(1014,'Black & decker',1),(1015,'Aiwa',1),(1016,'Sony',1),(1017,'Muebles helen',1),(1018,'Olympia',1),(1019,'Facenco',1),(1020,'Remington',1),(1021,'Maiesta',1),(1022,'Hamilton beach',1),(1023,'Proctor silex',1),(1024,'Picca',1),(1025,'Motorola',1),(1026,'Hp',1),(1027,'Black &amp; decker',1),(1028,'Genico',1),(1029,'Hot plate',1),(1030,'Shimano',1),(1031,'Panasonic',1),(1032,'Diamond',1),(1033,'Dream',1),(1034,'Liderbike',1);
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
) ENGINE=InnoDB AUTO_INCREMENT=1041 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ca_categories`
--

LOCK TABLES `ca_categories` WRITE;
/*!40000 ALTER TABLE `ca_categories` DISABLE KEYS */;
INSERT INTO `ca_categories` VALUES (1001,'Televisores',1),(1002,'Estufas',1),(1003,'Refrigeradoras',1),(1004,'Lavadoras',1),(1005,'Microondas',1),(1006,'Horno tostador',1),(1007,'Plancha de ropa',1),(1008,'Licuadoras',1),(1009,'Barra de sonido',1),(1010,'Bocina',1),(1011,'Torre de sonido',1),(1012,'Minicomponente',1),(1013,'Muebles',1),(1014,'Camas',1),(1015,'Belleza',1),(1016,'Soporte tv',1),(1017,'Cafeteras',1),(1018,'Percoladoras',1),(1019,'Batidoras',1),(1020,'Procesador de alimentos',1),(1021,'Olla de presion',1),(1022,'Utileria de cocina',1),(1023,'Ventiladores',1),(1024,'Celulares',1),(1025,'Computadoras',1),(1026,'Tablet',1),(1027,'Almohada',1),(1028,'Olla electrica',1),(1029,'Frigobar',1),(1030,'Congelador horizontal',1),(1031,'Licuadora portatil',1),(1032,'Estufas electricas',1),(1033,'Computadoras laptop',1),(1034,'Estufas de mesa',1),(1035,'Funda para cama',1),(1036,'Bicicletas',1),(1037,'Set de ollas',1),(1038,'Vaso de licuadora',1),(1039,'Sartenes',1),(1040,'Extractor de jugo',1);
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
) ENGINE=InnoDB AUTO_INCREMENT=1008 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ci_cities`
--

LOCK TABLES `ci_cities` WRITE;
/*!40000 ALTER TABLE `ci_cities` DISABLE KEYS */;
INSERT INTO `ci_cities` VALUES (1001,'Guatemala',1,1001),(1002,'',0,1002),(1003,'Ciudad vieja',1,1003),(1004,'Santa catarina barahona',1,1003),(1005,'San antonio aguas calientes',1,1003),(1006,'Escuintla',1,1004),(1007,'',0,1003);
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
INSERT INTO `cu_customers` VALUES (121158,'1950 15274 0312',1,'2023-07-19 20:50:06','1d298f36-ba20-44f3-b9ec-fefcb05e02e4'),(154937,'CF',1,'2023-07-21 00:20:04','3b6aa0c3-13d9-4c6a-9410-ea1e2e9c816a'),(156030,'1990 94020 0301',1,'2023-07-18 18:17:34','4ceae599-40aa-4a72-811d-e6faac16539d'),(177620,'2229 92344 1710',1,'2023-07-25 14:52:23','5bbbf059-4879-41a9-bd39-4b441ba5ea95'),(207710,'1603 61842 0312',1,'2023-07-25 15:02:08','083d7c0e-0a16-44df-b813-d15098089d29'),(217295,'000',1,'2023-07-09 01:07:23','10b9d983-db1e-4606-b069-368682b5afa1'),(263029,'1733 83270 0708',1,'2023-07-18 18:48:39','5b12d439-1ef0-40df-a8b4-66645a7c8e24'),(265789,'2846 24977 0301',1,'2023-07-25 15:07:07','17bb4930-3ccb-498f-b07c-1d6b6ee3084d'),(274216,'CF',1,'2023-07-24 16:14:01','ff352e28-971c-4bac-8c7b-5f28a0de8d5e'),(286336,'2846 24977 0301',1,'2023-07-25 15:15:45','0e2f5cff-9708-4b7b-9ea3-aff816377176'),(299916,'2709 46063 0313',1,'2023-07-18 18:55:00','a5cdb768-5b85-4db0-837b-a4fbd8c145ad'),(300391,'1787 30467 0313',1,'2023-07-18 19:00:35','bafe5bef-9684-4249-9a06-23462c9a1afc'),(317775,'1592 93324 0312',1,'2023-07-24 18:14:58','7db60ec9-d0d6-4d7e-bdea-797698d3d1a7'),(344692,'2577 22378 0312',1,'2023-07-18 16:49:36','72255d26-f2c7-40db-a314-2a77dd37f8c2'),(344965,'2257 36241 0312',1,'2023-07-18 18:53:39','9729f6f7-27a5-4a3f-896f-e872e0e1c63b'),(350487,'2615 63106 0312',1,'2023-07-18 18:59:20','e47e1ec9-f331-4ce4-ac20-3b8e14d9945f'),(384677,'1999 29114 0312',1,'2023-07-19 20:43:07','f468c827-8a81-48ab-8031-b08562b986ba'),(391271,'3057 32374 0301',1,'2023-07-18 18:07:35','221ddeea-f9b6-44be-ae34-403148b9d605'),(409507,'3062 46422 0311',1,'2023-07-18 18:56:03','ebfce75c-674f-4773-805a-f219f9f9ca98'),(465387,'2251 92160 0312',1,'2023-07-18 18:51:09','84993d6e-cf70-488b-a92e-51154be22c36'),(470829,'2012 72241 0312',1,'2023-07-24 15:18:10','0b765976-7c40-4653-a884-d1feff70c27b'),(513793,'2459 92596 0301',1,'2023-07-18 18:09:22','75674e31-bdc3-47ab-aa5a-5879313c2fac'),(528498,'2359 47725 0312',1,'2023-07-19 20:41:08','608a7794-1deb-4e6b-876a-9e1d123ad6e4'),(531314,'cf',1,'2023-07-25 17:28:41','d2a7422a-8433-4d52-a4ce-4c3d24391928'),(567726,'1938 85735 0312',1,'2023-07-25 14:31:01','8953ab35-3c34-4673-90ff-0e9ec806d819'),(607279,'1928 51330 0301',1,'2023-07-19 20:52:19','c5e0220c-398e-47fc-b344-44f209ca77ab'),(617322,'CF',1,'2023-07-22 00:56:39','c1b07586-b53a-45e3-9142-031062ac7875'),(617391,'2388 75237 0301',1,'2023-07-18 18:07:03','969a16b4-2bda-4a8a-b18c-d9b25c25af34'),(631810,'CF',1,'2023-07-22 00:47:50','e1174e8f-33ed-4a42-9d89-ffce1b1f44d2'),(636391,'3057 28180 0301',1,'2023-07-19 17:23:13','b3d64882-65da-492e-94cd-7d721cf8b069'),(636703,'2205 50867 1224',1,'2023-07-18 18:47:35','a240c6f0-b3c4-4d32-9ae8-52f0441e9560'),(640021,'3271 54136 1017',1,'2023-07-18 18:16:02','748e9fdc-7514-4b02-b49a-6c500136c8ea'),(657346,'3057 55366 0301',1,'2023-07-25 16:56:57','7d900c5a-dfe7-48b8-8f74-db2c71457de9'),(674600,'2745 07978 0312',1,'2023-07-18 18:46:06','091a809e-edd6-4213-ae79-7ef4505ff530'),(677687,'1981 81329 0312',1,'2023-07-25 17:18:23','b2521ae2-6862-4d7c-9214-8dfb2ba60e7c'),(691214,'1842 07789 0301',1,'2023-07-25 16:25:10','58f37bcf-3f14-4b0b-b264-3f3b9e0fa91a'),(711390,'1859 48162 0312',1,'2023-07-18 18:57:13','653d9535-2440-4c68-9610-1773d6243dc7'),(719522,'22446397',1,'2023-07-24 14:45:32','0768ab8c-6385-453b-9166-68ebf41e35f4'),(768580,'2084 50327 0315',1,'2023-07-18 20:20:57','2613f49d-93e1-45f6-812b-1de4a25a9b01'),(781925,'2446 32421 0303',1,'2023-07-19 20:39:49','f461c98e-33f4-42c4-ba99-c39ea3ba3b58'),(820825,'0',1,'2023-07-18 22:09:43','3e967167-f7cc-4844-a9da-793e4c61fce5'),(828599,'2553 18715 0312',1,'2023-07-24 14:25:52','c3785d2e-4340-47d2-a59c-7f88bb732623'),(844283,'1979 71393 0316',1,'2023-07-18 18:08:04','68a42481-5c71-4550-bfbe-cd299488c9bb'),(859043,'1584 28307 0312',1,'2023-07-25 14:57:38','4ba80cdd-2902-4ec3-b72d-ac07b014f09d'),(892956,'1598 32098 0501',1,'2023-07-25 14:41:03','110f5b95-d887-4217-94aa-011ae3a74406'),(893605,'1675 87544 0920',1,'2023-07-19 20:48:02','148e27a0-b5b5-442c-b87d-4968ec353333'),(901390,'2183 74976 0312',1,'2023-07-24 14:47:46','735c6789-5199-46aa-a0b9-94a5bbabc2d8'),(904274,'2638 05786 0312',1,'2023-07-18 18:52:07','89f6d914-2124-429e-ae10-bd92a4e27a76'),(914973,'2986 33949 0301',1,'2023-07-18 18:58:24','4665aa40-8e63-4362-8f4b-0daccca5e0fa'),(916450,'3162 11559 0504',1,'2023-07-22 00:22:53','81afa2a8-9b92-4cf6-b1a4-8c9dc27b6257'),(943954,'1796 67157 0312',1,'2023-07-25 15:40:42','63ced801-99a8-48fb-b2ed-f613d2581bda'),(946078,'3062 78790 0312',1,'2023-07-25 17:35:31','68d2815d-1075-406d-bac6-cd4faea8dd0b'),(970934,'1585 69423 0301',1,'2023-07-19 17:45:39','9b9286d6-1fc4-4cac-b5cb-89365d01b0b2'),(975312,'1813 24563 0312',1,'2023-07-25 14:09:37','81c2f770-6e69-46f3-819c-f56c3e33a0dd');
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
INSERT INTO `pe_persons` VALUES ('00168a7f-444c-4d59-8a9f-bcb3bbc62da8','Multiesponjas, Sociedad Anonima','sincorreo@gmail.com','5902-1958'),('04c85492-590c-4861-a392-cc17cb76be9c','Sepsa','sin2@gmail.com','4211-1678'),('0634147a-a9ee-48d2-a3a5-7c972c6ce94c','Agencias Way','sincorreo1@gmail.com','000-000'),('0768ab8c-6385-453b-9166-68ebf41e35f4','Marvin Leonel Gonzalez','sinll239sl@gmail.com','0000-0000'),('083d7c0e-0a16-44df-b813-d15098089d29','Vilma Aracely Jiménez López','4604-4197@gmail.com','4604-4197'),('091a809e-edd6-4213-ae79-7ef4505ff530','Brandon Daniel Taj Poron','brandontaj55@gmail.com','4255 1461'),('0b765976-7c40-4653-a884-d1feff70c27b','Bartolome Vasquez Vega','nnalisk3@gmail.com','3081-7504'),('0e2f5cff-9708-4b7b-9ea3-aff816377176','Israel Alejandro Pol Lopez','3273-4861@gmail.com','3273-4861'),('0f3ab69b-b9ef-45b8-b6d5-2c3b983b2f41','Mayoreo Distelsa','kherrera@distelsa.com.gt','5710-2562'),('10b9d983-db1e-4606-b069-368682b5afa1','Jose Alejandro Gonzalez Romero','sincorreo1@gsail.com','000-000'),('110f5b95-d887-4217-94aa-011ae3a74406','Leonel Francisco Florez Hernandez','159@gmail.com','sin telefono'),('116da2fb-2ac9-483a-8c6b-2f46b4b4b6e2','Diveco, Sociedad Anonima','sin@gmail.com','4013-9968'),('11984714-7fdd-402c-9e96-ae8e14a563af','Slc Trade','aguerra@slc.com.gt','3424-4526'),('148e27a0-b5b5-442c-b87d-4968ec353333','Marvin Rocael Ramírez Pérez','4817-6459@gmail.com','4817-6459'),('17bb4930-3ccb-498f-b07c-1d6b6ee3084d','Esvin Lorenzo Flores Lopez','284@gmaill.com','5385-5523'),('1d298f36-ba20-44f3-b9ec-fefcb05e02e4','María Magdalena Caná Cucuy','sinsoodk3@gmail.com','sin numero'),('221ddeea-f9b6-44be-ae34-403148b9d605','Steven Alejandro Santos Conjolón','stevnske@gmail.com','3000-9989'),('2613f49d-93e1-45f6-812b-1de4a25a9b01','Sergio Vinicio Telon Lopez','tellns3@gmail.com','4303-5317'),('34c2315d-b0b3-4be1-862f-1db6168d5880','Genico','genico@gmail.com','000-000'),('36e90fb9-583d-474f-ad85-08f4eacf05ad','Bodegangas','sac@bodegangas.com.gt','2474-2851'),('3b2bdf70-3f6c-4930-a526-7f4a6d681ae2','Baldomero Arenales','baldorender@gmail.com','35241396'),('3b6aa0c3-13d9-4c6a-9410-ea1e2e9c816a','Yesica Doriselda Hernandez Cruz','yeslk3@gmail.com','000-000'),('3e967167-f7cc-4844-a9da-793e4c61fce5','Alejandro Soch','choso3@gmail.com','4273-8486'),('4665aa40-8e63-4362-8f4b-0daccca5e0fa','Ignacio Omar Hernández Nij','ignach3@gmail.com','4430-9646'),('4ba80cdd-2902-4ec3-b72d-ac07b014f09d','Timoteo Paredes Hernandez','1584@gmail.com','5592-9550'),('4ceae599-40aa-4a72-811d-e6faac16539d','Milner Leonel Pérez Payolá','milnsi3@gmail.com','4173-5393'),('54786e44-eb51-4b14-ad95-d54539cd0a0f','Muebles Helen','muebles_helen@hotmail.com','4883-1398'),('58f37bcf-3f14-4b0b-b264-3f3b9e0fa91a','Estuardo Alejandro Perez Jimenez','4503-0259@gmail.com','4503-0259'),('5b12d439-1ef0-40df-a8b4-66645a7c8e24','Abelino Salazar Churunel','cusknk3@gmail.com','3809-4059'),('5bbbf059-4879-41a9-bd39-4b441ba5ea95','Edras Calet Velez Monrroy','4285-0985@gmail.com','4285-0985'),('608a7794-1deb-4e6b-876a-9e1d123ad6e4','Ervin Geovani Gómez López','d0-4488@gmail.com','3860-4488'),('63ced801-99a8-48fb-b2ed-f613d2581bda','Lilian Esperanza Lopez Perez De Gomez','5203-6320@gmil.copm','5203-6320'),('64116745-badb-4eda-9a55-246cb34d380b','El Gallo Mas Gallo','atencionalcliente@grupom.net','7882-4081'),('653d9535-2440-4c68-9610-1773d6243dc7','Walter Leonel Cucuy Taj','sunsk3@gmail.com','5372-3223'),('68a42481-5c71-4550-bfbe-cd299488c9bb','Aaron Ordoñez López','arrjsn3@gmail.com','5927-7958'),('68d2815d-1075-406d-bac6-cd4faea8dd0b','Josue Nehemias Godinez Gomez','4474-3314@gmail.com','4474-3314'),('72255d26-f2c7-40db-a314-2a77dd37f8c2','Lidia Maritza Camargo Hernandez De Gomez','sinorreo@fgmail.com','5866-1444'),('735c6789-5199-46aa-a0b9-94a5bbabc2d8','Martin Celada Voz','sinlal.zl3@gmail.cpom','4197-4168'),('748e9fdc-7514-4b02-b49a-6c500136c8ea','Dany Alberto Pú López','pulsnk3@gmail.com','5538-7488'),('75674e31-bdc3-47ab-aa5a-5879313c2fac','Luis Jeremías Pérez Jiménez','luisje@gmail.com','5003-6320'),('7d900c5a-dfe7-48b8-8f74-db2c71457de9','Luis Eduardo Orenos Morán','5004-7133@gmail.com','5004-7133'),('7db60ec9-d0d6-4d7e-bdea-797698d3d1a7','Amilcar Alfredo Garcia Vasquez','sijlaks@gmail.com','5741-2195'),('81afa2a8-9b92-4cf6-b1a4-8c9dc27b6257','Milvia Vivas Lopez','n121@gmail.com','4088-4313'),('81c2f770-6e69-46f3-819c-f56c3e33a0dd','Wellington Vinicio Felipe Tuchan','4770-9570@gmail.com','4770-9570'),('837f62ed-560d-464c-ba2a-06ddf76e1c03','Tecno Facil Outlet','tf.outletsanjuan@distelsa.com.gt','2432-6286'),('84993d6e-cf70-488b-a92e-51154be22c36','Ana Patricia Gómez Rodríguez','arriolaany894@gmail.com','5592-3093'),('86302e2b-809c-490c-819a-367f88f4af67','Jesus Navarro','jesusns1902@gmail.com','523481468309'),('8953ab35-3c34-4673-90ff-0e9ec806d819','Dora Olimpia García Hernández','5964-2796@gmail.com','5964-2796'),('89f6d914-2124-429e-ae10-bd92a4e27a76','Edgar Eduardo Caná Perez','edgans3@gmail.com','5191-5388'),('969a16b4-2bda-4a8a-b18c-d9b25c25af34','Luis Alfredo Fernández','luisafe@gmail.com','3012-0301'),('9729f6f7-27a5-4a3f-896f-e872e0e1c63b','Nelson Estuardo Bosarreyes López','bosarreyes09@gmail.com','5996-5372'),('9b9286d6-1fc4-4cac-b5cb-89365d01b0b2','Hector Armando Rodriguez Elias','snkksao3@gmail.com','3476-9020'),('a240c6f0-b3c4-4d32-9ae8-52f0441e9560','Geiny Osberto Gómez Ortiz','carlusn3@gmail.com','5203-6320'),('a5cdb768-5b85-4db0-837b-a4fbd8c145ad','Handersson Geovany Perez Arenales','andksk3@gmail.com','4268-5314'),('b03edfb9-84ae-482c-a600-432cfdad6aa9','La Bodegona','sincorre@gmail.com','5454-5025'),('b2521ae2-6862-4d7c-9214-8dfb2ba60e7c','Wilfredo González Rodríguez','5535@gmail.com','5535-5150'),('b3d64882-65da-492e-94cd-7d721cf8b069','Juan Fernando Lopez Ramirez','fr099836@gmail.com','5123-6325'),('bafe5bef-9684-4249-9a06-23462c9a1afc','Carlos Humberto Otoy Quexel','chunsot@gmail.com','4943-1902'),('c1b07586-b53a-45e3-9142-031062ac7875','Patricia Vasquez','jjalsdkj3@gmail.com','3199-6119'),('c3785d2e-4340-47d2-a59c-7f88bb732623','Brenda Isabel Hernandez','nlsoknn33@gmail.com','5836-4322'),('c5e0220c-398e-47fc-b344-44f209ca77ab','Saúl Estuardo Almengor Pereira','5702-6346@gmail.com','5702-6346'),('c70dd5a9-f7a8-4964-a0c5-f6310bc1dddd','Gudiel Xulu','mariano@gmail.com','58975487'),('d2a7422a-8433-4d52-a4ce-4c3d24391928','Lucrecia Hernández Cardenas','jlsoi3sksk@gmail.coms','0000-0000'),('d6169c9d-4f21-46ef-8030-ff6ebbdedc1a','Comercial El Porteño','ellsalioi3@gmail.com','7889-0575'),('dab4a868-dd48-4363-bcaa-14619938406e','Distribuidora Acuario','4@gmaiul.com','5413-3643'),('e1174e8f-33ed-4a42-9d89-ffce1b1f44d2','Gabriel Jimenez','sinsll3k2@gmail.com','0000-0000'),('e47e1ec9-f331-4ce4-ac20-3b8e14d9945f','Jenifer Tereso Gómez López','jensgos3@gmail.com','5861-4806'),('e63803eb-bba1-4191-917a-8320849fbd20','Billion Home','sinjo2@gmail.com','000-000'),('ea01b71f-51df-4e9a-a402-018e399e611b','Baldomero Arenales','baldoarenas8@gmail.com','3524-1396'),('ebfce75c-674f-4773-805a-f219f9f9ca98','Miriam Fabiola Ciriaco Sunún','jksnk3@gmail.com','42609403'),('f461c98e-33f4-42c4-ba99-c39ea3ba3b58','Manuel Amilcar Chún García','nksl3@gmaill.com','3678-9508'),('f468c827-8a81-48ab-8031-b08562b986ba','Ruth Raquel Solís López De Gonzalez','5503-3978@gmail.com','5503-3978'),('f98ff4d9-a90c-44a2-9a11-2c3b492dc510','Hamilton Xulu','hamidaniel16@gmail.com','4184-7857'),('ff352e28-971c-4bac-8c7b-5f28a0de8d5e','Devora Leticia Hernandez','nisllakj3@gmail.com','0000-0000');
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
INSERT INTO `pr_products` VALUES ('03C5DFCF7DC34556','520102','SET DE SARTENES PICCA 3 PIEZAS GRIS MARMOL','PI003SSMP','3 SARTENES DIFERENTES TAMAÑOS',290,450,690,1,'2023-07-24 17:05:26',1039,1024,170372),('04BBC945496F4A08','7','LICUADORA OSTER 8 VELOCIDADES VASO DE VIDRIO BLANCO','BLSTMG-W00','8 velocidades, vaso de vidrio.',340,490,590,1,'2023-07-08 23:01:44',1008,1009,170372),('0508603A57FE4AB9','50','ESTUFA CON HORNO ACROS 20\" NEGRA TOP NEGRO','LNAW1001B00','4 hornillas color negro',1460,2050,3050,1,'2023-07-11 17:18:08',1002,1007,170372),('08880B600B0D49AF','53','PLANCHA OSTER A VAPOR CON SUELA ANTIADHERENTE PALO ROSA','GCSTBS3801','a vapor suela antiadherente palo rosa',170,300,360,1,'2023-07-11 17:21:31',1007,1009,571770),('08E8815178F64A8B','12','ROPERO NOVO MUEBLES HELEN','ROPNOVO','ropero',2400,3300,4620,1,'2023-07-08 23:11:23',1013,1017,813063),('098E6298EE46420F','26','LICUADORA BLACK&DECKER 10 VELOCIDADES JARRA DE PLASTICO ROJO','BLBD210PP','10 velocidades , roja , jarra vidrio.',209.3,420,500,1,'2023-07-08 23:30:30',1008,1027,415958),('0A53251C5C4646DA','1','ESTUFA CON HORNO OSTER 20\" GRAFITO TOP INOXIDABLE','OS-GSBCT20BS','ESTUFA CON HORNO OSTER 20\" GRAFITO TOP INOXIDABLE',1260,1920,2950,1,'2023-07-08 22:42:32',1002,1009,571770),('0C5FACC960FD4D23','48','BARRA DE SONIDO AIWA 40 W (BT/AUX/USB/HDMI)','AWSBH1','40 watts con bluetooth auxiliar usb y hdmi',595,850,1380,1,'2023-07-11 17:15:46',1009,1015,170372),('0CE2F51125A247F2','93','ESTUFA DE MESA IML 4 HORNILLAS MARFIL TOP INOXIDABLE','C-4M','4 hornillas de mesa',422,650,930,1,'2023-07-11 18:11:21',1034,1010,571770),('0D34DEAE83F74276','27','BATIDORA MANUAL OSTER 6 VELOCIDADES BLANCA','FPSTHM3532','6 velocidades, blanca.',315,425,500,1,'2023-07-08 23:31:34',1019,1009,160039),('0E1BF3CD91F54847','51','ESTUFA CON HORNO RCA 20\" GRIS TOP INOXIDABLE','RCCR24','4 hornillas gris inoxidable',1349,2000,3000,1,'2023-07-11 17:19:11',1002,1003,571770),('119A0F8D25484193','38','TELEVISOR TOSHIBA 32\" SMART HD LED','32V35KB','televisor de 32 pulgadas high definition led',1676.92,2490,3350,1,'2023-07-11 16:56:21',1001,1005,207812),('163F4251944846ED','60','PLANCHA OSTER A VAPOR CON SUELA ANTIADHERENTE ROJO','GCSTBS5004','a vapor color rojo antiadherente',197,300,360,1,'2023-07-11 17:29:26',1007,1009,571770),('17B5FC1821D94156','34','PLANCHA PARA CABELLO REMINGTON ALISADORA EDICION LIMITADA (OBSEQUIOS) NEGRO','S3500','plancha de cabello',315,499,740,1,'2023-07-08 23:40:19',1015,1020,170372),('184D49A4D8444EAD','6','LICUADORA BLACK&DECKER 10 VELOCIDADES JARRA DE VIDRIO NEGRO','BLBD210GB','10 velocidades negra, de vidrio.',198,450,550,1,'2023-07-08 23:00:17',1008,1027,190196),('19B32FE3B9AD4EED','2','ESTUFA CON HORNO ACROS 20\" NEGRO Y GRIS TOP NEGRO','LAW5300S00','color gris con negro',1615,2050,3050,1,'2023-07-08 22:45:00',1002,1007,170372),('1BEAA6617B1A4408','14','ROPERO ESPAÑOL MUEBLES HELEN','ROPESPANOL','ropero',2725,3650,5580,1,'2023-07-08 23:15:30',1013,1017,813063),('1C93512DFE5A49FE','8MWTW2024WLG','LAVADORA WHIRLPOOL DE 44 LBS TAPA DE VIDRIO CON XPERT CYCLE  GRIS','8MWTW2024WLG','44 libras',3587,4680,6600,1,'2023-07-25 16:59:52',1004,1012,207812),('1DC8418629714E85','44652088964','BICICLETA DIAMOND 26 TM730 24SPEED MARCO CURVO','DIAMONDTM730',' ',1900,2550,3160,1,'2023-07-24 17:34:53',1036,1032,342271),('1E3D51AEBF4A4894','4221165','LICUADORA OSTER 2 VEL. CONTROL DE PULSO VASO DE VIDRIO BLANCO','BLSTKAG-WPB','VASO DE VIDRIO',385,550,650,1,'2023-07-24 17:08:02',1008,1009,170372),('1E6CFE52CDC74CB9','41','CAMA OLYMPIA ANTIESTRES ORTOPEDICA MATRIMONIAL ANTIZANCUDOS','ANTIESTRESORTMATRI','ortopedica matrimonial con tratamiento anti-zancudos',1888.45,2890,3950,1,'2023-07-11 17:02:18',1014,1018,109822),('1F70004FC1C34E42','19','PLANCHA PARA CABELLO REMINGTON PRO-ION STRAIGHT ','S7710','plancha de cabello',279,499,700,1,'2023-07-08 23:23:07',1015,1020,415958),('20D76F4847AB4D54','15','ROPERO MILAN MUEBLES HELEN','ROPMILAN','ROPERO',2425,3450,5280,1,'2023-07-08 23:17:32',1013,1017,813063),('219F92BBC474450C','17','TRINCHANTE ZENIA MUEBLES HELEN','TRINZENIA','trinchante',3075,4150,6000,1,'2023-07-08 23:19:57',1013,1017,813063),('223B3F321B7049E0','74','VENTILADOR DE 12\"  PEDESTAL ROJO ','VEN12ROJO','12 pulgadas color rojo',160,250,250,1,'2023-07-11 17:48:15',1023,1028,864663),('24462CC7CCCB45A2','69','CAMA OLYMPIA EDICIÓN ESPECIAL CHAPINA MATRIMONIAL BOX TOP','EECHMATRI1BTS','edición julio chapina matrimonial',1272,1920,2850,1,'2023-07-11 17:42:13',1014,1018,109822),('259EDE7359C14D6A','96','PLANCHA OSTER A VAPOR CON SUELA ANTIADHERENTE LILA','GCSTBS6005','a vapor antiadherente color lila',260,360,410,1,'2023-07-11 18:14:49',1007,1009,571770),('275D83AEBC19460B','98','LAVADORA MABE DE 44 LBS CON TECNOLOGÍA AQUA SAVER GREEN BLANCA','LMA70213CBAB0','44 libras color blanca',3313,4450,6420,1,'2023-07-11 18:16:55',1004,1008,207812),('282B9B8BA3EB4799','30','PROCESADOR DE ALIMENTOS BLACK&DECKER 8 TAZAS BLANCO','FP1337','procesador 8 tazas',390,590,750,1,'2023-07-08 23:35:42',1020,1027,170372),('2973B2D55CD04745','65','TELEVISOR COMPAQ 32\" SMART ANDROIDTV','QLG32','32 pulgadas con sistema android',1395,2195,3200,1,'2023-07-11 17:37:42',1001,1006,170372),('2DB64881CF144F24','20','SECADORA DE CABELLO REMINGTON THERMACARE','D12A','secadora de cabello',281.8,399,520,1,'2023-07-08 23:23:59',1015,1020,415958),('3389135FF94949D6','58','REFRIGERADORA MABE 8 PIES FROST 1 PUERTA CON DISPENSADOR SILVER','RMU210FANU','8 pies 1 puerta con dispensador color silver',2049,2960,4200,1,'2023-07-11 17:27:42',1003,1008,207812),('3561AE8C34CB4A13','47','OLLA DE PRESIÓN PICCA 5 LITROS MARMOL GRIS','PI00050PG','5 litros de mármol color gris',265,500,600,1,'2023-07-11 17:13:53',1021,1024,170372),('382F4FFD093D4AB7','67','HORNO MICROONDAS OSTER 1,1 PIES CUBICOS MARCO DE ACERO','OGGM61002','1,1 pies marco de acero',699,1100,1440,1,'2023-07-11 17:39:52',1005,1009,207812),('39BADCEC7C67457E','45211','SET DE OLLAS PICCA  7 PCS MARMOL TURQUESA','P1007BMU','JUEGO DE OLLAS',490,750,990,0,'2023-07-24 16:51:03',1037,1024,170372),('3AD4D64160CE4028','86','CAMA OLYMPIA EDICIÓN ESPECIAL CHAPINA MATRIMONIAL DOBLE BOX TOP','EECHMATRI2BTS','doble box top edición julio chapina',1570,2500,3100,1,'2023-07-11 18:01:06',1014,1018,109822),('3AFBED8FAFEC4D7D','88','BOCINA BLUETOOTH ABS COLORES','MS-2678BT','bocina con bluetooth y luces',153,250,999,1,'2023-07-11 18:03:45',1010,1028,308689),('3DBF3CAD8E6F4633','8MWTW1713WJM','LAVADORA WHIRLPOOL DE 38 LBS TAPA DE VIDRIO CON XPERT CYCLE BLANCA','8MWTW1713WJM','38 LIBRAS',3500,4390,1545,1,'2023-07-25 16:47:22',1004,1012,571770),('407CF69A132F4264','28','OLLA MULTIUSO BLACK&DECKER 3 LITROS','MCH14','multifuncion para 3 litros',450,715,870,1,'2023-07-08 23:33:10',1028,1027,190196),('40E6DA39C004482E','99','PROTECTOR DE CAMA OLYMPIA QUEEN','EDREDONQUEEN','funda para cama queen',80,150,999,1,'2023-07-11 18:18:14',1035,1018,109822),('427F765F23944413','59','REFRIGERADORA MABE 10 PIES TOP MOUNT CON DISPENSADOR SILVER','RMA250PJMRU1','10 pies con dispensador',3085,4190,5340,1,'2023-07-11 17:28:37',1003,1008,207812),('4284EB52D1124C6F','11','MINICOMPONENTE LG Xboom CJ45 8500 WATTS CON WOOFER (USB/CD/BT)','LG-CJ45','8500 watts, 2 bocinas mas el woofer',1899,2595,3600,1,'2023-07-08 23:09:07',1012,1002,190196),('4349362C8D814D10','36','COMBO DE ALISADORA, ONDULADORA Y SECADORA REMINGTON ROJO','S5520-D3015MP','alisadora, onduladora y secadora',550,799,1000,1,'2023-07-11 16:52:30',1015,1020,170372),('439D87D29ED24B31','10','ALMOHADA DE FIBRA ESTANDAR ','ALM3','almohada',1,25,25,1,'2023-07-08 23:06:58',1027,1018,109822),('47B65C5EE02747D1','445215588','BICICLETA DIAMOND BMX NO. 16 CARS NIÑO','BMX16CARS','BICICLETA PARA NIÑO EDICION CARS',625,850,1120,1,'2023-07-24 17:21:35',1036,1032,342271),('4949245C63C743EA','4520112','TORRE DE SONIDO PANASONIC DE 13200W CON DVD/CD/FM/USB/BLUETOOTH MAX DANCE ILLUMINATION','SC-TMAX40','de 13,200 watts',2895,3950,5400,1,'2023-07-24 17:15:25',1011,1031,170372),('50DAA31CDC9C41B3','556216558','BICICLETA DIAMOND STEEL 26 CACHOS 21 SPEED FRENO DE DISCO','STEEL21','BICICLETA COLOR NEGRA CON VERDE',1275,1890,2600,1,'2023-07-24 17:30:36',1036,1032,342271),('52F44C4F3E9043CD','40','LAVADORA MABE DE 42 LBS CON TECNOLOGÍA AQUA SAVER GREEN BLANCA','LMA79113VBAB0 ','lavadora de 42 libras color blanca',3289,4250,6120,1,'2023-07-11 16:58:51',1004,1008,207812),('53BCD6AB3B5C410B','455621','HORNO MICROONDAS WHIRLPOOL DE 0.7 PIES CUBICOS SILVER','WM1807D','Color gris',612,890,1110,1,'2023-07-08 22:55:10',1005,1012,207812),('5569E58281A14752','43','PROCESADOR DE PULSO PROCTOR SILEX 1.5 TAZAS BLANCO','PS72500PS','1.5 tazas color blanco',145,200,200,1,'2023-07-11 17:05:40',1020,1023,571770),('58057F18F7EB4B2C','79','TELEVISOR HISENSE 32\" SMART HD LED','32A4KV','32 pulgadas hd led',1146,1950,3000,1,'2023-07-11 17:54:04',1001,1004,207812),('581A4C9BEB8742C5','29','LAVADORA WHIRLPOOL DE 48 LBS TAPA DE VIDRIO CON XPERT CYCLE BLANCA','8MWTW2224WJM','48 libras',3525,4790,6840,1,'2023-07-08 23:34:31',1004,1012,207812),('5B381E02A3BE466D','92','COMPUTADORA PORTATIL HP 14DQ0509LA','HP14DQ0509LA','laptop hp',2798,3499,5400,1,'2023-07-11 18:10:26',1033,1026,190196),('5CCCD6DABA16412E','50C350KB','TELEVISOR TOSHIBA 50\" SMART 4K ULTRA HD','50C350KB','50 pulgadas',2936,4110,2200,1,'2023-07-25 17:38:15',1001,1005,207812),('5FEF440C5E774E26','62','HORNO TOSTADOR BLACK&DECKER BLANCO','TO134W','horno tostador',355,590,660,1,'2023-07-11 17:33:10',1006,1027,170372),('643DFC15F36749CB','4452154','LAVADORA WHIRLPOOL DE 44 LBS CON XPERT SYSTEM BLANCA','8MWTW2024WJM','44 LIBRAS COLOR BLANCA CON PANEL COLOR GRIS',3407,4520,6820,1,'2023-07-24 17:01:38',1004,1012,207812),('65C667755CC74BB5','80','TELEVISOR HISENSE 43\" SMART HD LED','43H5G','43 pulgadas hd led',2088,3090,4159,1,'2023-07-11 17:54:47',1001,1004,207812),('67FD2B5F7EE6429A','73','REFRIGERADORA MABE 8 PIES 1 PUERTA CON DISPENSADOR FROST GRIS','RMC181PYMRXO','8 pies 1 puerta con dispensador',1900,2890,4200,1,'2023-07-11 17:46:27',1003,1008,367486),('68FA418121874A0B','5520221645','BICICLETA DREAMS BMX NO. 16 PRINCESA CON CANASTA','BMX16PRINCESA','PARA NIÑA BICICLETA CON CANASTA',680,920,1180,1,'2023-07-24 17:27:03',1036,1033,342271),('6BBB0BCC5DB845D3','13','ROPERO BELIAN MUEBLES HELEN','ROPBELIAN','ropero',2850,3745,5760,1,'2023-07-08 23:13:12',1013,1017,813063),('6BBFCDC1CC4C41D1','456628','LICUADORA OSTER 2 VEL. CONTROL DE PULSO VASO DE VIDRIO ROJO','BLSTKAG-RPB','VASO DE VIDRIO',385,550,650,1,'2023-07-24 17:09:50',1008,1009,170372),('6C0B4D18C6B14596','61','PLANCHA OSTER A VAPOR CON SUELA ANTIADHERENTE GRIS','GCSTBS5001','a vapor color gris antiadherente',197,300,360,1,'2023-07-11 17:30:13',1007,1009,571770),('6C1FEBDEBE36402F','52','PLANCHA SECA LIVIANA OSTER CELESTE Y BLANCO','GCSTBV4112','sin vapor color celeste y blanco',197,295,350,1,'2023-07-11 17:20:22',1007,1009,571770),('6CE44EE20A6A4143','18','CUCHILLA PARA LICUADORA OSTER ORIGINAL','BLSTAA4961','cuchilla para licuadora',44,80,0,1,'2023-07-08 23:21:36',1008,1009,571770),('6D160E13A67947CC','71','TELEVISOR SAMSUNG 55\" SMART LED 4K UHD ','UN55AU7000P','55 pulgadas smart led 4k UHD',4800,5850,7800,1,'2023-07-11 17:44:14',1001,1001,170372),('6EF3630D6BF74808','57','TELEVISOR SAMSUNG 43\" SMART LED 4K ULTRA HD','UN43AU7000P','43 pulgadas ultra hd 4k',3400,4250,5640,1,'2023-07-11 17:26:34',1001,1001,170372),('7089EEA2115349E8','47785','VASO DE VIDRIO OSTER CROMADA 2 VELOCIDADES ','46515','VASO DE VIDRIO SOLO CROMADA',105,150,999,1,'2023-07-24 16:57:23',1038,1009,170372),('70A20FA34E0A40B6','31','BATIDORA BLACK&DECKER MANUAL Y DE TAZÓN BLANCA','MX900','tazon de vidrio',365,590,750,1,'2023-07-08 23:36:53',1019,1027,170372),('72715C9985804D13','465206088','BICICLETA DIAMOND STEEL 26 CACHOS 21 SPEED FRENO DE DISCO','STEEL21','BICICLETA NEGRA CON CELESTE',1275,1890,2600,1,'2023-07-24 17:31:59',1036,1032,342271),('739A7DBE77D74134','25','LICUADORA BLACK&DECKER 10 VELOCIDADES JARRA DE VIDRIO BLANCO','BLBD210GW','10 velocidades, blanca, jarra de vidrio.',244.3,450,550,1,'2023-07-08 23:29:30',1008,1027,415958),('743ACCACD37E40E1','22','SOPORTE DE PARED MAIESTA PARA TV DE 26\"-63\" FIJO','RACKF26-63','soporte tv',35,120,0,1,'2023-07-08 23:26:15',1016,1021,308689),('79D3C5FEEEF34EE5','77','ESTUFA CON HORNO MABE 30\" NEGRO CON PARILLAS DE HIERRO FUNDIDO','EM7658BFIN1','6 hornillas con parrillas de hierro fundido',2708,3650,4740,1,'2023-07-11 17:52:18',1002,1008,207812),('7E27382FA06242BA','81','TELEVISOR TOSHIBA 55\" SMART UHD-4K HDR','55C350LS','55 pulgadas smart UHD 4K',3116,4110,5580,1,'2023-07-11 17:55:39',1001,1005,207812),('7F0A93011DBD4498','8','LICUADORA OSTER 8 VELOCIDADES VASO DE VIDRIO TURQUESA','BLSTMG-T15','8 velocidades, verde, vaso vidrio.',364.95,490,590,1,'2023-07-08 23:04:08',1008,1009,170372),('801688DEFFFE4E22','42','PROCESADOR DE PULSO PROCTOR SILEX 1.5 TAZAS NEGRO','PS72507','1.5 tazas color negro',145,200,200,1,'2023-07-11 17:04:48',1020,1023,571770),('82A65252FBF44C7B','85','CONGELADOR HORIZONTAL HISENSE DE 15 PIES CUBICOS BLANCO','FC15D6BWX','horizontal de 15 pies color blanco',3446,4490,6600,1,'2023-07-11 17:59:59',1030,1004,207812),('88C5BC3C69DB41CA','45221','VASO VIDRIO OSTER 8 VELOCIDADES  ;   VASO VIDRIO OSTER CROMADA ','46515  ;  BLSTMG ','VASO DE VIDRIO PARA DOS MODELOS DIFERENTES',105,150,999,1,'2023-07-24 16:59:00',1038,1009,170372),('8C1E18D106AC43C9','EEFIMPERIAL1BTS','CAMA OLYMPIA EDICIÓN ESPECIAL FUTBOLERA IMPERIAL BOX TOP ','EEFIMPERIAL1BTS','imperial futbolera',982,1390,930,1,'2023-07-25 17:31:31',1014,1018,109822),('8C4D3361881E41B0','89','ESTUFA ELECTRICA 1 HORNILLA 1000W','JX-1010B','1 hornilla electrica',93.9,175,999,1,'2023-07-11 18:04:49',1032,1029,308689),('8F06CF32E4D943BA','21','SOPORTE DE PARED MAIESTA PARA TV DE 14\"-42\" FIJO','RACKF14-42','colgar tv',24,80,0,1,'2023-07-08 23:25:22',1016,1021,308689),('93D43B7B12744D41','24','CAFETERA BLACK&DECKER 12 TAZAS JARRA DE VIDRIO PANEL DIGITAL NEGRO','CM1105B','12 tazas jarra de vidrio',200.83,440,500,1,'2023-07-08 23:28:05',1017,1027,415958),('942924E8921346B6','452154','LICUADORA OSTER 2 VEL. CONTROL DE PULSO VASO DE VIDRIO AZUL','BLSTKAG-LPB','VASO DE VIDRIO',385,550,650,1,'2023-07-24 17:08:53',1008,1009,170372),('98316E28CB1A4993','78','HORNO MICROONDAS OSTER DE 0,7 PIES CUBICOS NEGRO','OGKEW2702','0.7 pies color negro',565,825,1050,1,'2023-07-11 17:53:11',1005,1009,207812),('98966392F6904ECD','72','CAMA OLYMPIA EDICIÓN ESPECIAL CHAPINA IMPERIAL BOX TOP','EECHIMPERIAL1BTS','edición julio chapina imperial box top',1033,1490,2160,1,'2023-07-11 17:45:21',1014,1018,109822),('9897398DB1244D31','84','FRIGOBAR HISENSE 3,3\" 2 PUERTAS GRIS','RT33D6AAE','3,3 2 puertas color gris',1366,1890,2900,1,'2023-07-11 17:58:38',1029,1004,207812),('995B35B719F044E1','49','ESTUFA CON HORNO ACROS 30\" GRIS TOP INOXIDABLE','LAF5333D','6 horinillas con horno inoxidable',2339,3530,4620,1,'2023-07-11 17:17:07',1002,1007,170372),('997450717323425F','16','ROPERO ZADA MUEBLES HELEN','ROPZADA','ropero',2625,3590,5400,1,'2023-07-08 23:18:44',1013,1017,813063),('9BB98F64031243F9','4452254','EXTRACTOR DE JUGOS BLACK&DECKER QUIET SILENCIOSO COLOR NEGRO','JE2500B-LA','para todo tipo de jugos',395,625,780,1,'2023-07-24 17:16:46',1040,1027,170372),('A2E00980A9914729','54','LAVADORA SAMSUNG BLANCA 42 LBS CON TECONOLOGIA DUAL STORM','WA19A3353GW','capacidad para 42 libras color blanca',3391,4390,6300,1,'2023-07-11 17:22:35',1004,1001,207812),('A4324308721D427D','445215','SET DE OLLAS PICCA 7 PCS MARMOL GRIS','P1007BMC','OLLAS COLOR GRIS',480,750,990,1,'2023-07-24 16:52:22',1037,1024,170372),('A5275D06C19C48D4',' 4','ESTUFA CON HORNO MABE 30\" NEGRO Y GRIS TOP NEGRO','EM7622BAPS','color gris con negro',2072,3120,4380,1,'2023-07-08 22:29:36',1002,1001,207812),('A9F972B4EF7E4508','83','TORRE DE SONIDO SONY DE 450W CON DVD/CD/FM/USB/BLUETOOTH NCF E ILUMINACIÓN','MHCV43D','450w con ncf iluminación y woofer max',3210,4290,5700,1,'2023-07-11 17:57:30',1011,1016,207812),('AAC17EAA12664518','63','HORNO TOSTADOR BLACK&DECKER NEGRO','TO134B','horno tostador',355,590,660,1,'2023-07-11 17:33:53',1006,1027,170372),('AB68731198214EDA','44','ESTUFA CON HORNO ACROS 30\" NEGRO TOP INOXIDABLE','LAF5333B00','6 hornillas parrillas de alambron',2715,3530,4620,1,'2023-07-11 17:07:39',1002,1007,170372),('ADD6F54D055D43EA','91','COLCHON COMFORTEX PLUS IMPERIAL','COLCHCOMFORTEX','plus imperial',100,650,1099,1,'2023-07-11 18:08:56',1014,1019,190196),('AF3E8B3C75E54F86','95','PLANCHA OSTER A VAPOR CON SUELA ANTIADHERENTE CELESTE','GCSTBS6004','a vapor suela antiadherente celeste',250,360,410,1,'2023-07-11 18:13:29',1007,1009,571770),('B03725D0D57548AE','97','PLANCHA OSTER A VAPOR CON SUELA ANTIADHERENTE MENTA','GCSTBS5002','a vapor antiaherente color menta',197,300,360,1,'2023-07-11 18:15:47',1007,1009,571770),('B0BEC05418474437','75','VENTILADOR DE 10\" PEDESTAL AMARILLO','VEN10AMARILLO','de pedestal color amarillo',150,230,230,1,'2023-07-11 17:50:26',1023,1028,864663),('B49F3CBAEE224C2B','455','SOPORTE DE PARED MAIESTA PARA TV DE 14\"-55\" MOVIBLE','RACKM14-55','SOPORTE TV',68,175,999,1,'2023-07-24 16:42:03',1016,1021,308689),('B85255FDFE60431E','87','VASO EXPRIMIDOR DE JUGOS 380ml','HM-03','vaso licuadora portatil 380 ml',62.18,125,999,1,'2023-07-11 18:02:51',1031,1028,308689),('BA384E4E76F04409','55','TELEVISOR SAMSUNG 32\" SMART HD','UN32T4300','32 pulgadas smart hd',1800,2600,3550,1,'2023-07-11 17:24:23',1001,1001,170372),('BBB8B203245B4741','37','COMBO DE SECADORA Y ALISADORA DE CABELLO REMINGTON ROSE GOLD','D3015-S1520','secadora, alisadora.',450,699,900,1,'2023-07-11 16:53:42',1015,1020,170372),('BC5E2241D5AA432F','45','CAMA OLYMPIA EDICIÓN ESPECIAL ONE PHILLOW IMPERIAL','EEONEPHILLIMP','one pillow imperial (economica)',868,1290,1880,1,'2023-07-11 17:10:02',1014,1018,109822),('BF2A96989E714B58','68','HORNO MICROONDAS FRIGIDAIRE DE 0,7 PIES CUBICOS SILVER','FMDO20S3GSPG','0,7 pies color gris',590,890,1110,1,'2023-07-11 17:40:50',1005,1013,207812),('C2E127BD1ED34FA4','3','REFRIGERADOR MABE 9 PIES TOP MOUNT GRIS MATE ','RMA230PVMRG1','Color gris mate',2708,3690,4920,1,'2023-07-08 22:47:00',1003,1008,207812),('C33095A2D20343F4','33','LICUADORA OSTER TRADICIONAL 2 VELOCIDADES VASO PLASTICO','4170','vaso de plastico',425,655,840,1,'2023-07-08 23:38:58',1008,1009,170372),('C818D1242A9247C6','94','ESTUFA DE MESA IML 4 HORNILLAS GRIS TOP INOXIDABLE','C-4G','4 hornillas inoxidable color gris',422,650,930,1,'2023-07-11 18:12:16',1034,1010,571770),('C9222F249609435C','70','CAMA OLYMPIA EDICIÓN ESPECIAL CHAPINA KING BOX TOP','EECHKING1BTS','edición julio chapina King box top',1987,2840,3950,1,'2023-07-11 17:43:14',1014,1018,109822),('CBF0BD46B0F243E2','100','BICICLETA SHIMANO RELAMPAGO NO. 26 NEGRO Y ROJO','RELAMPAGO26','no 26 color combinado rojo y negro',1000,1600,2500,1,'2023-07-11 18:19:50',1036,1030,367486),('CE970787F7054FD5','66','LAVADORA WHIRLPOOL DE 44 LBS CON XPERT SYSTEM BLANCA','8MWTW2024MJM','capacidad 44 libras color blanca con panel gris',3352,4520,6480,1,'2023-07-11 17:38:44',1004,1012,207812),('CEF01AD00A134623','4587','OLLA DE PRESIÓN PICCA 5 LITROS MARMOL ROJA','PI00050PR','5 LITROS COLOR ROJA',299,525,600,1,'2023-07-24 16:47:24',1021,1024,170372),('CFF1278785E84735','46','CAMA OLYMPIA EDICIÓN ESPECIAL ONE PHILLOW MATRIMONIAL','EEONEPHILLMATRI','one phillow matrimonial (economica)',1160,1750,2700,1,'2023-07-11 17:11:06',1014,1018,109822),('D09DFB4B38C743CA','410215874','BICICLETA LIDERBIKE BMX NO. 20 FREESTYLE TOPSPEED','BMX20FREESTYLE','BMX PARA NIÑO',975,1490,2040,1,'2023-07-24 17:28:34',1036,1034,342271),('D0A25079C11842E3','ALLOY26CXR','BICICLETA DIAMOND 26 ALLOY CXR TOURNEY 24SPEED ','ALLOY26CXR',' ',1800,2420,3040,1,'2023-07-24 17:33:58',1036,1032,342271),('D1484955A26C4B8D','3454fg','LAVADORA WHIRLPOOL DE 40 LBS TAPA DE METAL CON XPERT CYCLE BLANCA','8MWTW1813MJM','40 libras',3291,4390,5450,1,'2023-07-25 14:35:32',1004,1012,207812),('D3CE6985E1FE45DC','35','TELEVISOR HISENSE 43\" SMART UHD-4K HDR LED','43A7GV','43 pulgadas ultra hd con 4k',2120,3090,4680,1,'2023-07-08 23:42:10',1001,1004,207812),('D66EF280B6C648A1','WA17T7G6DWW','LAVADORA SAMSUNG DE 38 LBS CON TECNOLOGÍA WOOBLE BLANCA','WA17T7G6DWW','38 libras',3113,4120,1635,1,'2023-07-25 15:53:17',1004,1001,564338),('D7AB03B5B528446B','5','CAFETERA BLACK&DECKER 10 TAZAS JARRA DE VIDRIO NEGRO','DCM1100B','para 10 tazas, jarra de vidrio.',150,320,390,1,'2023-07-08 22:58:48',1017,1027,190196),('DA5308C4F6A84FAB','39','REFRIGERADOR WHIRLPOOL 9 PIES TOP MOUNT CON DISPENSADOR GRIS','WRW25CKTWW','refrigeradora de 9 pies con dispensador ',3297,4290,5400,1,'2023-07-11 16:57:29',1003,1012,207812),('DAB0B3FC4E1048C5','76','REFRIGERADORA MABE 11 PIES TOP MOUNT CON DISPENSADOR SILVER','RMA300FXNU','11 pies con dispensador color Silver',3446,4450,5700,1,'2023-07-11 17:51:19',1003,1008,207812),('DB3EE6615EF74F39','FRDM22F3HPS','REFRIGERADORA FRIGIDAIRE 8 PIES 1 PUERTA CON DISPENSADOR SILVER','FRDM22F3HPS','8 pies una puerta',2088,2950,1720,1,'2023-07-25 17:09:52',1003,1013,207812),('DF8B4D48D1C44DD7','4252132','LICUADORA OSTER 2 VEL. CONTROL DE PERILLA VASO DE VIDRIO BLANCO','BLSTKAG-WRD','UN BOTON 2 VELOCIDADES',385,550,650,1,'2023-07-24 17:07:01',1008,1009,170372),('E0AAC39434F946FE','32','LICUADORA OSTER CROMADA 2 VELOCIDADES VASO DE VIDRIO','46515','vaso de vidrio',695,990,1200,1,'2023-07-08 23:38:01',1008,1009,170372),('E6DF9B2938E14FE7','64','PLANCHA A VAPOR BLACK&DECKER TRUEGLIDE NEGRA','IRBD300','a vapor color negra',140,275,350,1,'2023-07-11 17:36:36',1007,1027,170372),('EA7053AC92284D55','56','TELEVISOR SAMSUNG 43\" SMART LED  HD','UN43AU5300','43 pulgadas led hd',2875,3950,5400,1,'2023-07-11 17:25:13',1001,1001,170372),('ECD8A49F5E15405B','42154','VASO PLASTICO OSTER TRADICIONAL 2 VELOCIDADES','4170V','VASO DE REPUESTO OSTER 2 VELOCIDADES PLASTICO',95,0,0,1,'2023-07-24 16:55:14',1038,1009,170372),('F6E3BD889845464C','446583333','CAMA OLYMPIA EDICIÓN ESPECIAL FUTBOLERA MATRIMONIAL BOX TOP','EEFMATRI1BTS','matrimonial',1272,1920,846,1,'2023-07-25 14:47:03',1014,1018,109822),('F76831DD09144B0B','23','SOPORTE DE PARED MAIESTA PARA TV DE 40\"-80\" FIJO','RACKF40-80','40-80 fijo',65,145,0,1,'2023-07-08 23:26:59',1016,1021,308689),('F9D4185A13204250','90','ALMOHADA DE FIBRA OLYMPIA EXIBHICIÓN','ALMOHADAOLYMPIA',' EXIBHICIÓN EXIBHICIÓN EXIBHICIÓN EXIBHICIÓN',1,999,999,1,'2023-07-11 18:07:33',1027,1018,109822),('F9FFF5A0E64D4983','452158','LICUADORA OSTER 2 VEL. CONTROL DE PULSO VASO DE VIDRIO NEGRO','BLSTKAG-BPB','VASO DE VIDRIO',385,550,650,1,'2023-07-24 17:12:05',1008,1009,170372),('FD9B703AC2DE4EA2','44878835e','MINICOMPONENTE LG Xboom CJ44 5500 WATTS (USB/CD/BT)','LG-CJ44','minicomponente',1698,2150,3200,1,'2023-07-25 15:10:24',1012,1002,190196),('FF909EAE806B49F2','82','TELEVISOR HISENSE 70\" SMART UHD-4K HDR ANDROID TV','70H6500G','70 pulgadas smart uhd 4k con android tv',5016,6190,8400,1,'2023-07-11 17:56:28',1001,1004,207812);
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
INSERT INTO `pv_providers` VALUES (109822,1,'2023-07-08 19:51:22','116da2fb-2ac9-483a-8c6b-2f46b4b4b6e2'),(160039,1,'2023-07-08 19:48:13','b03edfb9-84ae-482c-a600-432cfdad6aa9'),(170372,1,'2023-07-08 19:52:27','dab4a868-dd48-4363-bcaa-14619938406e'),(190196,1,'2023-07-08 19:47:32','64116745-badb-4eda-9a55-246cb34d380b'),(207812,1,'2023-07-08 18:48:00','0f3ab69b-b9ef-45b8-b6d5-2c3b983b2f41'),(308689,1,'2023-07-08 19:52:00','e63803eb-bba1-4191-917a-8320849fbd20'),(342271,1,'2023-07-24 17:22:22','d6169c9d-4f21-46ef-8030-ff6ebbdedc1a'),(367486,1,'2023-07-08 19:50:08','0634147a-a9ee-48d2-a3a5-7c972c6ce94c'),(415958,1,'2023-07-08 19:51:42','04c85492-590c-4861-a392-cc17cb76be9c'),(525311,1,'2023-07-08 19:48:47','00168a7f-444c-4d59-8a9f-bcb3bbc62da8'),(564338,1,'2023-07-08 19:52:50','11984714-7fdd-402c-9e96-ae8e14a563af'),(571770,1,'2023-07-08 19:44:48','36e90fb9-583d-474f-ad85-08f4eacf05ad'),(575180,1,'2023-07-08 19:46:23','837f62ed-560d-464c-ba2a-06ddf76e1c03'),(813063,1,'2023-07-08 19:50:54','54786e44-eb51-4b14-ad95-d54539cd0a0f'),(864663,1,'2023-07-11 17:48:45','34c2315d-b0b3-4be1-862f-1db6168d5880');
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
  `sa_no` int(11) NOT NULL AUTO_INCREMENT,
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
  UNIQUE KEY `sa_no` (`sa_no`),
  KEY `us_id` (`us_id`),
  KEY `lo_id` (`lo_id`),
  KEY `ts_id` (`ts_id`),
  KEY `cu_id` (`cu_id`),
  CONSTRAINT `sa_sales_ibfk_1` FOREIGN KEY (`lo_id`) REFERENCES `lo_locations` (`lo_id`),
  CONSTRAINT `sa_sales_ibfk_2` FOREIGN KEY (`ts_id`) REFERENCES `ts_typessales` (`ts_id`),
  CONSTRAINT `sa_sales_ibfk_3` FOREIGN KEY (`cu_id`) REFERENCES `cu_customers` (`cu_id`),
  CONSTRAINT `sa_sales_ibfk_4` FOREIGN KEY (`us_id`) REFERENCES `us_users` (`us_id`)
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sa_sales`
--

LOCK TABLES `sa_sales` WRITE;
/*!40000 ALTER TABLE `sa_sales` DISABLE KEYS */;
INSERT INTO `sa_sales` VALUES ('0165207b-bc9d-4c95-9a2d-aa2a475b2599',8,2000,0,1,0,1,'2023-07-22 00:49:54',1002,1001,631810,312965),('07742b64-40ff-4033-9439-b9200ddc0752',12,4680,0,12,30,1,'2023-07-24 15:06:00',1001,1002,901390,312965),('0d8a5b58-afaa-4c16-897e-c40d0fd74848',22,481,0,2,30,1,'2023-07-25 14:54:58',1001,1002,177620,312965),('269542ee-f60f-4b29-a57d-11aba8b35989',33,1860,0,5,3,1,'2023-07-25 17:32:51',1001,1002,531314,312965),('2811d801-800e-4226-bfaa-204c38fddec1',25,960,0,3,30,1,'2023-07-25 15:11:22',1001,1002,265789,312965),('2dbe33fe-c9e7-4735-92bd-f64c8167a2b6',21,900,0,3,30,1,'2023-07-25 14:47:49',1001,1002,892956,312965),('36b69578-ca76-42ff-833c-f9b41e5ea23a',26,770,0,2,30,1,'2023-07-25 15:20:36',1001,1002,286336,312965),('3a6d3160-8c5a-4469-b6b1-491a779fc699',34,2200,0,5,2,1,'2023-07-25 17:39:17',1001,1002,946078,312965),('43b159bd-6e07-4283-a2b5-dcb3957eeced',28,1635,0,3,30,1,'2023-07-25 15:54:15',1001,1002,943954,312965),('4bbeb566-68a1-4c73-873b-656ce2b7d525',9,1920,0,3,31,1,'2023-07-22 00:57:59',1001,1002,617322,312965),('4bd5a688-1048-4a72-8bd4-5396315e051e',14,450,0,1,0,1,'2023-07-24 15:33:48',1001,1001,781925,312965),('4c8eddd3-9050-480a-b0ac-7aa92539f4f3',3,5400,0,12,31,1,'2023-07-19 17:50:40',1001,1002,970934,312965),('55449caa-4afd-45ea-816f-7442eb845728',29,1925,0,5,30,1,'2023-07-25 16:42:00',1001,1002,691214,312965),('5f534838-55a2-4b6d-a8eb-9a51958c2657',23,550,0,2,30,1,'2023-07-25 14:59:31',1001,1002,859043,312965),('6088a0be-bf2c-405e-ae56-99649812d371',15,490,0,1,30,1,'2023-07-24 16:30:25',1002,1002,274216,312965),('6634dfee-86fa-4c8c-9da1-621f7fd33dba',10,7050,0,12,30,1,'2023-07-24 14:42:24',1001,1002,828599,312965),('6f019bed-79a2-4f89-b970-08b21c615f3e',20,1035,0,2,30,1,'2023-07-25 14:37:22',1001,1002,567726,312965),('8258f12f-22fa-488c-9ef2-94febbda6486',18,702,0,13,30,0,'2023-07-25 14:26:17',1001,1002,975312,312965),('88614c24-3704-4c5a-b7b3-cbe829b59e6a',13,655,0,1,0,1,'2023-07-24 15:19:22',1001,1001,470829,312965),('8cb23470-4a52-4098-9b15-f78f8b905961',6,650,0,1,0,1,'2023-07-21 00:27:29',1002,1001,154937,181549),('936d3f1b-53ff-456d-9438-d5421fe01692',1,1920,0,2,31,1,'2023-07-18 20:22:50',1001,1002,768580,312965),('9cd60342-014d-47e8-90ee-72eafc08d763',5,650,0,1,0,0,'2023-07-21 00:25:44',1002,1001,NULL,181549),('a81ad9aa-aecd-4298-9afc-e70868676b56',19,702,0,2,30,1,'2023-07-25 14:27:15',1001,1002,975312,312965),('aedaadce-9a1d-4d9e-b6fe-1b757cc80b90',17,4159,3457,10,3,0,'2023-07-25 14:24:16',1001,1002,975312,312965),('becf379c-47b3-4134-b617-8c7c9f11c359',32,1720,0,5,30,1,'2023-07-25 17:21:03',1001,1002,677687,312965),('c7588d5d-e766-45ac-8e18-6774a9d65650',31,1725,0,3,30,1,'2023-07-25 17:01:17',1001,1002,657346,312965),('ccf5897f-6f56-4775-8625-a77ca7c8bf7e',7,2500,0,3,31,1,'2023-07-22 00:38:29',1002,1002,916450,312965),('dd7d5366-d2a7-49da-998c-577d9c818daf',4,5400,0,12,31,1,'2023-07-20 20:45:36',1001,1002,344692,312965),('e8a4b5ee-5480-4781-aeb5-27768cb7896a',30,1545,0,3,30,1,'2023-07-25 16:49:03',1001,1002,691214,312965),('ed5060a9-6e22-4c34-b984-67bca6314d12',11,300,0,1,0,1,'2023-07-24 14:46:42',1001,1001,719522,312965),('f603640e-8562-4339-8721-88c8967d780c',2,650,150,1,0,1,'2023-07-18 22:15:54',1001,1001,820825,312965),('f7ec25fd-8f92-4121-ad3e-8102a14697dd',24,1590,0,3,30,1,'2023-07-25 15:04:51',1001,1002,207710,312965),('faa65e1b-7067-4369-bda4-87db9a605fe7',27,846,0,3,3,1,'2023-07-25 15:31:42',1001,1002,970934,312965),('fac1c7f3-aff8-4530-89dd-6830b7a173ad',16,6820,0,12,30,1,'2023-07-24 18:21:03',1001,1002,317775,312965);
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
) ENGINE=InnoDB AUTO_INCREMENT=1036 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sd_saledetails`
--

LOCK TABLES `sd_saledetails` WRITE;
/*!40000 ALTER TABLE `sd_saledetails` DISABLE KEYS */;
INSERT INTO `sd_saledetails` VALUES (1001,1920,1272,1,'24462CC7CCCB45A2','936d3f1b-53ff-456d-9438-d5421fe01692'),(1002,650,799,1,'ADD6F54D055D43EA','f603640e-8562-4339-8721-88c8967d780c'),(1003,5400,2875,1,'EA7053AC92284D55','4c8eddd3-9050-480a-b0ac-7aa92539f4f3'),(1004,5400,2798,1,'5B381E02A3BE466D','dd7d5366-d2a7-49da-998c-577d9c818daf'),(1005,650,422,1,'C818D1242A9247C6','9cd60342-014d-47e8-90ee-72eafc08d763'),(1006,650,422,1,'C818D1242A9247C6','8cb23470-4a52-4098-9b15-f78f8b905961'),(1007,2500,1570,1,'3AD4D64160CE4028','ccf5897f-6f56-4775-8625-a77ca7c8bf7e'),(1008,2000,1349,1,'0E1BF3CD91F54847','0165207b-bc9d-4c95-9a2d-aa2a475b2599'),(1009,1920,1272,1,'24462CC7CCCB45A2','4bbeb566-68a1-4c73-873b-656ce2b7d525'),(1010,4200,2049,1,'3389135FF94949D6','6634dfee-86fa-4c8c-9da1-621f7fd33dba'),(1011,2850,1272,1,'24462CC7CCCB45A2','6634dfee-86fa-4c8c-9da1-621f7fd33dba'),(1012,300,170,1,'08880B600B0D49AF','ed5060a9-6e22-4c34-b984-67bca6314d12'),(1013,4680,2120,1,'D3CE6985E1FE45DC','07742b64-40ff-4033-9439-b9200ddc0752'),(1014,655,425,1,'C33095A2D20343F4','88614c24-3704-4c5a-b7b3-cbe829b59e6a'),(1015,450,198,1,'184D49A4D8444EAD','4bd5a688-1048-4a72-8bd4-5396315e051e'),(1016,490,364.95,1,'7F0A93011DBD4498','6088a0be-bf2c-405e-ae56-99649812d371'),(1017,6820,3407,1,'643DFC15F36749CB','fac1c7f3-aff8-4530-89dd-6830b7a173ad'),(1018,4159,2088,1,'65C667755CC74BB5','aedaadce-9a1d-4d9e-b6fe-1b757cc80b90'),(1019,702,2088,1,'65C667755CC74BB5','8258f12f-22fa-488c-9ef2-94febbda6486'),(1020,702,2088,1,'65C667755CC74BB5','a81ad9aa-aecd-4298-9afc-e70868676b56'),(1021,1035,3291,1,'D1484955A26C4B8D','6f019bed-79a2-4f89-b970-08b21c615f3e'),(1022,900,1272,1,'F6E3BD889845464C','2dbe33fe-c9e7-4735-92bd-f64c8167a2b6'),(1023,481,1272,1,'F6E3BD889845464C','0d8a5b58-afaa-4c16-897e-c40d0fd74848'),(1024,550,1272,1,'F6E3BD889845464C','5f534838-55a2-4b6d-a8eb-9a51958c2657'),(1025,1590,3289,1,'52F44C4F3E9043CD','f7ec25fd-8f92-4121-ad3e-8102a14697dd'),(1026,960,1698,1,'FD9B703AC2DE4EA2','2811d801-800e-4226-bfaa-204c38fddec1'),(1027,770,2072,1,'A5275D06C19C48D4','36b69578-ca76-42ff-833c-f9b41e5ea23a'),(1028,846,1272,1,'F6E3BD889845464C','faa65e1b-7067-4369-bda4-87db9a605fe7'),(1029,1635,3113,1,'D66EF280B6C648A1','43b159bd-6e07-4283-a2b5-dcb3957eeced'),(1030,1925,2715,1,'AB68731198214EDA','55449caa-4afd-45ea-816f-7442eb845728'),(1031,1545,3500,1,'3DBF3CAD8E6F4633','e8a4b5ee-5480-4781-aeb5-27768cb7896a'),(1032,1725,3587,1,'1C93512DFE5A49FE','c7588d5d-e766-45ac-8e18-6774a9d65650'),(1033,1720,2088,1,'DB3EE6615EF74F39','becf379c-47b3-4134-b617-8c7c9f11c359'),(1034,930,982,2,'8C1E18D106AC43C9','269542ee-f60f-4b29-a57d-11aba8b35989'),(1035,2200,2936,1,'5CCCD6DABA16412E','3a6d3160-8c5a-4469-b6b1-491a779fc699');
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
INSERT INTO `sess_usersessions` VALUES ('182deaf4-e4a3-4485-aed0-749d073e5f92',0,1,'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36','2023-07-24 23:01:31',263899),('354836aa-8456-472b-ba84-69f667cb10c7',0,1,'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36','2023-07-11 17:42:35',206506),('bd2f9efb-cc92-4c22-bbd4-566df65c34bb',0,1,'Mozilla/5.0 (iPhone; CPU iPhone OS 16_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5.2 Mobile/15E148 Safari/604.1','2023-07-21 04:37:52',263899),('dae26fe5-ec47-4595-818e-e3126b158885',0,1,'Mozilla/5.0 (iPhone; CPU iPhone OS 16_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5.1 Mobile/15E148 Safari/604.1','2023-07-12 15:19:06',263899),('e5f1853a-8da3-4bbb-af85-9155fd0ae567',0,1,'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36','2023-07-24 18:12:17',206506),('f52bfe3d-3af2-4854-95ca-3c022373c070',1,1,'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36','2023-07-26 01:22:22',206506);
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
) ENGINE=InnoDB AUTO_INCREMENT=1151 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sp_salepayments`
--

LOCK TABLES `sp_salepayments` WRITE;
/*!40000 ALTER TABLE `sp_salepayments` DISABLE KEYS */;
INSERT INTO `sp_salepayments` VALUES (1001,1000001,1000,0,1000,'2023-07-18','2023-07-18 20:22:50',1001,312965,'936d3f1b-53ff-456d-9438-d5421fe01692'),(1002,NULL,920,0,0,'2023-08-18',NULL,NULL,NULL,'936d3f1b-53ff-456d-9438-d5421fe01692'),(1003,1000002,500,0,500,'2023-07-18','2023-07-18 22:15:54',1001,312965,'f603640e-8562-4339-8721-88c8967d780c'),(1004,1000003,450,0,450,'2023-07-19','2023-07-19 17:50:40',1001,312965,'4c8eddd3-9050-480a-b0ac-7aa92539f4f3'),(1005,NULL,450,0,0,'2023-08-20',NULL,NULL,NULL,'4c8eddd3-9050-480a-b0ac-7aa92539f4f3'),(1006,NULL,450,0,0,'2023-09-20',NULL,NULL,NULL,'4c8eddd3-9050-480a-b0ac-7aa92539f4f3'),(1007,NULL,450,0,0,'2023-10-20',NULL,NULL,NULL,'4c8eddd3-9050-480a-b0ac-7aa92539f4f3'),(1008,NULL,450,0,0,'2023-11-20',NULL,NULL,NULL,'4c8eddd3-9050-480a-b0ac-7aa92539f4f3'),(1009,NULL,450,0,0,'2023-12-20',NULL,NULL,NULL,'4c8eddd3-9050-480a-b0ac-7aa92539f4f3'),(1010,NULL,450,0,0,'2024-01-20',NULL,NULL,NULL,'4c8eddd3-9050-480a-b0ac-7aa92539f4f3'),(1011,NULL,450,0,0,'2024-02-20',NULL,NULL,NULL,'4c8eddd3-9050-480a-b0ac-7aa92539f4f3'),(1012,NULL,450,0,0,'2024-03-20',NULL,NULL,NULL,'4c8eddd3-9050-480a-b0ac-7aa92539f4f3'),(1013,NULL,450,0,0,'2024-04-20',NULL,NULL,NULL,'4c8eddd3-9050-480a-b0ac-7aa92539f4f3'),(1014,NULL,450,0,0,'2024-05-20',NULL,NULL,NULL,'4c8eddd3-9050-480a-b0ac-7aa92539f4f3'),(1015,NULL,450,0,0,'2024-06-20',NULL,NULL,NULL,'4c8eddd3-9050-480a-b0ac-7aa92539f4f3'),(1016,1000004,450,0,450,'2023-07-20','2023-07-20 20:45:36',1001,312965,'dd7d5366-d2a7-49da-998c-577d9c818daf'),(1017,NULL,450,0,0,'2023-08-20',NULL,NULL,NULL,'dd7d5366-d2a7-49da-998c-577d9c818daf'),(1018,NULL,450,0,0,'2023-09-20',NULL,NULL,NULL,'dd7d5366-d2a7-49da-998c-577d9c818daf'),(1019,NULL,450,0,0,'2023-10-21',NULL,NULL,NULL,'dd7d5366-d2a7-49da-998c-577d9c818daf'),(1020,NULL,450,0,0,'2023-11-21',NULL,NULL,NULL,'dd7d5366-d2a7-49da-998c-577d9c818daf'),(1021,NULL,450,0,0,'2023-12-22',NULL,NULL,NULL,'dd7d5366-d2a7-49da-998c-577d9c818daf'),(1022,NULL,450,0,0,'2024-01-22',NULL,NULL,NULL,'dd7d5366-d2a7-49da-998c-577d9c818daf'),(1023,NULL,450,0,0,'2024-02-22',NULL,NULL,NULL,'dd7d5366-d2a7-49da-998c-577d9c818daf'),(1024,NULL,450,0,0,'2024-03-24',NULL,NULL,NULL,'dd7d5366-d2a7-49da-998c-577d9c818daf'),(1025,NULL,450,0,0,'2024-04-24',NULL,NULL,NULL,'dd7d5366-d2a7-49da-998c-577d9c818daf'),(1026,NULL,450,0,0,'2024-05-25',NULL,NULL,NULL,'dd7d5366-d2a7-49da-998c-577d9c818daf'),(1027,NULL,450,0,0,'2024-06-25',NULL,NULL,NULL,'dd7d5366-d2a7-49da-998c-577d9c818daf'),(1028,1000005,650,0,650,'2023-07-21','2023-07-21 00:25:44',1001,181549,'9cd60342-014d-47e8-90ee-72eafc08d763'),(1029,1000006,650,0,650,'2023-07-21','2023-07-21 00:27:29',1001,181549,'8cb23470-4a52-4098-9b15-f78f8b905961'),(1030,1000007,1000,0,1000,'2023-07-22','2023-07-22 00:38:29',1001,312965,'ccf5897f-6f56-4775-8625-a77ca7c8bf7e'),(1031,NULL,750,0,0,'2023-08-22',NULL,NULL,NULL,'ccf5897f-6f56-4775-8625-a77ca7c8bf7e'),(1032,NULL,750,0,0,'2023-09-07',NULL,NULL,NULL,'ccf5897f-6f56-4775-8625-a77ca7c8bf7e'),(1033,1000008,2000,0,2000,'2023-07-22','2023-07-22 00:49:54',1001,312965,'0165207b-bc9d-4c95-9a2d-aa2a475b2599'),(1034,1000009,1000,0,1000,'2023-07-22','2023-07-22 00:57:59',1001,312965,'4bbeb566-68a1-4c73-873b-656ce2b7d525'),(1035,NULL,460,0,0,'2023-08-22',NULL,NULL,NULL,'4bbeb566-68a1-4c73-873b-656ce2b7d525'),(1036,NULL,460,0,0,'2023-09-05',NULL,NULL,NULL,'4bbeb566-68a1-4c73-873b-656ce2b7d525'),(1037,1000010,635,0,635,'2023-07-24','2023-07-24 14:42:24',1001,312965,'6634dfee-86fa-4c8c-9da1-621f7fd33dba'),(1038,NULL,583,0,0,'2023-08-23',NULL,NULL,NULL,'6634dfee-86fa-4c8c-9da1-621f7fd33dba'),(1039,NULL,583,0,0,'2023-09-22',NULL,NULL,NULL,'6634dfee-86fa-4c8c-9da1-621f7fd33dba'),(1040,NULL,583,0,0,'2023-10-22',NULL,NULL,NULL,'6634dfee-86fa-4c8c-9da1-621f7fd33dba'),(1041,NULL,583,0,0,'2023-11-21',NULL,NULL,NULL,'6634dfee-86fa-4c8c-9da1-621f7fd33dba'),(1042,NULL,583,0,0,'2023-12-21',NULL,NULL,NULL,'6634dfee-86fa-4c8c-9da1-621f7fd33dba'),(1043,NULL,583,0,0,'2024-01-20',NULL,NULL,NULL,'6634dfee-86fa-4c8c-9da1-621f7fd33dba'),(1044,NULL,583,0,0,'2024-02-19',NULL,NULL,NULL,'6634dfee-86fa-4c8c-9da1-621f7fd33dba'),(1045,NULL,583,0,0,'2024-03-20',NULL,NULL,NULL,'6634dfee-86fa-4c8c-9da1-621f7fd33dba'),(1046,NULL,583,0,0,'2024-04-19',NULL,NULL,NULL,'6634dfee-86fa-4c8c-9da1-621f7fd33dba'),(1047,NULL,583,0,0,'2024-05-19',NULL,NULL,NULL,'6634dfee-86fa-4c8c-9da1-621f7fd33dba'),(1048,NULL,585,0,0,'2024-06-18',NULL,NULL,NULL,'6634dfee-86fa-4c8c-9da1-621f7fd33dba'),(1049,1000011,300,0,300,'2023-07-24','2023-07-24 14:46:42',1001,312965,'ed5060a9-6e22-4c34-b984-67bca6314d12'),(1050,1000012,390,0,390,'2023-07-24','2023-07-24 15:06:00',1001,312965,'07742b64-40ff-4033-9439-b9200ddc0752'),(1051,NULL,390,0,0,'2023-08-24',NULL,NULL,NULL,'07742b64-40ff-4033-9439-b9200ddc0752'),(1052,NULL,390,0,0,'2023-09-24',NULL,NULL,NULL,'07742b64-40ff-4033-9439-b9200ddc0752'),(1053,NULL,390,0,0,'2023-10-24',NULL,NULL,NULL,'07742b64-40ff-4033-9439-b9200ddc0752'),(1054,NULL,390,0,0,'2023-11-24',NULL,NULL,NULL,'07742b64-40ff-4033-9439-b9200ddc0752'),(1055,NULL,390,0,0,'2023-12-24',NULL,NULL,NULL,'07742b64-40ff-4033-9439-b9200ddc0752'),(1056,NULL,390,0,0,'2024-01-24',NULL,NULL,NULL,'07742b64-40ff-4033-9439-b9200ddc0752'),(1057,NULL,390,0,0,'2024-02-24',NULL,NULL,NULL,'07742b64-40ff-4033-9439-b9200ddc0752'),(1058,NULL,390,0,0,'2024-03-24',NULL,NULL,NULL,'07742b64-40ff-4033-9439-b9200ddc0752'),(1059,NULL,390,0,0,'2024-04-24',NULL,NULL,NULL,'07742b64-40ff-4033-9439-b9200ddc0752'),(1060,NULL,390,0,0,'2024-05-24',NULL,NULL,NULL,'07742b64-40ff-4033-9439-b9200ddc0752'),(1061,NULL,390,0,0,'2024-06-24',NULL,NULL,NULL,'07742b64-40ff-4033-9439-b9200ddc0752'),(1062,1000013,655,0,655,'2023-07-24','2023-07-24 15:19:22',1001,312965,'88614c24-3704-4c5a-b7b3-cbe829b59e6a'),(1063,1000014,450,0,450,'2023-07-24','2023-07-24 15:33:48',1001,312965,'4bd5a688-1048-4a72-8bd4-5396315e051e'),(1064,NULL,490,0,0,'2023-08-05',NULL,NULL,NULL,'6088a0be-bf2c-405e-ae56-99649812d371'),(1065,NULL,568,0,0,'2023-07-30',NULL,NULL,NULL,'fac1c7f3-aff8-4530-89dd-6830b7a173ad'),(1066,NULL,568,0,0,'2023-08-30',NULL,NULL,NULL,'fac1c7f3-aff8-4530-89dd-6830b7a173ad'),(1067,NULL,568,0,0,'2023-09-30',NULL,NULL,NULL,'fac1c7f3-aff8-4530-89dd-6830b7a173ad'),(1068,NULL,568,0,0,'2023-10-30',NULL,NULL,NULL,'fac1c7f3-aff8-4530-89dd-6830b7a173ad'),(1069,NULL,568,0,0,'2023-11-30',NULL,NULL,NULL,'fac1c7f3-aff8-4530-89dd-6830b7a173ad'),(1070,NULL,568,0,0,'2023-12-30',NULL,NULL,NULL,'fac1c7f3-aff8-4530-89dd-6830b7a173ad'),(1071,NULL,568,0,0,'2024-01-30',NULL,NULL,NULL,'fac1c7f3-aff8-4530-89dd-6830b7a173ad'),(1072,NULL,568,0,0,'2024-02-29',NULL,NULL,NULL,'fac1c7f3-aff8-4530-89dd-6830b7a173ad'),(1073,NULL,568,0,0,'2024-03-30',NULL,NULL,NULL,'fac1c7f3-aff8-4530-89dd-6830b7a173ad'),(1074,NULL,568,0,0,'2024-04-30',NULL,NULL,NULL,'fac1c7f3-aff8-4530-89dd-6830b7a173ad'),(1075,NULL,568,0,0,'2024-05-30',NULL,NULL,NULL,'fac1c7f3-aff8-4530-89dd-6830b7a173ad'),(1076,NULL,572,0,0,'2024-06-30',NULL,NULL,NULL,'fac1c7f3-aff8-4530-89dd-6830b7a173ad'),(1077,1000015,1000,0,1000,'2023-07-25','2023-07-25 14:24:16',1001,312965,'aedaadce-9a1d-4d9e-b6fe-1b757cc80b90'),(1078,NULL,-34,0,0,'2023-07-28',NULL,NULL,NULL,'aedaadce-9a1d-4d9e-b6fe-1b757cc80b90'),(1079,NULL,-34,0,0,'2023-07-31',NULL,NULL,NULL,'aedaadce-9a1d-4d9e-b6fe-1b757cc80b90'),(1080,NULL,-34,0,0,'2023-08-03',NULL,NULL,NULL,'aedaadce-9a1d-4d9e-b6fe-1b757cc80b90'),(1081,NULL,-34,0,0,'2023-08-06',NULL,NULL,NULL,'aedaadce-9a1d-4d9e-b6fe-1b757cc80b90'),(1082,NULL,-34,0,0,'2023-08-09',NULL,NULL,NULL,'aedaadce-9a1d-4d9e-b6fe-1b757cc80b90'),(1083,NULL,-34,0,0,'2023-08-12',NULL,NULL,NULL,'aedaadce-9a1d-4d9e-b6fe-1b757cc80b90'),(1084,NULL,-34,0,0,'2023-08-15',NULL,NULL,NULL,'aedaadce-9a1d-4d9e-b6fe-1b757cc80b90'),(1085,NULL,-34,0,0,'2023-08-18',NULL,NULL,NULL,'aedaadce-9a1d-4d9e-b6fe-1b757cc80b90'),(1086,NULL,-26.0024,0,0,'2023-08-21',NULL,NULL,NULL,'aedaadce-9a1d-4d9e-b6fe-1b757cc80b90'),(1087,NULL,54,0,0,'2023-08-24',NULL,NULL,NULL,'8258f12f-22fa-488c-9ef2-94febbda6486'),(1088,NULL,54,0,0,'2023-09-23',NULL,NULL,NULL,'8258f12f-22fa-488c-9ef2-94febbda6486'),(1089,NULL,54,0,0,'2023-10-23',NULL,NULL,NULL,'8258f12f-22fa-488c-9ef2-94febbda6486'),(1090,NULL,54,0,0,'2023-11-22',NULL,NULL,NULL,'8258f12f-22fa-488c-9ef2-94febbda6486'),(1091,NULL,54,0,0,'2023-12-22',NULL,NULL,NULL,'8258f12f-22fa-488c-9ef2-94febbda6486'),(1092,NULL,54,0,0,'2024-01-21',NULL,NULL,NULL,'8258f12f-22fa-488c-9ef2-94febbda6486'),(1093,NULL,54,0,0,'2024-02-20',NULL,NULL,NULL,'8258f12f-22fa-488c-9ef2-94febbda6486'),(1094,NULL,54,0,0,'2024-03-21',NULL,NULL,NULL,'8258f12f-22fa-488c-9ef2-94febbda6486'),(1095,NULL,54,0,0,'2024-04-20',NULL,NULL,NULL,'8258f12f-22fa-488c-9ef2-94febbda6486'),(1096,NULL,54,0,0,'2024-05-20',NULL,NULL,NULL,'8258f12f-22fa-488c-9ef2-94febbda6486'),(1097,NULL,54,0,0,'2024-06-19',NULL,NULL,NULL,'8258f12f-22fa-488c-9ef2-94febbda6486'),(1098,NULL,54,0,0,'2024-07-19',NULL,NULL,NULL,'8258f12f-22fa-488c-9ef2-94febbda6486'),(1099,NULL,54,0,0,'2024-08-18',NULL,NULL,NULL,'8258f12f-22fa-488c-9ef2-94febbda6486'),(1100,NULL,351,0,0,'2023-08-05',NULL,NULL,NULL,'a81ad9aa-aecd-4298-9afc-e70868676b56'),(1101,NULL,351,0,0,'2023-09-05',NULL,NULL,NULL,'a81ad9aa-aecd-4298-9afc-e70868676b56'),(1102,NULL,517,0,0,'2023-08-15',NULL,NULL,NULL,'6f019bed-79a2-4f89-b970-08b21c615f3e'),(1103,NULL,518,0,0,'2023-09-15',NULL,NULL,NULL,'6f019bed-79a2-4f89-b970-08b21c615f3e'),(1104,NULL,300,0,0,'2023-07-15',NULL,NULL,NULL,'2dbe33fe-c9e7-4735-92bd-f64c8167a2b6'),(1105,NULL,300,0,0,'2023-08-15',NULL,NULL,NULL,'2dbe33fe-c9e7-4735-92bd-f64c8167a2b6'),(1106,NULL,300,0,0,'2023-09-15',NULL,NULL,NULL,'2dbe33fe-c9e7-4735-92bd-f64c8167a2b6'),(1107,NULL,240,0,0,'2023-08-16',NULL,NULL,NULL,'0d8a5b58-afaa-4c16-897e-c40d0fd74848'),(1108,NULL,241,0,0,'2023-09-16',NULL,NULL,NULL,'0d8a5b58-afaa-4c16-897e-c40d0fd74848'),(1109,NULL,275,0,0,'2023-08-16',NULL,NULL,NULL,'5f534838-55a2-4b6d-a8eb-9a51958c2657'),(1110,NULL,275,0,0,'2023-09-16',NULL,NULL,NULL,'5f534838-55a2-4b6d-a8eb-9a51958c2657'),(1111,NULL,530,0,0,'2023-07-31',NULL,NULL,NULL,'f7ec25fd-8f92-4121-ad3e-8102a14697dd'),(1112,NULL,530,0,0,'2023-08-15',NULL,NULL,NULL,'f7ec25fd-8f92-4121-ad3e-8102a14697dd'),(1113,NULL,530,0,0,'2023-09-15',NULL,NULL,NULL,'f7ec25fd-8f92-4121-ad3e-8102a14697dd'),(1114,NULL,320,0,0,'2023-07-16',NULL,NULL,NULL,'2811d801-800e-4226-bfaa-204c38fddec1'),(1115,NULL,320,0,0,'2023-08-16',NULL,NULL,NULL,'2811d801-800e-4226-bfaa-204c38fddec1'),(1116,NULL,320,0,0,'2023-09-16',NULL,NULL,NULL,'2811d801-800e-4226-bfaa-204c38fddec1'),(1117,NULL,385,0,0,'2023-08-17',NULL,NULL,NULL,'36b69578-ca76-42ff-833c-f9b41e5ea23a'),(1118,NULL,385,0,0,'2023-09-17',NULL,NULL,NULL,'36b69578-ca76-42ff-833c-f9b41e5ea23a'),(1119,NULL,282,0,0,'2023-07-20',NULL,NULL,NULL,'faa65e1b-7067-4369-bda4-87db9a605fe7'),(1120,NULL,282,0,0,'2023-09-20',NULL,NULL,NULL,'faa65e1b-7067-4369-bda4-87db9a605fe7'),(1121,NULL,282,0,0,'2023-08-20',NULL,NULL,NULL,'faa65e1b-7067-4369-bda4-87db9a605fe7'),(1122,NULL,545,0,0,'2023-07-31',NULL,NULL,NULL,'43b159bd-6e07-4283-a2b5-dcb3957eeced'),(1123,NULL,545,0,0,'2023-08-31',NULL,NULL,NULL,'43b159bd-6e07-4283-a2b5-dcb3957eeced'),(1124,NULL,545,0,0,'2023-09-30',NULL,NULL,NULL,'43b159bd-6e07-4283-a2b5-dcb3957eeced'),(1125,NULL,385,0,0,'2023-07-21',NULL,NULL,NULL,'55449caa-4afd-45ea-816f-7442eb845728'),(1126,NULL,385,0,0,'2023-08-21',NULL,NULL,NULL,'55449caa-4afd-45ea-816f-7442eb845728'),(1127,NULL,385,0,0,'2023-09-21',NULL,NULL,NULL,'55449caa-4afd-45ea-816f-7442eb845728'),(1128,NULL,385,0,0,'2023-10-21',NULL,NULL,NULL,'55449caa-4afd-45ea-816f-7442eb845728'),(1129,NULL,385,0,0,'2023-11-21',NULL,NULL,NULL,'55449caa-4afd-45ea-816f-7442eb845728'),(1130,NULL,515,0,0,'2023-07-21',NULL,NULL,NULL,'e8a4b5ee-5480-4781-aeb5-27768cb7896a'),(1131,NULL,515,0,0,'2023-08-21',NULL,NULL,NULL,'e8a4b5ee-5480-4781-aeb5-27768cb7896a'),(1132,NULL,515,0,0,'2023-09-21',NULL,NULL,NULL,'e8a4b5ee-5480-4781-aeb5-27768cb7896a'),(1133,NULL,575,0,0,'2023-07-30',NULL,NULL,NULL,'c7588d5d-e766-45ac-8e18-6774a9d65650'),(1134,NULL,575,0,0,'2023-08-30',NULL,NULL,NULL,'c7588d5d-e766-45ac-8e18-6774a9d65650'),(1135,NULL,575,0,0,'2023-09-30',NULL,NULL,NULL,'c7588d5d-e766-45ac-8e18-6774a9d65650'),(1136,NULL,344,0,0,'2023-07-30',NULL,NULL,NULL,'becf379c-47b3-4134-b617-8c7c9f11c359'),(1137,NULL,344,0,0,'2023-08-30',NULL,NULL,NULL,'becf379c-47b3-4134-b617-8c7c9f11c359'),(1138,NULL,344,0,0,'2023-09-30',NULL,NULL,NULL,'becf379c-47b3-4134-b617-8c7c9f11c359'),(1139,NULL,344,0,0,'2023-10-30',NULL,NULL,NULL,'becf379c-47b3-4134-b617-8c7c9f11c359'),(1140,NULL,344,0,0,'2023-11-30',NULL,NULL,NULL,'becf379c-47b3-4134-b617-8c7c9f11c359'),(1141,NULL,372,0,0,'2023-05-30',NULL,NULL,NULL,'269542ee-f60f-4b29-a57d-11aba8b35989'),(1142,NULL,372,0,0,'2023-06-30',NULL,NULL,NULL,'269542ee-f60f-4b29-a57d-11aba8b35989'),(1143,NULL,372,0,0,'2023-07-30',NULL,NULL,NULL,'269542ee-f60f-4b29-a57d-11aba8b35989'),(1144,NULL,372,0,0,'2023-09-30',NULL,NULL,NULL,'269542ee-f60f-4b29-a57d-11aba8b35989'),(1145,NULL,372,0,0,'2023-08-09',NULL,NULL,NULL,'269542ee-f60f-4b29-a57d-11aba8b35989'),(1146,NULL,440,0,0,'2023-07-27',NULL,NULL,NULL,'3a6d3160-8c5a-4469-b6b1-491a779fc699'),(1147,NULL,440,0,0,'2023-08-27',NULL,NULL,NULL,'3a6d3160-8c5a-4469-b6b1-491a779fc699'),(1148,NULL,440,0,0,'2023-09-27',NULL,NULL,NULL,'3a6d3160-8c5a-4469-b6b1-491a779fc699'),(1149,NULL,440,0,0,'2023-10-27',NULL,NULL,NULL,'3a6d3160-8c5a-4469-b6b1-491a779fc699'),(1150,NULL,440,0,0,'2023-11-27',NULL,NULL,NULL,'3a6d3160-8c5a-4469-b6b1-491a779fc699');
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
) ENGINE=InnoDB AUTO_INCREMENT=1005 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `st_states`
--

LOCK TABLES `st_states` WRITE;
/*!40000 ALTER TABLE `st_states` DISABLE KEYS */;
INSERT INTO `st_states` VALUES (1001,'Guatemala',1),(1002,'',0),(1003,'Sacatepequez',1),(1004,'Escuintla',1);
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
INSERT INTO `ts_typessales` VALUES (1001,'De contado'),(1002,'Credito'),(1003,'Fuera de tienda');
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
INSERT INTO `us_users` VALUES (181549,'$2b$12$OpB5dQXT2dBErSIPlg3AJuUzvdrFSqtdMUws426Pb/h6I17vs9qLy','[\'/pos/statistics\', \'/pos/manage/customers\', \'/pos/manage/products\', \'/pos/manage/providers\', \'/pos/manage/categories\', \'/pos/manage/brands\', \'/pos/manage/sales\', \'/pos/manage/addresses\', \'/pos/manage/sale/payments\', \'/pos/manage/sale/payments/edit\']',1,'2023-06-25 23:59:54','f98ff4d9-a90c-44a2-9a11-2c3b492dc510',111529),(206506,'$2b$12$c5QpRpxLh/OYZNM9M5KCQecnCpsKqs45WK1QHJscUN6MFpF45dsnC','[\'/pos/statistics\', \'/pos/manage/users\', \'/pos/manage/customers\', \'/pos/manage/paymentmethods\', \'/pos/manage/locations\', \'/pos/manage/products\', \'/pos/manage/providers\', \'/pos/manage/categories\', \'/pos/manage/brands\', \'/pos/manage/cities\', \'/pos/manage/states\', \'/pos/manage/sales\', \'/pos/manage/dbbackup\', \'/pos/manage/addresses\', \'/pos/manage/sale/payments\', \'/pos/manage/sale/payments/edit\']',1,'2023-06-21 13:15:07','86302e2b-809c-490c-819a-367f88f4af67',111529),(263899,'$2b$12$PluQojW52KsQOmZe/.F8f.f7sbJcbM9AYlOyqA1hlLptSoGqA9LaO','[\'/pos/statistics\', \'/pos/manage/users\', \'/pos/manage/customers\', \'/pos/manage/paymentmethods\', \'/pos/manage/locations\', \'/pos/manage/products\', \'/pos/manage/providers\', \'/pos/manage/categories\', \'/pos/manage/brands\', \'/pos/manage/cities\', \'/pos/manage/states\', \'/pos/manage/sales\', \'/pos/manage/dbbackup\', \'/pos/manage/addresses\', \'/pos/manage/sale/payments\', \'/pos/manage/sale/payments/edit\']',1,'2023-06-23 11:32:06','ea01b71f-51df-4e9a-a402-018e399e611b',111529),(312965,'$2b$12$IpfJ36L4QPu3lbjGTpx.e.9Zc8w3wuF6grG1jNA0eJF/HxEhiQEO.','[\'/pos/statistics\', \'/pos/manage/customers\', \'/pos/manage/products\', \'/pos/manage/providers\', \'/pos/manage/categories\', \'/pos/manage/brands\', \'/pos/manage/sales\', \'/pos/manage/addresses\', \'/pos/manage/sale/payments\', \'/pos/manage/sale/payments/edit\']',1,'2023-07-18 20:18:13','3b2bdf70-3f6c-4930-a526-7f4a6d681ae2',111529),(791950,'$2b$12$KIzwtHxeY.h97KqM1xcmVeKiDa5ZOe.dCDQ89zG9FVymEJnJfSKVa','[\'/pos/manage/customers\', \'/pos/manage/sales\', \'/pos/manage/addresses\', \'/pos/manage/sale/payments\']',1,'2023-06-25 23:58:58','c70dd5a9-f7a8-4964-a0c5-f6310bc1dddd',111529);
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

-- Dump completed on 2023-07-26  1:22:26
