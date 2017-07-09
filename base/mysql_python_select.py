#!/usr/bin/python
#-----------utf-8---------------------
#import mysqldb
import MySQLdb
# db connect
db_con = MySQLdb.connect("127.0.0.1","root","password","employees")
#db cursor
cursor = db_con.cursor()
#sql
sql = "SELECT name,age,sex FROM emptest1 "

try:
	#exe SQL
    cursor.execute(sql)

    res = cursor.fetchall()
    for row in res:
    	vname=row[0]
    	vage=row[1] 
    	vsex=row[2]
    	#print results
    	print "name=%s,age=%d,sex=%s" % (vname,vage,vsex)
except:
	print "error:unabe to fecth data"

#close db_con
db_con.close();