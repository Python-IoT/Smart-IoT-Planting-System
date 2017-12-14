#!/usr/bin/env python
import pymysql  #Python3
 
db = pymysql.connect("localhost","sips","root","zaijian" )
cursor = db.cursor()
cursor.execute("SELECT VERSION()")
data = cursor.fetchone()
 
print ("Database version : %s " % data)
db.close()
