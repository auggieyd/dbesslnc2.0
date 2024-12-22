/*
 Source Server         : wsl
 Source Server Type    : MySQL
 Source Server Version : 80040
 Source Host           : localhost:3307
 Source Schema         : dbess

 Target Server Type    : MySQL
 Target Server Version : 80040
 File Encoding         : 65001

 Date: 18/12/2024 15:19:22
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for disease_related
-- ----------------------------
DROP TABLE IF EXISTS `disease_related`;
CREATE TABLE `disease_related`  (
  `Noncode_id` text CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL,
  `Lncbook_id` text CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL,
  `likely_or_pathogenic_count` text CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL,
  `chr` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `start` int NOT NULL,
  `end` int NOT NULL,
  `strand` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `num_id` int NOT NULL AUTO_INCREMENT,
  `NCBI_id` text CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL,
  `gene_name` text CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL,
  `UID` text CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `disease_related` int NULL DEFAULT 1,
  PRIMARY KEY (`num_id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 33004 CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Table structure for esslnc
-- ----------------------------
DROP TABLE IF EXISTS `esslnc`;
CREATE TABLE `esslnc`  (
  `Noncode_id` text CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL,
  `Lncbook_id` text CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL,
  `UID` text CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL COMMENT '主键',
  `lib_id` text CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL,
  `gene_name` text CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL,
  `ensembl_id` text CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL,
  `num_id` int NOT NULL AUTO_INCREMENT,
  `PMID` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `NCBI_id` text CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL,
  `reason` text CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL,
  `Organism` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `Go_annotation` text CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL,
  `Alias` text CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL,
  `description` text CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL,
  `chr` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `start` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `end` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `strand` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `cancer_related` int UNSIGNED NULL DEFAULT 0,
  `disease_related` int UNSIGNED NULL DEFAULT 0,
  `vivo` int NULL DEFAULT 0,
  `vitro` int NULL DEFAULT 0,
  PRIMARY KEY (`num_id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 6379 CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Table structure for exp_crispr
-- ----------------------------
DROP TABLE IF EXISTS `exp_crispr`;
CREATE TABLE `exp_crispr`  (
  `num_id` int NOT NULL AUTO_INCREMENT,
  `exp_type` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `exp_score` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `cell_line` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `role` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `is_ess` int NULL DEFAULT NULL,
  `target_id` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `UID` text CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL,
  `PMID` text CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL,
  PRIMARY KEY (`num_id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1444 CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Table structure for exp_profile
-- ----------------------------
DROP TABLE IF EXISTS `exp_profile`;
CREATE TABLE `exp_profile`  (
  `Organism` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `Lncbook_trans_id` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `UID` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `transcript_id` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `brain` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `lung` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `urinarybladder` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `kidney` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `adrenal` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `thyroid` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `heart` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `lymphnode` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `spleen` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `bonemarrow` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `tonsil` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `appendix` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `colon` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `esophagus` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `gallbladder` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `smallintestine` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `salivarygland` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `stomach` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `liver` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `duodenum` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `pancreas` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `rectum` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `endometrium` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `ovary` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `testis` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `prostate` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `fallopiantube` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `skeletalmuscle` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `smoothmuscle` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `skin` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `fat` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `num_id` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`num_id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 23781 CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Table structure for expression
-- ----------------------------
DROP TABLE IF EXISTS `expression`;
CREATE TABLE `expression`  (
  `UID` text CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL,
  `organism` text CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL,
  `transcript_id` text CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL,
  `adipose` double NULL DEFAULT NULL,
  `adrenal` double NULL DEFAULT NULL,
  `brain` double NULL DEFAULT NULL,
  `brain_R` double NULL DEFAULT NULL,
  `breast` double NULL DEFAULT NULL,
  `colon` double NULL DEFAULT NULL,
  `fId` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`fId`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2687 CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Table structure for lncrna_variant_mapping
-- ----------------------------
DROP TABLE IF EXISTS `lncrna_variant_mapping`;
CREATE TABLE `lncrna_variant_mapping`  (
  `variation_id` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `UID` text CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL
) ENGINE = InnoDB CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Table structure for trans
-- ----------------------------
DROP TABLE IF EXISTS `trans`;
CREATE TABLE `trans`  (
  `NONCODE_Gene_ID` text CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL,
  `NONCODE_TRANSCRIPT_ID` text CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL,
  `length` int NULL DEFAULT NULL,
  `Name` text CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL,
  `Organism` text CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL,
  `FASTA` mediumtext CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL,
  `id` int NOT NULL AUTO_INCREMENT,
  `Lncbook_id` text CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL,
  `Lncbook_trans_id` text CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL,
  `UID` text CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL,
  `transcript_id` text CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL,
  `chr` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `start` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `end` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `strand` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `exon_num` int NULL DEFAULT NULL,
  `exon_pos` text CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 34853 CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Table structure for variants
-- ----------------------------
DROP TABLE IF EXISTS `variants`;
CREATE TABLE `variants`  (
  `chr` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `variant_start` int NULL DEFAULT NULL,
  `variant_end` int NULL DEFAULT NULL,
  `variant_type` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `clinical_significance` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `variation_id` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `reference_allele` text CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL,
  `alternate_allele` text CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL,
  `phenotype` text CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL,
  PRIMARY KEY (`variation_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = DYNAMIC;

SET FOREIGN_KEY_CHECKS = 1;
