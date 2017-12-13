#!/usr/bin/env python
import sqlite3
#Using sqlite to store the data of devices.
#os.system('./db_init.sql') #create database and init the tables

#ID    LIGHT    PUMP      ANGLE    ALARM        PHONE
#1    On/OFF    Run/Stop  45/90    Open/Close   13880002222
def create_db():
  con = sqlite3.connect('gw.db')
  print(con)
  
def create_table():
  con = sqlite3.connect('gw.db')
  c = con.cursor()
  sql_str = '''CREATE TABLE DEVICE(
  ID INTEGER PRIMARY KEY    NOT NULL,
  NAME      TEXT,
  INFO      TEXT,
  LIGHT     INTEGER,
  TEMP      REAL,
  HUM       REAL,
  ALARM     INTEGER
  );
  '''
  c.execute(sql_str)
  con.commit()
  con.close()
  
def insert_data():
  con = sqlite3.connect('gw.db')
  c = con.cursor()
  sql_str = "INSERT INTO DEVICE VALUES (2, 'soybean','greenhouse for soybean' , 1,28.5,45, 0 );"
  c.execute(sql_str)
  con.commit()
  con.close()
