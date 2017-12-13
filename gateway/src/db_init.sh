#!/bin/sh
#create database
sqlite3 gw.db
.databases
.quit

#create table
CREATE TABLE DEVICE(
ID INTEGER PRIMARY KEY    NOT NULL,
NAME      TEXT,    
INFO      TEXT,
LIGHT     INTEGER,     
TEMP      REAL,
  HUM		 REAL
);

.tables
#modify table
ALTER TABLE DEVICE ADD COLUMN ALARM INTERGER;

#insert data
INSERT INTO DEVICE(ID,NAME,INFO,LIGHT,ALARM)
VALUES (1, 'corn','number 1 greenhouse for corn' , 1, 0 );

.headers on 
.mode column

#modify data
UPDATE DEVICE SET LIGHT = 0 WHERE ID = 2;

#delete data
DELETE FROM DEVICE WHERE ID = 1;
