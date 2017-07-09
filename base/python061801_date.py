#!/usr/bin/python
# ------coding:UTF8--------
import time; #this wil  import time module;

print "system date:",time.time();

print "local time",time.localtime(time.time())

print "formart lcoal time:",time.asctime(time.localtime(time.time()))

print "formrt:yyyy-mm-dd:",time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())

print "formrt:yyyymmdd:",time.strftime("%Y%m%d %H:%M:%S",time.localtime())

#calendar
import calendar

cal = calendar.month(2017,6)

print "2016year6month calendar:"
print cal
