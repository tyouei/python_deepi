#!/usr/bin/python
# --------utf-8--------------

#capitalize()

def  print_cap(str):
	print str.capitalize();
    
#call print_cap

print_cap("this is test!")

#center()

def print_center(vstr,vlength,vchar):
	print vstr.center(vlength,vchar);

#call center
print_center("I",10,"o")

#count()

def print_count(vstr,vsub,vstart,vend):
	print vstr.count(vsub,vstart,vend);
#call print_count
print_count("this is test program","t",1,20);

#decode

def print_decode(vstr,vencode,verror):
	print vstr.decode(vencode,verror);
#call print_decode
print_decode("this is utf-8","utf-8","strict")

#endswith()

def pritn_endswith(vstr,vsuffin,vstart,vend):
	print vstr.endswith(vsuffin,vstart,vend);

pritn_endswith("this is OK !!","OK",2,10);

#expandtabs(tabsize=8)
def print_tabs(vstr,vsize):
	print vstr.expandtabs(vsize);

#call expandtabs()
print_tabs("is a tab 	",8)

#find(str,start,end)
def print_find(vstr,vfindstr,vstart,vend):
	print vstr.find(vfindstr,vstart,vend);
#call find
print_find("this is a find function","find",1,20)






