#!/usr/bin/python
# this is test
# print "hello world!"

#list test program 

list1=["123","abc","456","edfg"]
print list1
print list1[0]
print list1[-1]
print list1[-2:-1]
print len(list1)

#data type converslon

print long(len(list1))
print hex(len(list1))
print oct(len(list1))

#arithmetic operation
# + - * /

a=2
b=3
c=0
c=2+3
print "a+b=",c
c=3-2
print "b-c=",c
c=2*3
print "a*b=",c
c=3/2
print "b/c=",c
c=2%3
print "2%3=",c 
c=2^3
print c

c=2**3
print c

# & | ^ ~

a=60    #0011 1100
b=13	#0000 1101
c=0

c=a&b;
print "a&b=",c

c=a|b;
print "a|b=",c

c=a^b;
print "a^b=",c

c=~a
print "~a=",c

c=a<<2
print "a<<2",c

c=a>>2
print "a>>2",c

#logic operation
# and or not

a=10
b=20
c=0

c=a and b
if c:
	print "a and b = true"
else:
	print "a and b = flase"

#edit a 
print "a=0"
a=0
if (a and b):
	print "a and b =true"
else:
	print "a and b =false"

if (a or b):
	print "a or b =true"
else:
	print "a or b =false"

if (not a):
   print "true"
else:
   print "false"

if not(not b):
	print "false"
else:
	print "true"

#------------member operation---------
# in  / not in

list_member=["abc","wang ","zhang","john"]

if("abc" in list_member):
	print "abc in list_member"
else:
	print "abc not in list_member"


if ("edfg" not in list_member):
	print "edfg not in list_member"
else:
	print "edfg in list_member"

#-------------identity operation--------
# is / not is
a=20
b=20

print "a=",a
print "b=",b

if (a is b):
	print "a=b"
else:
	print "a<>b"

c=30

print "c=",c
if (a is not c):
	print "a is not c"
else:
	print "a is c "

#-----------------while------------------
numbers=[1,2,3,4,5,6,7]
even=[]
old=[]

while len(numbers)>0:
	idx=numbers.pop()
	if (idx%2):
		even.append(idx)
	else:
		old.append(idx)
print "even=",even
print "old=",old

#-----------------for loop ---------------
for letter in 'python':
	if (letter=="h"):
		pass
	print ">>>>",letter
print "good bye!"

list1 =["apple","orage","mango","banana"]
for idex in list1:
	print idex











