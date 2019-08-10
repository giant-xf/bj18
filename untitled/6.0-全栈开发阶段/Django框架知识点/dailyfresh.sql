/*
Navicat MySQL Data Transfer

Source Server         : ubuntu
Source Server Version : 50725
Source Host           : 192.168.1.103:3306
Source Database       : dailyfresh

Target Server Type    : MYSQL
Target Server Version : 50725
File Encoding         : 65001

Date: 2019-08-07 22:37:48
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for auth_group
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_group
-- ----------------------------

-- ----------------------------
-- Table structure for auth_group_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group__permission_id_47304e67dfa85713_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_group__permission_id_47304e67dfa85713_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permission_group_id_3527068307aa56e1_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_group_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for auth_permission
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  CONSTRAINT `auth__content_type_id_4dcf2e71b082cbab_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=49 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO `auth_permission` VALUES ('1', 'Can add log entry', '1', 'add_logentry');
INSERT INTO `auth_permission` VALUES ('2', 'Can change log entry', '1', 'change_logentry');
INSERT INTO `auth_permission` VALUES ('3', 'Can delete log entry', '1', 'delete_logentry');
INSERT INTO `auth_permission` VALUES ('4', 'Can add permission', '2', 'add_permission');
INSERT INTO `auth_permission` VALUES ('5', 'Can change permission', '2', 'change_permission');
INSERT INTO `auth_permission` VALUES ('6', 'Can delete permission', '2', 'delete_permission');
INSERT INTO `auth_permission` VALUES ('7', 'Can add group', '3', 'add_group');
INSERT INTO `auth_permission` VALUES ('8', 'Can change group', '3', 'change_group');
INSERT INTO `auth_permission` VALUES ('9', 'Can delete group', '3', 'delete_group');
INSERT INTO `auth_permission` VALUES ('10', 'Can add content type', '4', 'add_contenttype');
INSERT INTO `auth_permission` VALUES ('11', 'Can change content type', '4', 'change_contenttype');
INSERT INTO `auth_permission` VALUES ('12', 'Can delete content type', '4', 'delete_contenttype');
INSERT INTO `auth_permission` VALUES ('13', 'Can add session', '5', 'add_session');
INSERT INTO `auth_permission` VALUES ('14', 'Can change session', '5', 'change_session');
INSERT INTO `auth_permission` VALUES ('15', 'Can delete session', '5', 'delete_session');
INSERT INTO `auth_permission` VALUES ('16', 'Can add 用户', '6', 'add_user');
INSERT INTO `auth_permission` VALUES ('17', 'Can change 用户', '6', 'change_user');
INSERT INTO `auth_permission` VALUES ('18', 'Can delete 用户', '6', 'delete_user');
INSERT INTO `auth_permission` VALUES ('19', 'Can add 地址', '7', 'add_address');
INSERT INTO `auth_permission` VALUES ('20', 'Can change 地址', '7', 'change_address');
INSERT INTO `auth_permission` VALUES ('21', 'Can delete 地址', '7', 'delete_address');
INSERT INTO `auth_permission` VALUES ('22', 'Can add 商品种类', '8', 'add_goodstype');
INSERT INTO `auth_permission` VALUES ('23', 'Can change 商品种类', '8', 'change_goodstype');
INSERT INTO `auth_permission` VALUES ('24', 'Can delete 商品种类', '8', 'delete_goodstype');
INSERT INTO `auth_permission` VALUES ('25', 'Can add 商品', '9', 'add_goodssku');
INSERT INTO `auth_permission` VALUES ('26', 'Can change 商品', '9', 'change_goodssku');
INSERT INTO `auth_permission` VALUES ('27', 'Can delete 商品', '9', 'delete_goodssku');
INSERT INTO `auth_permission` VALUES ('28', 'Can add 商品SPU', '10', 'add_goods');
INSERT INTO `auth_permission` VALUES ('29', 'Can change 商品SPU', '10', 'change_goods');
INSERT INTO `auth_permission` VALUES ('30', 'Can delete 商品SPU', '10', 'delete_goods');
INSERT INTO `auth_permission` VALUES ('31', 'Can add 商品图片', '11', 'add_goodsimage');
INSERT INTO `auth_permission` VALUES ('32', 'Can change 商品图片', '11', 'change_goodsimage');
INSERT INTO `auth_permission` VALUES ('33', 'Can delete 商品图片', '11', 'delete_goodsimage');
INSERT INTO `auth_permission` VALUES ('34', 'Can add 首页轮播商品', '12', 'add_indexgoodsbanner');
INSERT INTO `auth_permission` VALUES ('35', 'Can change 首页轮播商品', '12', 'change_indexgoodsbanner');
INSERT INTO `auth_permission` VALUES ('36', 'Can delete 首页轮播商品', '12', 'delete_indexgoodsbanner');
INSERT INTO `auth_permission` VALUES ('37', 'Can add 主页分类展示商品', '13', 'add_indextypegoodsbanner');
INSERT INTO `auth_permission` VALUES ('38', 'Can change 主页分类展示商品', '13', 'change_indextypegoodsbanner');
INSERT INTO `auth_permission` VALUES ('39', 'Can delete 主页分类展示商品', '13', 'delete_indextypegoodsbanner');
INSERT INTO `auth_permission` VALUES ('40', 'Can add 主页促销活动', '14', 'add_indexpromotionbanner');
INSERT INTO `auth_permission` VALUES ('41', 'Can change 主页促销活动', '14', 'change_indexpromotionbanner');
INSERT INTO `auth_permission` VALUES ('42', 'Can delete 主页促销活动', '14', 'delete_indexpromotionbanner');
INSERT INTO `auth_permission` VALUES ('43', 'Can add 订单', '15', 'add_orderinfo');
INSERT INTO `auth_permission` VALUES ('44', 'Can change 订单', '15', 'change_orderinfo');
INSERT INTO `auth_permission` VALUES ('45', 'Can delete 订单', '15', 'delete_orderinfo');
INSERT INTO `auth_permission` VALUES ('46', 'Can add 订单商品', '16', 'add_ordergoods');
INSERT INTO `auth_permission` VALUES ('47', 'Can change 订单商品', '16', 'change_ordergoods');
INSERT INTO `auth_permission` VALUES ('48', 'Can delete 订单商品', '16', 'delete_ordergoods');

-- ----------------------------
-- Table structure for df_address
-- ----------------------------
DROP TABLE IF EXISTS `df_address`;
CREATE TABLE `df_address` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `receiver` varchar(20) NOT NULL,
  `addr` varchar(256) NOT NULL,
  `zip_code` varchar(6) DEFAULT NULL,
  `phone` varchar(11) NOT NULL,
  `is_default` tinyint(1) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `df_address_user_id_4bc54cff7c6fb0c1_fk_df_user_id` (`user_id`),
  CONSTRAINT `df_address_user_id_4bc54cff7c6fb0c1_fk_df_user_id` FOREIGN KEY (`user_id`) REFERENCES `df_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of df_address
-- ----------------------------
INSERT INTO `df_address` VALUES ('5', '2019-07-30 15:00:17.980000', '2019-08-06 05:48:48.738400', '0', '小王', '湖北省荆州市', '10000', '17671451457', '0', '56');
INSERT INTO `df_address` VALUES ('6', '2019-07-30 15:40:15.285000', '2019-08-06 05:48:48.784400', '0', '小胡', '湖北省荆州市监利县', '10000', '17671451457', '1', '56');
INSERT INTO `df_address` VALUES ('13', '2019-08-05 16:42:56.994000', '2019-08-06 05:48:48.772400', '0', '小李', '湖北省武汉市江夏区', '', '17671451457', '0', '56');
INSERT INTO `df_address` VALUES ('14', '2019-08-05 16:43:11.830000', '2019-08-06 05:48:48.775400', '0', '小马', '北京市朝阳区', '', '17671451457', '0', '56');
INSERT INTO `df_address` VALUES ('15', '2019-08-06 13:57:47.265000', '2019-08-06 13:57:47.265000', '0', '小王', '湖北省荆州市', '', '17671451457', '1', '57');
INSERT INTO `df_address` VALUES ('16', '2019-08-06 14:23:04.749000', '2019-08-06 14:23:04.749000', '0', '王悦', '广州市海珠区龙潭村颖龙北街', '', '16602735201', '0', '56');

-- ----------------------------
-- Table structure for df_goods
-- ----------------------------
DROP TABLE IF EXISTS `df_goods`;
CREATE TABLE `df_goods` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `name` varchar(20) NOT NULL,
  `detail` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of df_goods
-- ----------------------------
INSERT INTO `df_goods` VALUES ('1', '2017-11-15 03:03:05.257969', '2017-11-15 03:03:05.258130', '0', '草莓', '<p><strong>草莓采摘园位于北京大兴区 庞各庄镇四各庄村 ，每年1月-6月面向北京以及周围城市提供新鲜草莓采摘和精品礼盒装草莓，草莓品种多样丰富，个大香甜。所有草莓均严格按照有机标准培育，不使用任何化肥和农药。草莓在采摘期间免洗可以直接食用。欢迎喜欢草莓的市民前来采摘，也欢迎各大单位选购精品有机草莓礼盒，有机草莓礼盒是亲朋馈赠、福利送礼的最佳选择。</strong></p>');
INSERT INTO `df_goods` VALUES ('2', '2017-11-15 03:05:36.964951', '2017-11-15 03:05:36.965129', '0', '葡萄', '');
INSERT INTO `df_goods` VALUES ('3', '2017-11-15 03:05:52.323866', '2017-11-15 03:05:52.323949', '0', '柠檬', '');
INSERT INTO `df_goods` VALUES ('4', '2017-11-15 03:06:01.267481', '2017-11-15 03:06:01.267615', '0', '奇异果', '');
INSERT INTO `df_goods` VALUES ('5', '2017-11-15 03:06:30.418683', '2017-11-15 03:06:30.418789', '0', '大青虾', '');
INSERT INTO `df_goods` VALUES ('6', '2017-11-15 03:06:35.994464', '2017-11-15 03:06:35.994567', '0', '秋刀鱼', '');
INSERT INTO `df_goods` VALUES ('7', '2017-11-15 03:06:48.115318', '2017-11-15 03:06:48.115410', '0', '扇贝', '');
INSERT INTO `df_goods` VALUES ('8', '2017-11-15 03:07:03.057514', '2017-11-15 03:07:03.057601', '0', '基围虾', '');
INSERT INTO `df_goods` VALUES ('9', '2017-11-15 03:07:36.306725', '2017-11-15 03:07:36.306926', '0', '猪肉', '');
INSERT INTO `df_goods` VALUES ('10', '2017-11-15 03:07:39.056064', '2017-11-15 03:07:39.056145', '0', '牛肉', '');
INSERT INTO `df_goods` VALUES ('11', '2017-11-15 03:07:41.955755', '2017-11-15 03:07:41.955833', '0', '羊肉', '');
INSERT INTO `df_goods` VALUES ('12', '2017-11-15 03:07:44.741474', '2017-11-15 03:07:44.741574', '0', '牛排', '');
INSERT INTO `df_goods` VALUES ('13', '2017-11-15 03:07:51.748699', '2017-11-15 03:07:51.748828', '0', '鸡蛋', '');
INSERT INTO `df_goods` VALUES ('14', '2017-11-15 03:07:56.413773', '2017-11-15 03:07:56.413853', '0', '鸡肉', '');
INSERT INTO `df_goods` VALUES ('15', '2017-11-15 03:07:59.568405', '2017-11-15 03:07:59.568554', '0', '鸭蛋', '');
INSERT INTO `df_goods` VALUES ('16', '2017-11-15 03:08:03.020608', '2017-11-15 03:08:03.020764', '0', '鸡腿', '');
INSERT INTO `df_goods` VALUES ('17', '2017-11-15 03:08:10.063820', '2017-11-15 03:08:10.063898', '0', '白菜', '');
INSERT INTO `df_goods` VALUES ('18', '2017-11-15 03:08:13.315906', '2017-11-15 03:08:13.316025', '0', '芹菜', '');
INSERT INTO `df_goods` VALUES ('19', '2017-11-15 03:08:16.351445', '2017-11-15 03:08:16.351526', '0', '香菜', '');
INSERT INTO `df_goods` VALUES ('20', '2017-11-15 03:08:24.232660', '2017-11-15 03:08:24.232743', '0', '冬瓜', '');
INSERT INTO `df_goods` VALUES ('21', '2017-11-15 03:08:36.939678', '2017-11-15 03:08:36.940113', '0', '鱼丸', '');
INSERT INTO `df_goods` VALUES ('22', '2017-11-15 03:08:43.194862', '2017-11-15 03:08:43.194985', '0', '蟹棒', '');
INSERT INTO `df_goods` VALUES ('23', '2017-11-15 03:08:50.771785', '2017-11-15 03:08:50.771931', '0', '虾丸', '');
INSERT INTO `df_goods` VALUES ('24', '2017-11-15 03:09:01.546052', '2017-11-15 03:09:01.546152', '0', '速冻水饺', '');
INSERT INTO `df_goods` VALUES ('25', '2017-11-14 08:50:50.383071', '2017-11-14 08:50:50.383115', '0', '芒果', '');
INSERT INTO `df_goods` VALUES ('26', '2017-11-17 07:54:26.657410', '2017-11-17 07:54:26.657443', '0', '鹌鹑蛋', '');
INSERT INTO `df_goods` VALUES ('27', '2017-11-17 07:54:35.205668', '2017-11-17 07:54:35.205703', '0', '鹅蛋', '');
INSERT INTO `df_goods` VALUES ('28', '2017-11-17 07:54:46.756236', '2017-11-17 07:54:46.756272', '0', '红辣椒', '');
INSERT INTO `df_goods` VALUES ('29', '2019-08-02 23:15:45.000000', '2019-08-02 23:15:48.000000', '0', '河虾', '</strong></p>');
INSERT INTO `df_goods` VALUES ('30', '2019-08-03 19:44:32.000000', '2019-08-03 19:44:34.000000', '0', '苹果', '</p><strong>苹果红又大</strong></p>');

-- ----------------------------
-- Table structure for df_goods_image
-- ----------------------------
DROP TABLE IF EXISTS `df_goods_image`;
CREATE TABLE `df_goods_image` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `image` varchar(100) NOT NULL,
  `sku_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `df_goods_image_22ad5bca` (`sku_id`),
  CONSTRAINT `df_goods_image_sku_id_12c8678c4fe8cbc1_fk_df_goods_sku_id` FOREIGN KEY (`sku_id`) REFERENCES `df_goods_sku` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of df_goods_image
-- ----------------------------
INSERT INTO `df_goods_image` VALUES ('1', '2019-08-02 15:08:42.339000', '2019-08-02 15:08:42.339000', '0', 'group1/M00/00/00/wKgBZ11EUfqAdv3tAAAljHPuXJg1421587', '14');
INSERT INTO `df_goods_image` VALUES ('2', '2019-08-02 15:08:52.336000', '2019-08-02 15:08:52.336000', '0', 'group1/M00/00/00/wKgBZ11EUgSAJ8dNAAAjjiYTEkw7596828', '19');
INSERT INTO `df_goods_image` VALUES ('3', '2019-08-02 15:09:09.801000', '2019-08-02 15:09:09.801000', '0', 'group1/M00/00/00/wKgBZ11EUhWAW-9sAAAgnaeGwNQ1914798', '21');
INSERT INTO `df_goods_image` VALUES ('4', '2019-08-02 15:09:26.550000', '2019-08-02 15:09:26.550000', '0', 'group1/M00/00/00/wKgBZ11EUiaABScnAAAeuLYy0pU0202360', '22');
INSERT INTO `df_goods_image` VALUES ('5', '2019-08-02 15:29:20.775000', '2019-08-02 15:29:20.775000', '0', 'group1/M00/00/00/wKgBZ11EVtCAdKFhAAAk0DN4-yE6486713', '17');
INSERT INTO `df_goods_image` VALUES ('6', '2019-08-02 15:32:27.329000', '2019-08-02 15:32:27.329000', '0', 'group1/M00/00/00/wKgBZ11EV4uAVpo5AAAk8WCqqmI5168080', '24');
INSERT INTO `df_goods_image` VALUES ('7', '2019-08-02 15:35:02.856000', '2019-08-02 15:35:02.856000', '0', 'group1/M00/00/00/wKgBZ11EWCaAIP49AAA5OS4Kl4c1260886', '23');
INSERT INTO `df_goods_image` VALUES ('8', '2019-08-02 15:37:48.384000', '2019-08-02 15:37:48.384000', '0', 'group1/M00/00/00/wKgBZ11EWMyATTnWAAAkaP_7_189557238', '25');
INSERT INTO `df_goods_image` VALUES ('9', '2019-08-03 00:29:23.000000', '2019-08-02 16:30:03.740000', '0', 'group1/M00/00/00/wKgBZ11EZQuAUVrpAAEExAU4yXU1114064', '26');
INSERT INTO `df_goods_image` VALUES ('10', '2019-08-03 00:30:28.000000', '2019-08-02 16:32:03.878000', '0', 'group1/M00/00/00/wKgBZ11EZYOACz3TAAB6NOQDrpk4207102', '27');
INSERT INTO `df_goods_image` VALUES ('11', '2019-08-03 00:35:06.000000', '2019-08-02 16:35:56.883000', '0', 'group1/M00/00/00/wKgBZ11EZmyAOrs1AAEVpb1YHUE6825839', '28');
INSERT INTO `df_goods_image` VALUES ('12', '2019-08-03 00:35:23.000000', '2019-08-02 16:36:06.418000', '0', 'group1/M00/00/00/wKgBZ11EZnaAaMexAACwa3rCDPQ6897293', '29');
INSERT INTO `df_goods_image` VALUES ('13', '2019-08-03 12:25:29.000000', '2019-08-03 04:28:42.094000', '0', 'group1/M00/00/00/wKgBZ11FDXmAbrxrAADUKbwLSqY4419273', '30');
INSERT INTO `df_goods_image` VALUES ('14', '2019-08-03 12:25:29.000000', '2019-08-03 04:28:53.360000', '0', 'group1/M00/00/00/wKgBZ11FDYSAXm99AADUY5hC_sI2694888', '31');
INSERT INTO `df_goods_image` VALUES ('15', '2019-08-03 12:25:29.000000', '2019-08-03 04:29:04.438000', '0', 'group1/M00/00/00/wKgBZ11FDZCAbu7CAAFC_2tSkFo8174905', '32');
INSERT INTO `df_goods_image` VALUES ('16', '2019-08-03 12:25:29.000000', '2019-08-03 04:29:15.087000', '0', 'group1/M00/00/00/wKgBZ11FDZqAb4LIAAA2_p7G96w7429356', '33');
INSERT INTO `df_goods_image` VALUES ('17', '2019-08-03 12:25:29.000000', '2019-08-03 04:43:52.518000', '0', 'group1/M00/00/00/wKgBZ11FEQiAMgUzAADWHYeKaNI4523912', '34');
INSERT INTO `df_goods_image` VALUES ('18', '2019-08-03 12:25:29.000000', '2019-08-03 04:44:05.694000', '0', 'group1/M00/00/00/wKgBZ11FERWANXmZAACIrzuaK640148548', '35');
INSERT INTO `df_goods_image` VALUES ('19', '2019-08-03 12:25:29.000000', '2019-08-03 04:44:19.830000', '0', 'group1/M00/00/00/wKgBZ11FESOACeY7AACNpHC0IEY8631676', '36');
INSERT INTO `df_goods_image` VALUES ('20', '2019-08-03 12:25:29.000000', '2019-08-03 04:44:29.190000', '0', 'group1/M00/00/00/wKgBZ11FESyAXQS9AAENHrNG1-s9842233', '37');
INSERT INTO `df_goods_image` VALUES ('21', '2019-08-03 12:25:29.000000', '2019-08-03 04:46:57.515000', '0', 'group1/M00/00/00/wKgBZ11FEcGAApiMAADZQphQJ2o6115450', '38');
INSERT INTO `df_goods_image` VALUES ('22', '2019-08-03 12:25:29.000000', '2019-08-03 04:47:06.167000', '0', 'group1/M00/00/00/wKgBZ11FEcmAMD6eAABxy5vKkgY8023640', '39');
INSERT INTO `df_goods_image` VALUES ('23', '2019-08-03 12:25:29.000000', '2019-08-03 04:47:16.476000', '0', 'group1/M00/00/00/wKgBZ11FEdSAKzILAABICav_wjk4834015', '40');
INSERT INTO `df_goods_image` VALUES ('24', '2019-08-03 12:25:29.000000', '2019-08-03 04:48:30.755000', '0', 'group1/M00/00/00/wKgBZ11FEh6AfnkcAACMoBJXjDs3177579', '41');

-- ----------------------------
-- Table structure for df_goods_sku
-- ----------------------------
DROP TABLE IF EXISTS `df_goods_sku`;
CREATE TABLE `df_goods_sku` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `name` varchar(20) NOT NULL,
  `desc` varchar(256) NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `unite` varchar(20) NOT NULL,
  `image` varchar(100) NOT NULL,
  `stock` int(11) NOT NULL,
  `sales` int(11) NOT NULL,
  `status` smallint(6) NOT NULL,
  `goods_id` int(11) NOT NULL,
  `type_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `df_goods_sku_goods_id_52f533b7084d67a4_fk_df_goods_id` (`goods_id`),
  KEY `df_goods_sku_94757cae` (`type_id`),
  CONSTRAINT `df_goods_sku_goods_id_52f533b7084d67a4_fk_df_goods_id` FOREIGN KEY (`goods_id`) REFERENCES `df_goods` (`id`),
  CONSTRAINT `df_goods_sku_type_id_20f087a1b0b15d09_fk_df_goods_type_id` FOREIGN KEY (`type_id`) REFERENCES `df_goods_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=42 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of df_goods_sku
-- ----------------------------
INSERT INTO `df_goods_sku` VALUES ('12', '2019-08-03 19:43:13.000000', '2019-08-07 05:29:04.189999', '0', '红富士大苹果', '商品简介', '18.00', '500g', 'group1/M00/00/00/wKgBZ11FdC2AIVgUAADN80inxaQ0565398', '28', '7', '1', '30', '1');
INSERT INTO `df_goods_sku` VALUES ('13', '2019-08-03 16:19:58.000000', '2019-08-06 11:40:22.528000', '0', '盒装草莓', '商品简介', '16.00', '盒', 'group1/M00/00/00/wKgBZ11FRDmAO7jaAAEc8FlxEvU5641090', '23', '10', '1', '1', '1');
INSERT INTO `df_goods_sku` VALUES ('14', '2019-08-03 13:48:42.000000', '2019-08-03 05:51:05.168000', '0', '大兴大棚草莓', '草莓浆果柔软多汁，味美爽口，适合速冻保鲜贮藏。草莓速冻后，可以保持原有的色、香、味，既便于贮藏，又便于外销', '16.00', '500g', 'group1/M00/00/00/wKgBZ11FIMiANekaAADhpU9_Ylo5002860', '30', '1', '1', '1', '1');
INSERT INTO `df_goods_sku` VALUES ('15', '2019-08-02 14:09:44.686000', '2019-08-06 14:26:32.784000', '0', '草莓', '商品简介', '30.00', '500g', 'group1/M00/00/00/wKgBZ11FILiAYRNzAAAljHPuXJg3270222', '22', '14', '1', '1', '1');
INSERT INTO `df_goods_sku` VALUES ('16', '2019-08-02 14:29:17.693000', '2019-08-02 14:29:17.693000', '0', '鲜芒', '商品简介', '29.90', '2.5kg', 'group1/M00/00/00/wKgBZ11ESL2AU4cbAAAZxC0XRLc8303067', '20', '2', '1', '25', '1');
INSERT INTO `df_goods_sku` VALUES ('17', '2019-08-02 14:33:53.597000', '2019-08-02 14:33:53.598000', '0', '大青虾', '商品简介', '48.00', '500g', 'group1/M00/00/00/wKgBZ11ESdGAGbf8AAAk0DN4-yE0452978', '5', '1', '1', '5', '2');
INSERT INTO `df_goods_sku` VALUES ('18', '2019-08-02 14:36:45.888000', '2019-08-02 14:36:45.888000', '0', '新鲜蒙古牛肩肉', '商品简介', '40.00', '500g', 'group1/M00/00/00/wKgBZ11ESn2AAbFkAAEExAU4yXU5545951', '5', '1', '1', '10', '3');
INSERT INTO `df_goods_sku` VALUES ('19', '2019-08-02 14:47:50.625000', '2019-08-02 14:47:50.625000', '0', '加州提子', '商品简介', '60.00', '500g', 'group1/M00/00/00/wKgBZ11ETRaAI0s2AAAjjiYTEkw3548144', '20', '2', '1', '2', '1');
INSERT INTO `df_goods_sku` VALUES ('20', '2019-08-02 14:53:04.342000', '2019-08-07 05:12:21.837999', '0', '亚马逊牛油果', '商品简介', '48.00', '500g', 'group1/M00/00/00/wKgBZ11ETlCAEF86AAAidvtT3FY7901555', '18', '6', '1', '4', '1');
INSERT INTO `df_goods_sku` VALUES ('21', '2019-08-02 14:57:48.154000', '2019-08-07 12:48:37.233000', '0', '柠檬', '商品简介', '25.00', '500g', 'group1/M00/00/00/wKgBZ11ET2yAdSa6AAAgnaeGwNQ8082326', '19', '5', '1', '3', '1');
INSERT INTO `df_goods_sku` VALUES ('22', '2019-08-02 14:58:45.350000', '2019-08-07 14:27:33.945000', '0', '奇异果', '商品简介', '25.80', '500g', 'group1/M00/00/00/wKgBZ11ET6WAEGj1AAAeuLYy0pU2827741', '13', '10', '1', '4', '1');
INSERT INTO `df_goods_sku` VALUES ('23', '2019-08-02 23:13:09.000000', '2019-08-02 15:18:33.686000', '0', '河虾', '商品简介', '48.00', '500g', 'group1/M00/00/00/wKgBZ11EVEmAKdxqAAA5OS4Kl4c9539111', '20', '3', '1', '29', '2');
INSERT INTO `df_goods_sku` VALUES ('24', '2019-08-02 23:20:35.000000', '2019-08-02 15:23:44.257000', '0', '扇贝', '商品简介', '46.00', '500g', 'group1/M00/00/00/wKgBZ11EVYCARdObAAAk8WCqqmI3895265', '20', '2', '1', '7', '2');
INSERT INTO `df_goods_sku` VALUES ('25', '2019-08-02 23:35:44.000000', '2019-08-02 15:38:10.699000', '0', '冷冻秋刀鱼', '商品简介', '19.00', '500g', 'group1/M00/00/00/wKgBZ11EWOKAIZSLAAAkaP_7_186612411', '20', '2', '1', '6', '2');
INSERT INTO `df_goods_sku` VALUES ('26', '2019-08-03 00:23:48.000000', '2019-08-02 16:28:11.087000', '0', '牛肉', '商品简介', '38.00', '500g', 'group1/M00/00/00/wKgBZ11EZJqADGlAAAEExAU4yXU8880131', '20', '2', '1', '10', '3');
INSERT INTO `df_goods_sku` VALUES ('27', '2019-08-03 00:26:23.000000', '2019-08-02 16:27:56.380000', '0', '羊肉', '商品简介', '45.00', '500g', 'group1/M00/00/00/wKgBZ11EZIyANtyZAAB6NOQDrpk3229052', '20', '2', '1', '11', '3');
INSERT INTO `df_goods_sku` VALUES ('28', '2019-08-03 00:32:25.000000', '2019-08-02 16:36:26.053000', '0', '猪肉', '商品简介', '35.00', '500g', 'group1/M00/00/00/wKgBZ11EZomAFEFDAAEVpb1YHUE4155866', '20', '2', '1', '9', '3');
INSERT INTO `df_goods_sku` VALUES ('29', '2019-08-03 00:33:26.000000', '2019-08-02 16:36:38.500000', '0', '羊排', '商品简介', '68.00', '500g', 'group1/M00/00/00/wKgBZ11EZpaAXJX2AACwa3rCDPQ5638222', '20', '2', '1', '12', '3');
INSERT INTO `df_goods_sku` VALUES ('30', '2019-08-03 12:19:20.000000', '2019-08-03 04:27:18.689000', '0', '鸡蛋', '商品简介', '12.00', '500g', 'group1/M00/00/00/wKgBZ11FDSaASGPOAADUKbwLSqY9868687', '50', '10', '1', '13', '4');
INSERT INTO `df_goods_sku` VALUES ('31', '2019-08-03 12:20:12.000000', '2019-08-03 04:27:32.621000', '0', '鸡肉', '商品简介', '21.00', '500g', 'group1/M00/00/00/wKgBZ11FDTSAdhD1AADUY5hC_sI2058534', '30', '1', '1', '14', '4');
INSERT INTO `df_goods_sku` VALUES ('32', '2019-08-03 12:21:09.000000', '2019-08-03 04:27:43.952000', '0', '鸭蛋', '商品简介', '15.00', '500g', 'group1/M00/00/00/wKgBZ11FDT-ABwpJAAFC_2tSkFo7011933', '50', '1', '1', '15', '4');
INSERT INTO `df_goods_sku` VALUES ('33', '2019-08-03 12:21:53.000000', '2019-08-03 04:27:54.845000', '0', '鸡腿', '商品简介', '23.00', '500g', 'group1/M00/00/00/wKgBZ11FDUqAFeV2AAA2_p7G96w0457216', '30', '1', '1', '16', '4');
INSERT INTO `df_goods_sku` VALUES ('34', '2019-08-03 12:21:53.000000', '2019-08-03 04:45:00.754000', '0', '白菜', '商品简介', '23.00', '500g', 'group1/M00/00/00/wKgBZ11FEUyARVjEAADWHYeKaNI8183047', '30', '1', '1', '17', '5');
INSERT INTO `df_goods_sku` VALUES ('35', '2019-08-03 12:21:53.000000', '2019-08-03 04:45:11.848000', '0', '芹菜', '商品简介', '23.00', '500g', 'group1/M00/00/00/wKgBZ11FEVeAGw6cAACIrzuaK647441508', '30', '1', '1', '18', '5');
INSERT INTO `df_goods_sku` VALUES ('36', '2019-08-03 12:21:53.000000', '2019-08-03 04:45:24.341000', '0', '香菜', '商品简介', '23.00', '500g', 'group1/M00/00/00/wKgBZ11FEWOAQwIqAACNpHC0IEY1315549', '30', '1', '1', '19', '5');
INSERT INTO `df_goods_sku` VALUES ('37', '2019-08-03 12:21:53.000000', '2019-08-03 04:45:34.743000', '0', '冬瓜', '商品简介', '23.00', '500g', 'group1/M00/00/00/wKgBZ11FEW6AXVr9AAENHrNG1-s5823227', '30', '1', '1', '20', '5');
INSERT INTO `df_goods_sku` VALUES ('38', '2019-08-03 12:21:53.000000', '2019-08-03 04:45:59.196000', '0', '鱼丸', '商品简介', '23.00', '500g', 'group1/M00/00/00/wKgBZ11FEYaAMi2BAADZQphQJ2o7981042', '30', '1', '1', '21', '6');
INSERT INTO `df_goods_sku` VALUES ('39', '2019-08-03 12:21:53.000000', '2019-08-03 04:46:09.756000', '0', '蟹棒', '商品简介', '23.00', '500g', 'group1/M00/00/00/wKgBZ11FEZGAda4DAABxy5vKkgY1792346', '30', '1', '1', '22', '6');
INSERT INTO `df_goods_sku` VALUES ('40', '2019-08-03 12:21:53.000000', '2019-08-03 04:46:21.406000', '0', '虾丸', '商品简介', '23.00', '500g', 'group1/M00/00/00/wKgBZ11FEZyALeKoAABICav_wjk3855278', '30', '1', '1', '23', '6');
INSERT INTO `df_goods_sku` VALUES ('41', '2019-08-03 12:21:53.000000', '2019-08-03 04:46:31.343000', '0', '速冻水饺', '商品简介', '23.00', '500g', 'group1/M00/00/00/wKgBZ11FEaaAAKT0AACMoBJXjDs3592706', '30', '1', '1', '24', '6');

-- ----------------------------
-- Table structure for df_goods_type
-- ----------------------------
DROP TABLE IF EXISTS `df_goods_type`;
CREATE TABLE `df_goods_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `name` varchar(20) NOT NULL,
  `logo` varchar(20) NOT NULL,
  `image` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of df_goods_type
-- ----------------------------
INSERT INTO `df_goods_type` VALUES ('1', '2019-08-01 14:44:49.213000', '2019-08-01 14:44:49.213000', '0', '新鲜水果', 'fruit', 'group1/M00/00/00/wKgBZ11C-uCAMS53AAAmv27pX4k2321230');
INSERT INTO `df_goods_type` VALUES ('2', '2019-08-01 14:45:31.700000', '2019-08-01 14:45:31.700000', '0', '海鲜水产', 'seafood', 'group1/M00/00/00/wKgBZ11C-wuADn3yAABHr3RQqFs0958030');
INSERT INTO `df_goods_type` VALUES ('3', '2019-08-02 14:23:11.763000', '2019-08-02 14:23:11.763000', '0', '猪牛羊肉', 'meet', 'group1/M00/00/00/wKgBZ11ER0-AOFfeAAAy1Tlm9So7314267');
INSERT INTO `df_goods_type` VALUES ('4', '2019-08-02 09:20:01.375000', '2019-08-02 09:20:01.375000', '0', '禽类蛋品', 'egg', 'group1/M00/00/00/wKgBZ11EAECAF9r_AAAqR4DoSUg4031553');
INSERT INTO `df_goods_type` VALUES ('5', '2019-08-02 09:20:41.670000', '2019-08-02 09:20:41.670000', '0', '新鲜蔬菜', 'vegetables', 'group1/M00/00/00/wKgBZ11EAGiACHe8AAA-0ZoYkpM2634868');
INSERT INTO `df_goods_type` VALUES ('6', '2019-08-02 09:21:09.624000', '2019-08-02 09:21:09.625000', '0', '速冻食品', 'ice', 'group1/M00/00/00/wKgBZ11EAISAT29MAAA3sZPrVzQ1867770');

-- ----------------------------
-- Table structure for df_index_banner
-- ----------------------------
DROP TABLE IF EXISTS `df_index_banner`;
CREATE TABLE `df_index_banner` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `image` varchar(100) NOT NULL,
  `index` smallint(6) NOT NULL,
  `sku_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `df_index_banner_sku_id_54d616864011dfd6_fk_df_goods_sku_id` (`sku_id`),
  CONSTRAINT `df_index_banner_sku_id_54d616864011dfd6_fk_df_goods_sku_id` FOREIGN KEY (`sku_id`) REFERENCES `df_goods_sku` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of df_index_banner
-- ----------------------------
INSERT INTO `df_index_banner` VALUES ('2', '2019-08-02 14:14:06.435000', '2019-08-02 14:14:06.435000', '0', 'group1/M00/00/00/wKgBZ11ERS6AIciXAACpB-LsCdE9589957', '0', '15');
INSERT INTO `df_index_banner` VALUES ('3', '2019-08-02 14:29:53.074000', '2019-08-02 14:29:53.074000', '0', 'group1/M00/00/00/wKgBZ11ESOCAaAMEAAC3B-z8J2c5074960', '1', '16');
INSERT INTO `df_index_banner` VALUES ('4', '2019-08-02 14:39:18.868000', '2019-08-03 06:37:33.712000', '0', 'group1/M00/00/00/wKgBZ11FK62AAT8gAAETwXb_pso7048334', '2', '18');
INSERT INTO `df_index_banner` VALUES ('5', '2019-08-02 14:39:32.161000', '2019-08-03 06:37:41.963000', '0', 'group1/M00/00/00/wKgBZ11FK7WAd0LnAAD0akkXmFo0843497', '3', '17');

-- ----------------------------
-- Table structure for df_index_promotion
-- ----------------------------
DROP TABLE IF EXISTS `df_index_promotion`;
CREATE TABLE `df_index_promotion` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `name` varchar(20) NOT NULL,
  `url` varchar(200) NOT NULL,
  `image` varchar(100) NOT NULL,
  `index` smallint(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of df_index_promotion
-- ----------------------------
INSERT INTO `df_index_promotion` VALUES ('1', '2017-11-14 08:56:21.863522', '2019-08-02 11:39:21.940000', '0', '吃货暑假趴', '#', 'group1/M00/00/00/wKgBZ11EHZSABgKyAAA2pLUeB602769537', '2');
INSERT INTO `df_index_promotion` VALUES ('2', '2017-11-14 08:56:53.522161', '2019-08-02 11:24:59.344000', '0', '盛夏尝鲜季', '#', 'group1/M00/00/00/wKgBZ11EHYuAUTSYAAA98yvCs1I0104680', '1');

-- ----------------------------
-- Table structure for df_index_type_goods
-- ----------------------------
DROP TABLE IF EXISTS `df_index_type_goods`;
CREATE TABLE `df_index_type_goods` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `display_type` smallint(6) NOT NULL,
  `index` smallint(6) NOT NULL,
  `sku_id` int(11) NOT NULL,
  `type_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `df_index_type_goods_sku_id_6f59ae84fe1500ff_fk_df_goods_sku_id` (`sku_id`),
  KEY `df_index_type_goods_type_id_4efd7bd0467c0a3e_fk_df_goods_type_id` (`type_id`),
  CONSTRAINT `df_index_type_goods_sku_id_6f59ae84fe1500ff_fk_df_goods_sku_id` FOREIGN KEY (`sku_id`) REFERENCES `df_goods_sku` (`id`),
  CONSTRAINT `df_index_type_goods_type_id_4efd7bd0467c0a3e_fk_df_goods_type_id` FOREIGN KEY (`type_id`) REFERENCES `df_goods_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=40 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of df_index_type_goods
-- ----------------------------
INSERT INTO `df_index_type_goods` VALUES ('2', '2019-08-02 14:41:47.823000', '2019-08-02 14:41:47.823000', '0', '0', '0', '16', '1');
INSERT INTO `df_index_type_goods` VALUES ('3', '2019-08-02 14:44:26.863000', '2019-08-02 14:44:26.863000', '0', '0', '1', '19', '1');
INSERT INTO `df_index_type_goods` VALUES ('4', '2019-08-02 14:54:45.263000', '2019-08-02 14:54:45.263000', '0', '0', '2', '20', '1');
INSERT INTO `df_index_type_goods` VALUES ('5', '2019-08-02 14:55:56.028000', '2019-08-02 14:55:56.028000', '0', '1', '0', '15', '1');
INSERT INTO `df_index_type_goods` VALUES ('6', '2019-08-02 14:59:30.865000', '2019-08-02 14:59:30.865000', '0', '1', '1', '19', '1');
INSERT INTO `df_index_type_goods` VALUES ('7', '2019-08-02 14:59:41.113000', '2019-08-02 14:59:41.113000', '0', '1', '2', '21', '1');
INSERT INTO `df_index_type_goods` VALUES ('8', '2019-08-02 14:59:51.392000', '2019-08-02 14:59:51.392000', '0', '1', '3', '22', '1');
INSERT INTO `df_index_type_goods` VALUES ('9', '2019-08-02 23:19:07.000000', '2019-08-02 23:19:10.000000', '0', '0', '0', '23', '2');
INSERT INTO `df_index_type_goods` VALUES ('10', '2019-08-02 23:22:29.000000', '2019-08-02 23:22:32.000000', '0', '0', '1', '24', '2');
INSERT INTO `df_index_type_goods` VALUES ('11', '2019-07-30 23:26:22.000000', '2019-08-02 23:26:26.000000', '0', '1', '0', '17', '2');
INSERT INTO `df_index_type_goods` VALUES ('12', '2019-08-02 23:32:39.000000', '2019-08-02 23:32:42.000000', '0', '1', '1', '24', '2');
INSERT INTO `df_index_type_goods` VALUES ('13', '2019-08-02 23:35:14.000000', '2019-08-02 23:35:17.000000', '0', '1', '2', '25', '2');
INSERT INTO `df_index_type_goods` VALUES ('14', '2019-08-02 23:33:48.000000', '2019-08-02 23:33:51.000000', '0', '1', '3', '23', '2');
INSERT INTO `df_index_type_goods` VALUES ('15', '2019-08-03 00:23:06.000000', '2019-08-03 00:23:08.000000', '0', '0', '0', '26', '3');
INSERT INTO `df_index_type_goods` VALUES ('16', '2019-08-03 00:26:03.000000', '2019-08-03 00:26:06.000000', '0', '0', '1', '27', '3');
INSERT INTO `df_index_type_goods` VALUES ('17', '2019-08-03 00:28:50.000000', '2019-08-03 00:28:52.000000', '0', '1', '0', '26', '3');
INSERT INTO `df_index_type_goods` VALUES ('18', '2019-08-03 00:30:50.000000', '2019-08-03 00:30:52.000000', '0', '1', '1', '27', '3');
INSERT INTO `df_index_type_goods` VALUES ('19', '2019-08-03 00:34:27.000000', '2019-08-03 00:34:29.000000', '0', '1', '2', '28', '3');
INSERT INTO `df_index_type_goods` VALUES ('20', '2019-08-03 00:34:44.000000', '2019-08-03 00:34:46.000000', '0', '1', '3', '29', '3');
INSERT INTO `df_index_type_goods` VALUES ('21', '2019-08-03 12:18:27.000000', '2019-08-03 12:18:32.000000', '0', '0', '0', '30', '4');
INSERT INTO `df_index_type_goods` VALUES ('22', '2019-08-03 12:22:51.000000', '2019-08-03 12:22:52.000000', '0', '0', '1', '31', '4');
INSERT INTO `df_index_type_goods` VALUES ('23', '2019-08-03 12:23:35.000000', '2019-08-03 12:23:37.000000', '0', '0', '2', '32', '4');
INSERT INTO `df_index_type_goods` VALUES ('24', '2019-08-03 12:23:54.000000', '2019-08-03 12:23:56.000000', '0', '1', '0', '30', '4');
INSERT INTO `df_index_type_goods` VALUES ('25', '2019-08-03 12:24:09.000000', '2019-08-03 12:24:11.000000', '0', '1', '1', '31', '4');
INSERT INTO `df_index_type_goods` VALUES ('26', '2019-08-03 12:24:25.000000', '2019-08-03 12:24:27.000000', '0', '1', '2', '32', '4');
INSERT INTO `df_index_type_goods` VALUES ('27', '2019-08-03 12:24:40.000000', '2019-08-03 12:24:41.000000', '0', '1', '3', '33', '4');
INSERT INTO `df_index_type_goods` VALUES ('28', '2019-08-03 12:24:40.000000', '2019-08-03 12:24:41.000000', '0', '0', '3', '34', '5');
INSERT INTO `df_index_type_goods` VALUES ('29', '2019-08-03 12:24:40.000000', '2019-08-03 12:24:41.000000', '0', '0', '3', '35', '5');
INSERT INTO `df_index_type_goods` VALUES ('30', '2019-08-03 12:24:40.000000', '2019-08-03 12:24:41.000000', '0', '1', '3', '34', '5');
INSERT INTO `df_index_type_goods` VALUES ('31', '2019-08-03 12:24:40.000000', '2019-08-03 12:24:41.000000', '0', '1', '3', '35', '5');
INSERT INTO `df_index_type_goods` VALUES ('32', '2019-08-03 12:24:40.000000', '2019-08-03 12:24:41.000000', '0', '1', '3', '36', '5');
INSERT INTO `df_index_type_goods` VALUES ('33', '2019-08-03 12:24:40.000000', '2019-08-03 12:24:41.000000', '0', '1', '3', '37', '5');
INSERT INTO `df_index_type_goods` VALUES ('34', '2019-08-03 12:24:40.000000', '2019-08-03 12:24:41.000000', '0', '0', '3', '38', '6');
INSERT INTO `df_index_type_goods` VALUES ('35', '2019-08-03 12:24:40.000000', '2019-08-03 12:24:41.000000', '0', '0', '3', '39', '6');
INSERT INTO `df_index_type_goods` VALUES ('36', '2019-08-03 12:24:40.000000', '2019-08-03 12:24:41.000000', '0', '1', '3', '38', '6');
INSERT INTO `df_index_type_goods` VALUES ('37', '2019-08-03 12:24:40.000000', '2019-08-03 12:24:41.000000', '0', '1', '3', '39', '6');
INSERT INTO `df_index_type_goods` VALUES ('38', '2019-08-03 12:24:40.000000', '2019-08-03 12:24:41.000000', '0', '1', '3', '40', '6');
INSERT INTO `df_index_type_goods` VALUES ('39', '2019-08-03 12:24:40.000000', '2019-08-03 12:24:41.000000', '0', '1', '3', '41', '6');

-- ----------------------------
-- Table structure for df_order_goods
-- ----------------------------
DROP TABLE IF EXISTS `df_order_goods`;
CREATE TABLE `df_order_goods` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `count` int(11) NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `comment` varchar(256) NOT NULL,
  `order_id` varchar(128) NOT NULL,
  `sku_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `df_order_goods_69dfcb07` (`order_id`),
  KEY `df_order_goods_22ad5bca` (`sku_id`),
  CONSTRAINT `df_order_good_order_id_445ab0f6571d59b_fk_df_order_info_order_id` FOREIGN KEY (`order_id`) REFERENCES `df_order_info` (`order_id`),
  CONSTRAINT `df_order_goods_sku_id_4959bd6e4c57d266_fk_df_goods_sku_id` FOREIGN KEY (`sku_id`) REFERENCES `df_goods_sku` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of df_order_goods
-- ----------------------------
INSERT INTO `df_order_goods` VALUES ('9', '2019-08-07 05:12:20.673999', '2019-08-07 14:14:52.797000', '0', '3', '25.80', '很好吃', '2019080713122056', '22');
INSERT INTO `df_order_goods` VALUES ('10', '2019-08-07 05:12:21.833999', '2019-08-07 14:14:52.831000', '0', '2', '48.00', '很香', '2019080713122056', '20');
INSERT INTO `df_order_goods` VALUES ('11', '2019-08-07 05:29:04.188999', '2019-08-07 14:34:17.520000', '0', '2', '18.00', '又大又红的苹果，好吃', '2019080713290456', '12');
INSERT INTO `df_order_goods` VALUES ('12', '2019-08-07 12:48:37.226000', '2019-08-07 12:48:37.226000', '0', '1', '25.00', '', '2019080720483756', '21');
INSERT INTO `df_order_goods` VALUES ('13', '2019-08-07 14:27:33.940000', '2019-08-07 14:28:25.775000', '0', '4', '25.80', '很不错哦，哈哈哈', '2019080722273356', '22');

-- ----------------------------
-- Table structure for df_order_info
-- ----------------------------
DROP TABLE IF EXISTS `df_order_info`;
CREATE TABLE `df_order_info` (
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `order_id` varchar(128) NOT NULL,
  `pay_method` smallint(6) NOT NULL,
  `total_count` int(11) NOT NULL,
  `total_price` decimal(10,2) NOT NULL,
  `transit_price` decimal(10,2) NOT NULL,
  `order_status` smallint(6) NOT NULL,
  `trade_no` varchar(128) NOT NULL,
  `addr_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`order_id`),
  KEY `df_order_info_90ccbf41` (`addr_id`),
  KEY `df_order_info_e8701ad4` (`user_id`),
  CONSTRAINT `df_order_info_addr_id_5d4ae8f61135728_fk_df_address_id` FOREIGN KEY (`addr_id`) REFERENCES `df_address` (`id`),
  CONSTRAINT `df_order_info_user_id_50d6dc3bb3ad3df_fk_df_user_id` FOREIGN KEY (`user_id`) REFERENCES `df_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of df_order_info
-- ----------------------------
INSERT INTO `df_order_info` VALUES ('2019-08-07 05:12:20.656999', '2019-08-07 14:14:52.836000', '0', '2019080713122056', '3', '5', '173.40', '10.00', '5', '2019080722001492851000017601', '6', '56');
INSERT INTO `df_order_info` VALUES ('2019-08-07 05:29:04.167999', '2019-08-07 14:34:17.528000', '0', '2019080713290456', '3', '2', '36.00', '10.00', '5', '2019080722001492851000017600', '6', '56');
INSERT INTO `df_order_info` VALUES ('2019-08-07 12:48:37.216000', '2019-08-07 12:49:54.206000', '0', '2019080720483756', '3', '1', '25.00', '10.00', '4', '2019080722001492851000017602', '6', '56');
INSERT INTO `df_order_info` VALUES ('2019-08-07 14:27:33.930000', '2019-08-07 14:28:25.784000', '0', '2019080722273356', '3', '4', '103.20', '10.00', '5', '2019080722001492851000017603', '6', '56');

-- ----------------------------
-- Table structure for df_user
-- ----------------------------
DROP TABLE IF EXISTS `df_user`;
CREATE TABLE `df_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `is_delete` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=58 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of df_user
-- ----------------------------
INSERT INTO `df_user` VALUES ('50', 'pbkdf2_sha256$20000$laGEL4AZaIEm$WYd5H+LwRIPHTxKDId2aWtTUZccootuM4CheWrthepw=', null, '0', 'smart1', '', '', 'cxf819989150@163.com', '0', '0', '2019-07-26 08:32:22.069200', '2019-07-26 08:32:22.089200', '2019-07-26 08:32:22.142200', '0');
INSERT INTO `df_user` VALUES ('51', 'pbkdf2_sha256$20000$RDVbybaPBR1d$FRAXzvBfZdR9JLfWEW22hRTf1VTE+WDsv/zjQt7L7Kk=', null, '0', 'smart', '', '', 'cxf819989150@163.com', '0', '0', '2019-07-26 08:39:22.708200', '2019-07-26 08:39:22.735200', '2019-07-26 08:39:22.785200', '0');
INSERT INTO `df_user` VALUES ('52', 'pbkdf2_sha256$20000$tkM1CWQq8ivT$ovSO81Oo7Sm8uPG2aPSvoKZXib722MJm09zv20TME8A=', null, '0', 'smart3', '', '', 'cxf819989150@163.com', '0', '0', '2019-07-26 08:40:01.242200', '2019-07-26 08:40:01.259200', '2019-07-26 08:40:01.328200', '0');
INSERT INTO `df_user` VALUES ('53', 'pbkdf2_sha256$20000$rw83kNsErUx7$2CpTMGrK5S4Rx3dsMAF/WijsPc6A/0E+pOtALleGMOg=', null, '0', 'smart4', '', '', 'cxf819989150@163.com', '0', '0', '2019-07-26 09:06:43.382200', '2019-07-26 09:06:43.403200', '2019-07-26 09:06:43.527200', '0');
INSERT INTO `df_user` VALUES ('54', 'pbkdf2_sha256$20000$bj41J1Pek7fr$rHRaIyh1NMRCp2xdywXlY8RmsTGnexr/qPESsM5Ni9Y=', null, '0', 'smart5', '', '', 'cxf819989150@163.com', '0', '0', '2019-07-26 09:54:06.955200', '2019-07-26 09:54:06.974200', '2019-07-26 09:54:07.058200', '0');
INSERT INTO `df_user` VALUES ('55', 'pbkdf2_sha256$20000$m26BNC8gsUNK$rEcg/hs9Gt8y3pkukURYveAx7c8jl2gtWzG1J3RG46E=', null, '0', 'smart6', '', '', 'cxf819989150@163.com', '0', '0', '2019-07-26 09:56:11.702200', '2019-07-26 09:56:11.721200', '2019-07-26 09:56:11.799200', '0');
INSERT INTO `df_user` VALUES ('56', 'pbkdf2_sha256$20000$eD0CAxMGaiPT$weLKvn0kSn3XUX2grjL2cZi3JGmipSIuJGDggnAfiqQ=', '2019-08-05 15:14:35.638000', '0', 'smart7', '', '', 'cxf819989150@163.com', '0', '1', '2019-07-26 09:57:23.423200', '2019-07-26 09:57:23.444200', '2019-07-26 09:58:15.279200', '0');
INSERT INTO `df_user` VALUES ('57', 'pbkdf2_sha256$20000$9z80RvwnSFKZ$qyOuKnHYetkAbt7pzL7VKfGjSf99cjj4PXzBWOEEJMM=', '2019-08-06 13:56:24.902000', '1', 'admin', '', '', '123@qq.com', '1', '1', '2019-08-01 05:40:16.506600', '2019-08-01 05:40:16.545600', '2019-08-01 05:40:16.545600', '0');

-- ----------------------------
-- Table structure for df_user_groups
-- ----------------------------
DROP TABLE IF EXISTS `df_user_groups`;
CREATE TABLE `df_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `df_user_groups_group_id_32c3e17279c38f56_fk_auth_group_id` (`group_id`),
  CONSTRAINT `df_user_groups_group_id_32c3e17279c38f56_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `df_user_groups_user_id_39d5f100647ef339_fk_df_user_id` FOREIGN KEY (`user_id`) REFERENCES `df_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of df_user_groups
-- ----------------------------

-- ----------------------------
-- Table structure for df_user_user_permissions
-- ----------------------------
DROP TABLE IF EXISTS `df_user_user_permissions`;
CREATE TABLE `df_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `df_user_use_permission_id_120594ca54c454c2_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `df_user_use_permission_id_120594ca54c454c2_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `df_user_user_permissions_user_id_5714de6f24755481_fk_df_user_id` FOREIGN KEY (`user_id`) REFERENCES `df_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of df_user_user_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for django_admin_log
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `djang_content_type_id_337d6711b4b8a85e_fk_django_content_type_id` (`content_type_id`),
  KEY `django_admin_log_user_id_685f8f503de510f0_fk_df_user_id` (`user_id`),
  CONSTRAINT `djang_content_type_id_337d6711b4b8a85e_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_685f8f503de510f0_fk_df_user_id` FOREIGN KEY (`user_id`) REFERENCES `df_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=90 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_admin_log
-- ----------------------------
INSERT INTO `django_admin_log` VALUES ('1', '2019-08-01 05:42:08.377600', '1', '猪牛羊肉', '1', '', '8', '57');
INSERT INTO `django_admin_log` VALUES ('2', '2019-08-01 14:44:49.244000', '2', '新鲜水果', '1', '', '8', '57');
INSERT INTO `django_admin_log` VALUES ('3', '2019-08-01 14:45:31.714000', '3', '海鲜水产', '1', '', '8', '57');
INSERT INTO `django_admin_log` VALUES ('4', '2019-08-02 09:20:01.396000', '4', '禽类蛋品', '1', '', '8', '57');
INSERT INTO `django_admin_log` VALUES ('5', '2019-08-02 09:20:41.680000', '5', '新鲜蔬菜', '1', '', '8', '57');
INSERT INTO `django_admin_log` VALUES ('6', '2019-08-02 09:21:09.634000', '6', '速冻食品', '1', '', '8', '57');
INSERT INTO `django_admin_log` VALUES ('7', '2019-08-02 11:24:00.617000', '2', 'IndexPromotionBanner object', '2', '已修改 image 。', '14', '57');
INSERT INTO `django_admin_log` VALUES ('8', '2019-08-02 11:24:59.370000', '2', 'IndexPromotionBanner object', '2', '已修改 image 。', '14', '57');
INSERT INTO `django_admin_log` VALUES ('9', '2019-08-02 11:25:08.864000', '1', 'IndexPromotionBanner object', '2', '已修改 image 。', '14', '57');
INSERT INTO `django_admin_log` VALUES ('10', '2019-08-02 11:35:35.591000', '1', 'IndexPromotionBanner object', '2', '已修改 index 。', '14', '57');
INSERT INTO `django_admin_log` VALUES ('11', '2019-08-02 11:36:00.461000', '1', 'IndexPromotionBanner object', '2', '已修改 index 。', '14', '57');
INSERT INTO `django_admin_log` VALUES ('12', '2019-08-02 11:37:31.624000', '1', 'IndexPromotionBanner object', '2', '已修改 index 。', '14', '57');
INSERT INTO `django_admin_log` VALUES ('13', '2019-08-02 11:37:57.400000', '1', 'IndexPromotionBanner object', '2', '已修改 index 。', '14', '57');
INSERT INTO `django_admin_log` VALUES ('14', '2019-08-02 11:39:21.943000', '1', 'IndexPromotionBanner object', '2', '已修改 index 。', '14', '57');
INSERT INTO `django_admin_log` VALUES ('15', '2019-08-02 14:09:45.029000', '15', 'GoodsSKU object', '1', '', '9', '57');
INSERT INTO `django_admin_log` VALUES ('16', '2019-08-02 14:14:06.467000', '2', 'IndexGoodsBanner object', '1', '', '12', '57');
INSERT INTO `django_admin_log` VALUES ('17', '2019-08-02 14:23:11.776000', '7', '猪牛羊肉', '1', '', '8', '57');
INSERT INTO `django_admin_log` VALUES ('18', '2019-08-02 14:29:17.725000', '16', 'GoodsSKU object', '1', '', '9', '57');
INSERT INTO `django_admin_log` VALUES ('19', '2019-08-02 14:29:53.090000', '3', 'IndexGoodsBanner object', '1', '', '12', '57');
INSERT INTO `django_admin_log` VALUES ('20', '2019-08-02 14:33:53.610000', '17', 'GoodsSKU object', '1', '', '9', '57');
INSERT INTO `django_admin_log` VALUES ('21', '2019-08-02 14:36:45.906000', '18', 'GoodsSKU object', '1', '', '9', '57');
INSERT INTO `django_admin_log` VALUES ('22', '2019-08-02 14:39:18.892000', '4', 'IndexGoodsBanner object', '1', '', '12', '57');
INSERT INTO `django_admin_log` VALUES ('23', '2019-08-02 14:39:32.187000', '5', 'IndexGoodsBanner object', '1', '', '12', '57');
INSERT INTO `django_admin_log` VALUES ('24', '2019-08-02 14:41:47.827000', '2', 'IndexTypeGoodsBanner object', '1', '', '13', '57');
INSERT INTO `django_admin_log` VALUES ('25', '2019-08-02 14:44:26.947000', '3', 'IndexTypeGoodsBanner object', '1', '', '13', '57');
INSERT INTO `django_admin_log` VALUES ('26', '2019-08-02 14:47:50.651000', '19', 'GoodsSKU object', '1', '', '9', '57');
INSERT INTO `django_admin_log` VALUES ('27', '2019-08-02 14:53:04.358000', '20', 'GoodsSKU object', '1', '', '9', '57');
INSERT INTO `django_admin_log` VALUES ('28', '2019-08-02 14:54:45.270000', '4', 'IndexTypeGoodsBanner object', '1', '', '13', '57');
INSERT INTO `django_admin_log` VALUES ('29', '2019-08-02 14:55:56.033000', '5', 'IndexTypeGoodsBanner object', '1', '', '13', '57');
INSERT INTO `django_admin_log` VALUES ('30', '2019-08-02 14:57:48.172000', '21', 'GoodsSKU object', '1', '', '9', '57');
INSERT INTO `django_admin_log` VALUES ('31', '2019-08-02 14:58:45.377000', '22', 'GoodsSKU object', '1', '', '9', '57');
INSERT INTO `django_admin_log` VALUES ('32', '2019-08-02 14:59:30.870000', '6', 'IndexTypeGoodsBanner object', '1', '', '13', '57');
INSERT INTO `django_admin_log` VALUES ('33', '2019-08-02 14:59:41.119000', '7', 'IndexTypeGoodsBanner object', '1', '', '13', '57');
INSERT INTO `django_admin_log` VALUES ('34', '2019-08-02 14:59:51.398000', '8', 'IndexTypeGoodsBanner object', '1', '', '13', '57');
INSERT INTO `django_admin_log` VALUES ('35', '2019-08-02 15:08:42.351000', '1', 'GoodsImage object', '1', '', '11', '57');
INSERT INTO `django_admin_log` VALUES ('36', '2019-08-02 15:08:52.363000', '2', 'GoodsImage object', '1', '', '11', '57');
INSERT INTO `django_admin_log` VALUES ('37', '2019-08-02 15:09:09.818000', '3', 'GoodsImage object', '1', '', '11', '57');
INSERT INTO `django_admin_log` VALUES ('38', '2019-08-02 15:09:26.572000', '4', 'GoodsImage object', '1', '', '11', '57');
INSERT INTO `django_admin_log` VALUES ('39', '2019-08-02 15:18:33.711000', '23', 'GoodsSKU object', '2', '已修改 image 。', '9', '57');
INSERT INTO `django_admin_log` VALUES ('40', '2019-08-02 15:23:44.269000', '24', 'GoodsSKU object', '2', '已修改 image 。', '9', '57');
INSERT INTO `django_admin_log` VALUES ('41', '2019-08-02 15:29:20.798000', '5', 'GoodsImage object', '1', '', '11', '57');
INSERT INTO `django_admin_log` VALUES ('42', '2019-08-02 15:32:27.341000', '6', 'GoodsImage object', '1', '', '11', '57');
INSERT INTO `django_admin_log` VALUES ('43', '2019-08-02 15:35:02.882000', '7', 'GoodsImage object', '1', '', '11', '57');
INSERT INTO `django_admin_log` VALUES ('44', '2019-08-02 15:37:48.408000', '8', 'GoodsImage object', '1', '', '11', '57');
INSERT INTO `django_admin_log` VALUES ('45', '2019-08-02 15:38:10.728000', '25', 'GoodsSKU object', '2', '已修改 image 。', '9', '57');
INSERT INTO `django_admin_log` VALUES ('46', '2019-08-02 16:25:14.454000', '26', 'GoodsSKU object', '2', '已修改 image 。', '9', '57');
INSERT INTO `django_admin_log` VALUES ('47', '2019-08-02 16:27:56.402000', '27', 'GoodsSKU object', '2', '已修改 image 。', '9', '57');
INSERT INTO `django_admin_log` VALUES ('48', '2019-08-02 16:28:11.104000', '26', 'GoodsSKU object', '2', '已修改 image 。', '9', '57');
INSERT INTO `django_admin_log` VALUES ('49', '2019-08-02 16:30:03.754000', '9', 'GoodsImage object', '2', '已修改 image 。', '11', '57');
INSERT INTO `django_admin_log` VALUES ('50', '2019-08-02 16:32:03.898000', '10', 'GoodsImage object', '2', '已修改 image 。', '11', '57');
INSERT INTO `django_admin_log` VALUES ('51', '2019-08-02 16:35:56.909000', '11', 'GoodsImage object', '2', '已修改 image 。', '11', '57');
INSERT INTO `django_admin_log` VALUES ('52', '2019-08-02 16:36:06.433000', '12', 'GoodsImage object', '2', '已修改 image 。', '11', '57');
INSERT INTO `django_admin_log` VALUES ('53', '2019-08-02 16:36:26.073000', '28', 'GoodsSKU object', '2', '已修改 image 。', '9', '57');
INSERT INTO `django_admin_log` VALUES ('54', '2019-08-02 16:36:38.514000', '29', 'GoodsSKU object', '2', '已修改 image 。', '9', '57');
INSERT INTO `django_admin_log` VALUES ('55', '2019-08-03 04:27:18.718000', '30', 'GoodsSKU object', '2', '已修改 image 。', '9', '57');
INSERT INTO `django_admin_log` VALUES ('56', '2019-08-03 04:27:32.637000', '31', 'GoodsSKU object', '2', '已修改 image 。', '9', '57');
INSERT INTO `django_admin_log` VALUES ('57', '2019-08-03 04:27:43.973000', '32', 'GoodsSKU object', '2', '已修改 image 。', '9', '57');
INSERT INTO `django_admin_log` VALUES ('58', '2019-08-03 04:27:54.861000', '33', 'GoodsSKU object', '2', '已修改 image 。', '9', '57');
INSERT INTO `django_admin_log` VALUES ('59', '2019-08-03 04:28:42.119000', '13', 'GoodsImage object', '2', '已修改 image 。', '11', '57');
INSERT INTO `django_admin_log` VALUES ('60', '2019-08-03 04:28:53.376000', '14', 'GoodsImage object', '2', '已修改 image 。', '11', '57');
INSERT INTO `django_admin_log` VALUES ('61', '2019-08-03 04:29:04.457000', '15', 'GoodsImage object', '2', '已修改 image 。', '11', '57');
INSERT INTO `django_admin_log` VALUES ('62', '2019-08-03 04:29:15.170000', '16', 'GoodsImage object', '2', '已修改 image 。', '11', '57');
INSERT INTO `django_admin_log` VALUES ('63', '2019-08-03 04:43:52.546000', '17', 'GoodsImage object', '2', '已修改 image 。', '11', '57');
INSERT INTO `django_admin_log` VALUES ('64', '2019-08-03 04:44:05.722000', '18', 'GoodsImage object', '2', '已修改 image 。', '11', '57');
INSERT INTO `django_admin_log` VALUES ('65', '2019-08-03 04:44:19.843000', '19', 'GoodsImage object', '2', '已修改 image 。', '11', '57');
INSERT INTO `django_admin_log` VALUES ('66', '2019-08-03 04:44:29.220000', '20', 'GoodsImage object', '2', '已修改 image 。', '11', '57');
INSERT INTO `django_admin_log` VALUES ('67', '2019-08-03 04:45:00.791000', '34', 'GoodsSKU object', '2', '已修改 image 。', '9', '57');
INSERT INTO `django_admin_log` VALUES ('68', '2019-08-03 04:45:11.870000', '35', 'GoodsSKU object', '2', '已修改 image 。', '9', '57');
INSERT INTO `django_admin_log` VALUES ('69', '2019-08-03 04:45:24.353000', '36', 'GoodsSKU object', '2', '已修改 image 。', '9', '57');
INSERT INTO `django_admin_log` VALUES ('70', '2019-08-03 04:45:34.768000', '37', 'GoodsSKU object', '2', '已修改 image 。', '9', '57');
INSERT INTO `django_admin_log` VALUES ('71', '2019-08-03 04:45:59.216000', '38', 'GoodsSKU object', '2', '已修改 image 。', '9', '57');
INSERT INTO `django_admin_log` VALUES ('72', '2019-08-03 04:46:09.781000', '39', 'GoodsSKU object', '2', '已修改 image 。', '9', '57');
INSERT INTO `django_admin_log` VALUES ('73', '2019-08-03 04:46:21.432000', '40', 'GoodsSKU object', '2', '已修改 image 。', '9', '57');
INSERT INTO `django_admin_log` VALUES ('74', '2019-08-03 04:46:31.361000', '41', 'GoodsSKU object', '2', '已修改 image 。', '9', '57');
INSERT INTO `django_admin_log` VALUES ('75', '2019-08-03 04:46:57.536000', '21', 'GoodsImage object', '2', '已修改 image 。', '11', '57');
INSERT INTO `django_admin_log` VALUES ('76', '2019-08-03 04:47:06.195000', '22', 'GoodsImage object', '2', '已修改 image 。', '11', '57');
INSERT INTO `django_admin_log` VALUES ('77', '2019-08-03 04:47:16.493000', '23', 'GoodsImage object', '2', '已修改 image 。', '11', '57');
INSERT INTO `django_admin_log` VALUES ('78', '2019-08-03 04:47:26.776000', '24', 'GoodsImage object', '2', '已修改 image 。', '11', '57');
INSERT INTO `django_admin_log` VALUES ('79', '2019-08-03 04:48:03.532000', '24', 'GoodsImage object', '2', '已修改 image 。', '11', '57');
INSERT INTO `django_admin_log` VALUES ('80', '2019-08-03 04:48:30.770000', '24', 'GoodsImage object', '2', '已修改 image 。', '11', '57');
INSERT INTO `django_admin_log` VALUES ('81', '2019-08-03 05:43:03.776000', '15', 'GoodsSKU object', '2', '已修改 image 。', '9', '57');
INSERT INTO `django_admin_log` VALUES ('82', '2019-08-03 05:50:48.746000', '15', 'GoodsSKU object', '2', '已修改 image 。', '9', '57');
INSERT INTO `django_admin_log` VALUES ('83', '2019-08-03 05:51:05.196000', '14', 'GoodsSKU object', '2', '已修改 image 。', '9', '57');
INSERT INTO `django_admin_log` VALUES ('84', '2019-08-03 06:31:45.126000', '4', 'IndexGoodsBanner object', '2', '已修改 image 。', '12', '57');
INSERT INTO `django_admin_log` VALUES ('85', '2019-08-03 06:31:54.871000', '5', 'IndexGoodsBanner object', '2', '已修改 image 。', '12', '57');
INSERT INTO `django_admin_log` VALUES ('86', '2019-08-03 06:37:33.732000', '4', 'IndexGoodsBanner object', '2', '已修改 image 。', '12', '57');
INSERT INTO `django_admin_log` VALUES ('87', '2019-08-03 06:37:41.980000', '5', 'IndexGoodsBanner object', '2', '已修改 image 。', '12', '57');
INSERT INTO `django_admin_log` VALUES ('88', '2019-08-03 08:22:17.887000', '13', 'GoodsSKU object', '2', '已修改 image 。', '9', '57');
INSERT INTO `django_admin_log` VALUES ('89', '2019-08-03 11:46:53.448000', '12', 'GoodsSKU object', '2', '已修改 image 。', '9', '57');

-- ----------------------------
-- Table structure for django_content_type
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_43790f3e29083e14_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES ('1', 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES ('3', 'auth', 'group');
INSERT INTO `django_content_type` VALUES ('2', 'auth', 'permission');
INSERT INTO `django_content_type` VALUES ('4', 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES ('10', 'goods', 'goods');
INSERT INTO `django_content_type` VALUES ('11', 'goods', 'goodsimage');
INSERT INTO `django_content_type` VALUES ('9', 'goods', 'goodssku');
INSERT INTO `django_content_type` VALUES ('8', 'goods', 'goodstype');
INSERT INTO `django_content_type` VALUES ('12', 'goods', 'indexgoodsbanner');
INSERT INTO `django_content_type` VALUES ('14', 'goods', 'indexpromotionbanner');
INSERT INTO `django_content_type` VALUES ('13', 'goods', 'indextypegoodsbanner');
INSERT INTO `django_content_type` VALUES ('16', 'order', 'ordergoods');
INSERT INTO `django_content_type` VALUES ('15', 'order', 'orderinfo');
INSERT INTO `django_content_type` VALUES ('5', 'sessions', 'session');
INSERT INTO `django_content_type` VALUES ('7', 'user', 'address');
INSERT INTO `django_content_type` VALUES ('6', 'user', 'user');

-- ----------------------------
-- Table structure for django_migrations
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES ('1', 'contenttypes', '0001_initial', '2019-07-23 15:59:50.993205');
INSERT INTO `django_migrations` VALUES ('2', 'contenttypes', '0002_remove_content_type_name', '2019-07-23 15:59:51.823205');
INSERT INTO `django_migrations` VALUES ('3', 'auth', '0001_initial', '2019-07-23 15:59:54.260205');
INSERT INTO `django_migrations` VALUES ('4', 'auth', '0002_alter_permission_name_max_length', '2019-07-23 15:59:54.774205');
INSERT INTO `django_migrations` VALUES ('5', 'auth', '0003_alter_user_email_max_length', '2019-07-23 15:59:54.820205');
INSERT INTO `django_migrations` VALUES ('6', 'auth', '0004_alter_user_username_opts', '2019-07-23 15:59:54.898205');
INSERT INTO `django_migrations` VALUES ('7', 'auth', '0005_alter_user_last_login_null', '2019-07-23 15:59:54.959205');
INSERT INTO `django_migrations` VALUES ('8', 'auth', '0006_require_contenttypes_0002', '2019-07-23 15:59:54.993205');
INSERT INTO `django_migrations` VALUES ('9', 'user', '0001_initial', '2019-07-23 15:59:58.271205');
INSERT INTO `django_migrations` VALUES ('10', 'admin', '0001_initial', '2019-07-23 15:59:59.891205');
INSERT INTO `django_migrations` VALUES ('11', 'goods', '0001_initial', '2019-07-23 16:00:06.850205');
INSERT INTO `django_migrations` VALUES ('12', 'order', '0001_initial', '2019-07-23 16:00:07.337205');
INSERT INTO `django_migrations` VALUES ('13', 'order', '0002_auto_20171113_1813', '2019-07-23 16:00:12.621205');
INSERT INTO `django_migrations` VALUES ('14', 'sessions', '0001_initial', '2019-07-23 16:00:12.978205');
INSERT INTO `django_migrations` VALUES ('15', 'order', '0002_auto_20190806_1919', '2019-08-06 11:21:08.317000');

-- ----------------------------
-- Table structure for django_session
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_session
-- ----------------------------
