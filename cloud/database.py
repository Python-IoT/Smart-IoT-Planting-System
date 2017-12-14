#!/usr/bin/env python
import pymysql  #Python3
 
db = pymysql.connect("localhost","sips","root","zaijian" )
cursor = db.cursor()
cursor.execute("SELECT VERSION()")
data = cursor.fetchone()
 
print ("Database version : %s " % data)
db.close()

def create_table():
 db = pymysql.connect("localhost","sips","root","zaijian" )
  cursor = db.cursor()
  cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
  sql = """CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,  
         SEX CHAR(1),
         INCOME FLOAT )"""

  cursor.execute(sql)
  db.close()
