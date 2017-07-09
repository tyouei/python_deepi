#!/usr/bin/python
#------------uft8---------------------------
#------------mysql--------------------------
import MySQLdb

#open db connection
db=MySQLdb.connect("127.0.0.1","root","password","employees");

# get db cursor
cursor=db.cursor();

#exe SQL
cursor.execute("select version()");

# fetchone() record date
data = cursor.fetchone();

print "Database version:%s" % data;

#close db
db.close();