#/usr/bin/python
#----------------utf8------------------------------
# import Tkinter
from Tkinter import *

#create winows 
root = Tk()

#create list 
li = ['c','python','php','html','sql','java']
movie = ['css','jqurey','Bootstrap']
#create listbox
listb = Listbox(root)
listb2 = Listbox(root)

# insert data to listb
for item in li:
	listb.insert(0,item)

for item in movie:
	listb2.insert(0,item)

listb.pack()
listb2.pack()
root.mainloop()