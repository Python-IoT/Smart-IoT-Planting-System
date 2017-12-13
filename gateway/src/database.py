#!/usr/bin/env python
import sqlite3
#Using sqlite to store the data of devices.
#os.system('./db_init.sql') #create database and init the tables
def create_db():
  con = sqlite3.connect('gw.db')
  print(con)
