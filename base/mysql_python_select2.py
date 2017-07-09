#!/usr/bin/python
# -*- coding: UTF-8 -*-
import MySQLdb

# db connect
db = MySQLdb.connect("127.0.01","root","password","employees" )

# db get cursor
cursor = db.cursor()

# select 
sql = "SELECT name,age,sex FROM emptest1" 

try:
   # exe sql
   cursor.execute(sql)
   # get record 
   results = cursor.fetchall()
   for row in results:
      name = row[0]
      age = row[1]
      sex = row[2]
      #print 
      print "name=%s,age=%d,sex=%s" % \
             (name, age, sex )
except:
      print "Error: unable to fecth data"

#db close
db.close()