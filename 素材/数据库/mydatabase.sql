/*
Navicat MySQL Data Transfer

Source Server         : MySQL
Source Server Version : 50520
Source Host           : localhost:3306
Source Database       : mydatabase

Target Server Type    : MYSQL
Target Server Version : 50520
File Encoding         : 65001

Date: 2019-04-10 14:31:06
*/

SET FOREIGN_KEY_CHECKS=0;
-- ----------------------------
-- Table structure for `student`
-- ----------------------------
DROP TABLE IF EXISTS `student`;
CREATE TABLE `student` (
  `number` varchar(20) NOT NULL,
  `name` varchar(50) NOT NULL,
  `sex` varchar(2) DEFAULT NULL,
  `math` double(4,1) DEFAULT NULL,
  `english` double(4,1) DEFAULT NULL,
  `computer` double(4,1) DEFAULT NULL,
  PRIMARY KEY (`number`)
) ENGINE=InnoDB DEFAULT CHARSET=gbk;

-- ----------------------------
-- Records of student
-- ----------------------------
INSERT INTO student VALUES ('1502', '方花花', 'F', '76.5', '80.0', '80.0');
INSERT INTO student VALUES ('1507', '李要', 'M', '95.0', '60.0', '83.0');
INSERT INTO student VALUES ('1508', '王段', 'M', '92.0', '75.0', '81.0');
INSERT INTO student VALUES ('1512', '刘晓晓', 'F', '77.0', '85.0', '82.0');
INSERT INTO student VALUES ('1514', '蔡阳光', 'M', '99.0', '100.0', '67.0');
INSERT INTO student VALUES ('1520', '黄一一', 'M', '69.0', '90.0', '100.0');
