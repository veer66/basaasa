# CocoaMySQL dump
# Version 0.7b5
# http://cocoamysql.sourceforge.net
#
# Host: 127.0.0.1 (MySQL 5.0.37)
# Database: zooid
# Generation Time: 2007-06-12 14:53:07 +0200
# ************************************************************

# Dump of table zooid_articles
# ------------------------------------------------------------

CREATE TABLE `zooid_articles` (
  `id` int(11) NOT NULL auto_increment,
  `title` varchar(255) NOT NULL,
  `body` longtext,
  `progressive` tinyint(1) NOT NULL default '0',
  `need_checking` tinyint(1) NOT NULL default '0',
  `deleted` tinyint(4) default '0',
  PRIMARY KEY  (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=20 DEFAULT CHARSET=utf8;



# Dump of table zooid_comments
# ------------------------------------------------------------

CREATE TABLE `zooid_comments` (
  `id` int(11) NOT NULL auto_increment,
  `article_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `comment` longtext NOT NULL,
  `timestamp` int(11) NOT NULL default '0',
  PRIMARY KEY  (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;



# Dump of table zooid_groups
# ------------------------------------------------------------

CREATE TABLE `zooid_groups` (
  `id` int(11) NOT NULL auto_increment,
  `name` varchar(128) default NULL,
  PRIMARY KEY  (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;



# Dump of table zooid_reservations
# ------------------------------------------------------------

CREATE TABLE `zooid_reservations` (
  `id` int(11) NOT NULL auto_increment,
  `user_id` int(11) NOT NULL,
  `article_id` int(11) NOT NULL,
  `expected_submission_date` date default NULL,
  PRIMARY KEY  (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=18 DEFAULT CHARSET=utf8;



# Dump of table zooid_translations
# ------------------------------------------------------------

CREATE TABLE `zooid_translations` (
  `id` int(11) NOT NULL auto_increment,
  `body` longtext,
  `revision` int(11) NOT NULL default '1',
  `article_id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=78 DEFAULT CHARSET=utf8;



# Dump of table zooid_users
# ------------------------------------------------------------

CREATE TABLE `zooid_users` (
  `id` int(11) NOT NULL auto_increment,
  `username` varchar(255) NOT NULL,
  `password` varchar(32) NOT NULL,
  `first_name` varchar(255) NOT NULL,
  `last_name` varchar(255) NOT NULL,
  `group_id` int(11) NOT NULL,
  `email` varchar(255) default NULL,
  PRIMARY KEY  (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;



