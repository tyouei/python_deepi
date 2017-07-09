#/usr/bin/python
#------------coding:UTF-8------------------
# date leraning

#import time
import time
# time.time()
print time.time()

#  print location time
print time.localtime(time.time())

# format date
print time.strftime('%Y-%m-%d:%H%M%S-%A-%B',time.localtime(time.time()))

#import datetime
import datetime

now = datetime.datetime.now()

print now

#前一个小时
d1 = now-datetime.timedelta(hours=1)
print d1.strftime("%Y%m%d:%H-%M-%S")

#前一天
d2 = now-datetime.timedelta(days=1)
print d2.strftime("%Y%m%d:%H-%M-%S")

#上周日
d3 = now-datetime.timedelta(days=now.isoweekday())
print d3.strftime("%Y%m%d:%H-%M-%S"),"",d3.isoweekday()

#上周一
d31 = d3-datetime.timedelta(days=6)
print d31.strftime("%Y%m%d:%H-%M-%S"),"",d31.isoweekday()

#前一个月最后一天
print "now days :%d" % now.day
d4 = now-datetime.timedelta(days=now.day)
print d4.strftime("%Y%m%d %H%M%S")

#前一个月第一天
print datetime.datetime(d4.year,d4.month,2)
