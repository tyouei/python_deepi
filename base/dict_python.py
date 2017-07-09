#/usr/bin/python
#-----------coding:utf8------------------
#字典

#create dic
dict_1 = {'name':'zhangsan','age':23,'sex':'man'}
print dict_1

#判断字典的是否有该键存在
#has_key()
print dict_1.has_key("name")

#keys()返回的是字典的键的列表
print dict_1.keys()

#values()返回的是字典的值的列表
print dict_1.values()

#upadte():两个字典的合并
dict_2 = {'class':'3-103'}
dict_1.update(dict_2)
print dict_1

#del ,clear ,pop 删除字典
#删除指定的元素
del dict_1['class']
print dict_1
#清空所有元素
#dict_2.clear()
dict_2.pop('class')
print dict_2.has_key('class')

#从字典中获取指定的值
print dict_1.get('name')

#dict 循环遍历
#for in
print "for in----------------------"
for i in dict_1:
	print "dict_1[%s]=" % i,dict_1[i]

#items
print "##items---------------------"
for (k,v) in dict_1.items():
	print "dict_1[%s]=" % k,v

#iteritems
print "iteritems----------------------"
for k,v in dict_1.iteritems():
	print "dict_1[%s]=" % k,v
