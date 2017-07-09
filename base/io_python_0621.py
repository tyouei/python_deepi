#!/usr/bin/python
#---------------utf-8----------------

# file I/O 

#raw_input()

#str=raw_input();
#print str;

#input()
#str=input();
#print "input:",str;

# file()
# file open
fo=open("foo.txt",'ab',0);
print fo.name;
print fo.mode;
# file write
fo.write("hello file IO!!");
# file close
fo.close();

#file open
try:
	foo=open("foo1.txt",'rb',0);
except Exception, e:
	print "foo1.txt is not exiting"
else:
	#file read
	rw_input=foo.read(3);
	print rw_input;
	position=foo.tell();
	print position;
	foo.close();
	print foo.closed;
finally:
	pass;

#file name
import os;
os.rename("foo.txt","foo2.txt");
#file copy
import shutil 
shutil.copy("foo2.txt","foo.txt");

#Fiel delete
os.remove("foo2.txt");


