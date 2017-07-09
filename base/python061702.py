#!/usr/bin/python
import math #This will import math module

#abs
print "abs(-45):",abs(-45)
#fabs
print "math.fabs(-45):",math.fabs(-45)
#ceil 
print "ceil(-45.01):",math.ceil(-45.01)
print "ceil(100.12):",math.ceil(100.01)
print "ceil(119L):",math.ceil(119L)
print "cell(math.pi)",math.ceil(math.pi)
#cmp(x,y)
#x==y:0
#x<y:-1
#x>y:1
print "cmp(1,2):",cmp(1,2)
print "cmp(2.2):",cmp(2,2)
print "cmp(2,1):",cmp(2,1)

#math.exp(x)
print "math.exp(8):",math.exp(8)

#math.floor(x)
print "math.floor(-45.16):",math.floor(-45.16)

#math.log(x)
print "math.log(8):",math.log(8)
#math.log10(x)
print "math.log10(8):",math.log10(8)
#max(x,y,z,:::)
print "max(1,2,3,45,5,7):",max(1,2,3,45,5,7)
#min(x,y,z,:::::)
print "min(1,2,3,45,5,7):",min(1,2,3,45,5,7)
#math.modf(x)
print "math.modf(100.12",math.modf(100.12)
#math.pow(x,y)
print "math.pow(2,3)",math.pow(2,3)
#round(x,y)
print "round(80.1234,2)",round(80.1234,2)
print "round(80.1234,2)",round(80.1234)
#math.sqrt(x)
print "math.sqrt(4)",math.sqrt(4)

#import random
import random
#number
print "random.choice([1,2,3,45,6])",random.choice([1,2,3,45,6])
#string
print "random.choice('abcdefg')",random.choice('abcdefg')
#random.randrange(x,y,z)
print "randrange(100,1000,2)",random.randrange(100,1000,2)
#random.randmon() from 0 to 1
print "random.random()",random.random();
#random.seed()
random.seed(10)
print "random.random",random.random();
#random.uniform(5,10)
print "random.uniform(5,10)",random.uniform(5,10)

print "My name is %s and age is %d !"%('zhang',38)




