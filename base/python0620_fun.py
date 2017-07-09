#!/usr/bin/python
#----------UTF8-------------

# def function():
#	pass
#  return [expression] 

def print_name(vname):
	print vname;
	return;
# call print_name
#print_name("this is a function");

#change object
def no_chg_obj(vint):
	vint=10;
	print vint;

#call no_chg_obj
int1=5
no_chg_obj(int1)

#chagne object
def chg_obj(vlist):
	vlist.append([1,2,3,4,5]);
	print vlist;
	return

#change list
vlist=[10,20,30,40]
chg_obj(vlist);
print vlist;

# takes exactly 1 argument
def takes_arg(str):
	print str;
	return;
takes_arg("takes argument test!!");

# keyword argument
def keyword_agr(name,age):
	print "name=",name;
	print "age=",age
	return
#call keyword_agr
keyword_agr(age=30,name="zhang");
#default argument
def def_arg(name,age=25):
 	print "name=",name;
 	print "age=",age;
 	return
#call default argument
def_arg("age is default");
def_arg("age is setting",40);

#var length argument
def printinfo(arg1,*vartuple):

	print arg1;
	for var in vartuple:
		print var;
	return;

#call printinfo()
printinfo(10);
printinfo(10,20,30,40);

#anonymous funciton
sum =lambda arg1,arg2:arg1+arg2;
print "sum=",sum(10,20);

# test is a module
#from test_mod import add
import test_mod
print "test_mod.add=",test_mod.add(50,50);

#import test_mod

# call test.mod.sum()
#print "test_mod.sum=",test_mod.sum(10,30);

#dir()
import math

print dir(math);



