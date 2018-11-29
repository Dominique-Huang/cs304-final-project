--
-- Current Database: `loft`
--
use `loft`;

/* Create tables for user and properties */

drop table if exists users;
drop table if exists properties;

create table users(
    `name` varchar(20) DEFAULT NULL,
    `email` varchar(30) DEFAULT NULL,
    `pw` varchar(60) DEFAULT NULL,
    `university` varchar(40) DEFAULT NULL,
    `UID` int(15) unsigned unsigned NOT NULL AUTO_INCREMENT,
    PRIMARY KEY (`UID`)
);

create table tenants(
    smoker bit DEFAULT 0, /*1 if smoker, 0 if not*/
    gender int(1) DEFAULT 0, /*1 for female, 2 for male, 3 for other*/
    pet bit DEFAULT 0, /*1 if has pet, 0 if not*/
) INHERITS (users);

create table properties(
    /* how do we want to display features, gender, availability? */
    `propName` varchar(30) DEFAULT NULL,
    `propDescrip` varchar(150) DEFAULT NULL,
    `propLocation` varchar(150) DEFAULT NULL,
    `propPrice` int(10) unsigned DEFAULT NULL,
    `propSmoker` bit DEFAULT 0, /*1 if okay with smoker, 0 if not*/
    `propGender` int(1) DEFAULT 0, /*1 if female only, 2 if male only, 3 if no preference*/
    `propPet` bit DEFAULT 0, /*1 if okay with pet, 0 if not*/
    `PID` int(10) unsigned NOT NULL AUTO_INCREMENT,
    PRIMARY KEY (`PID`)
);

create table dates(
    `PID` int(10),
    startDate date,
    endDate date,
    foreign key (`PID`) references properties(`PID`)
) ENGINE = InnoDB;

create table featuresTenants(
    `UID` int(10),
    features varchar(100),
    foreign key (`UID`) references tenants(`UID`)
) ENGINE = InnoDB;

create table featuresProperties(
    `PID` int(10),
    features varchar(100),
    foreign key (`PID`) references properties(`PID`)
) ENGINE = InnoDB;

/* Map relationships*/

-- table to map one to many relationship of hosts and properties
drop table if exists host_prop;
create table host_prop(
    UID int,
    PID int,
    primary key (UID, PID)
);

INSERT INTO `users` VALUES ('Freddie(host)','Boston University',1), ('Freddie2(not host)','Massachusetts Institute of Technology',2);
INSERT INTO `properties` VALUES ('1 BR near Kendall','Single bedroom in apartment near Kendall Square','Kendall Square, Cambridge','1000',1), ('3 BR apartment near Central','Entire apartment include 3 BR located in Central','Central Square, Cambridge','4000',2);
INSERT INTO `host_prop` VALUES (1,1), (1, 2);