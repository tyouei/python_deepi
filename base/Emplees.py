#!/usr/bin/python
#--------------utf-8------------------------
class Emplees():
	"""docstring for Emplees"""

	"Emplees count"
	empCount=0;

	def __init__(self,name,age):
		#super(Emplee#s, self).__init__()
		self.age = age;
		self.name=name;
		Emplees.empCount+=1;

		#private property
		self.__privateName="this is private name";
		#protected property
		self._proNmae="this is protected property"

	def print_empcount(self):
		print "Total Emplee:",Emplees.empCount;

	def print_self(self):
		print "Emplee name:",self.name;
		print "Emplee age:%d" % self.age;

 
emp=Emplees("John LI ",18);

emp.print_empcount();
emp.print_self();

# print inner class property
print "Emplees.__doc__:",Emplees.__doc__
print "Emplees.__name__:",Emplees.__name__
print "Emplees.__module__:",Emplees.__module__
print "Emplees.__bases__:",Emplees.__bases__
print "Emplees.__dict__:",Emplees.__dict__

import MySQLdb
