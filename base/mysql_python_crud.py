#!/usr/bin/python
#------utf-8----------------
import MySQLdb

#open db connect
db_con=MySQLdb.connect("127.0.0.1","root","password","employees");

# get db cursor 
cursor=db_con.cursor();

# drop table if exiting
#cursor.execute("drop table if exists emptest1")
# create emptest1
#sql="""create table emptest1 (
#		name char(20) NOT NULL,
#		age int,
#		sex char(1))"""

# insert db
sql=""" insert into emptest1 (name,age,sex)
		values("testuser1","18","1")""";
try:
	cursor.execute(sql);
	db_con.commit();
except:
	db_con.rollback();
finally:
	pass


#close db connect
db_con.close();