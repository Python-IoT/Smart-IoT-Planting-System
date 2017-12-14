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
  
def db_insert():
  db = pymysql.connect("localhost","sips","root","zaijian" )
  cursor = db.cursor()
  sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""

  try:
    cursor.execute(sql)
    db.commit()
  except:
    db.rollback()
  db.close()
