--
-- Current Database: `loft`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `loft` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `loft`;

/* Create tables for user and properties */

drop table if exists tenants;
drop table if exists users;
drop table if exists properties;
drop table if exists dates;
drop table if exists featuresTenants;
drop table if exists featuresProperties;

create table users(
    `name` varchar(20) DEFAULT NULL,
    `email` varchar(30) DEFAULT NULL,
    `pw` varchar(60) DEFAULT NULL,
    `university` varchar(40) DEFAULT NULL,
    UID int(15) unsigned NOT NULL AUTO_INCREMENT,
    PRIMARY KEY (UID)
);

create table tenants(
    smoker bit DEFAULT 0, /*1 if smoker, 0 if not*/
    gender int(1) DEFAULT 0, /*1 for female, 2 for male, 3 for other*/
    pet bit DEFAULT 0, /*1 if has pet, 0 if not*/
    UID int(15) unsigned,
    foreign key (UID) references users(UID) on delete cascade on update cascade
)
ENGINE = InnoDB;

create table properties(
  -- add in description
    /* how do we want to display features, gender, availability? */
    `propName` varchar(100) DEFAULT NULL,
    `propDescription` varchar(100) DEFAULT NULL,
    `propLocation` varchar(150) DEFAULT NULL,
    `propPrice` int(10) unsigned DEFAULT NULL,
    `propSmoker` int(1) DEFAULT NULL, /*1 if okay with smoker, 0 if not*/
    `propGender` int(1) DEFAULT NULL, /*1 if female only, 2 if male only, 3 if no preference*/
    `propPet` int(1) DEFAULT NULL, /*1 if okay with pet, 0 if not*/
    `PID` int(10) unsigned NOT NULL AUTO_INCREMENT,
    PRIMARY KEY (PID)
);

create table dates(
    PID int(10),
    startDate date,
    endDate date
);

create table featuresTenants(
    UID int(10),
    features varchar(100)
);

create table featuresProperties(
    PID int(10),
    features varchar(100)
);

/* Map relationships*/

-- table to map one to many relationship of hosts and properties
drop table if exists host_prop;
create table host_prop(
    UID int,
    PID int,
    primary key (UID, PID)
);

INSERT INTO users VALUES ('Freddie', 'freddie@bu.edu', 'password','Boston University',1), ('Mary','mary@mit.edu', 'password','Massachusetts Institute of Technology', NULL);
INSERT INTO tenants VALUES (0, 2, 0, 1);
INSERT INTO properties VALUES ('Studio apartment', 'Cozy studio with natural lighting', 'Central Square', 1000, 0, 3, 1, NULL), ('2BR Apartment', 'Charming retreat by Newbury street', 'Boston', 1700, 0, 3, 0, NULL), ('1 BR near Kendall','Single bedroom in apartment near Kendall Square','Kendall Square, Cambridge','1200', 1, 2, 1, NULL);
-- INSERT INTO `properties` VALUES ('1 BR near Kendall','Single bedroom in apartment near Kendall Square','Kendall Square, Cambridge','1000',1), ('3 BR apartment near Central','Entire apartment include 3 BR located in Central','Central Square, Cambridge','4000',2);
-- INSERT INTO `host_prop` VALUES (1,1), (1, 2);
