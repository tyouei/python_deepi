#/usr/bin/python
#----------coding:utf8-------------------
#字符串

# 字符串的连接
# join

a = ['1','2','3']
b = ''
print b.join(a)
#使用占位符
print '%s%s%s' % tuple(a)

#字符串的截取
#----从左右截取
str = 'ilovepython'
print str[0]
print str[1:5]
#----从右到左
print str[-1]
print str[-5:-1]
#字符串替换
# 使用replace
b = str.replace('python','you')
print b
#使用正则表达式
import re
strinf = re.compile('python')
b = strinf.sub('you',str)
print b

# 字符串比较
str1 = 'str1'
str2 = 'str2'
# 不相等：-1
print cmp(str1,str2)
str3 = 'str1'
# 相等：0
print cmp(str1,str3)
# 字符串相加
print str1 + str2

#字符串查找,找到返回相应的位置
#方法1：find()
info ='abcdefg'
# 返回：0
print info.find('a')
# 返回：1
print info.find('b')
#方法2：index()
print info.index('a')
print info.index('abcdefg')
print info.index('cde')

#字符串的分割
info = 'name:age:sex,python:html:css'
print info.split(':')

#字符串的翻转
#[::-1]
print info[::-1]

#字符串编码
#decode ,encode
print info.decode('utf-8').encode('gbk')
#字符串format
m='you'
str = "i love {python}".format(python=m)
print str

# 字符串的长度
print len(info)

#字符串的大小写
print info.upper()

print info.upper().lower().capitalize()

#字符串去空格
#strip ,lstrip,rstrip
info=" abcdefg "
print info.strip()
