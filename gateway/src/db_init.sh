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
