# -*- coding: utf-8 -*-
#在列表中选择
data = [1,5,-3,-8,7,6,-5,10]
res = []
for x in data:
    if x>=0:
        res.append(x)
print res
import timeit
from random import randint
data = [randint(-10,10) for _ in xrange(10)]
print data
a = filter(lambda x:x>=0,data)
print a

#列表解析
b = [x for x in data if x>=0]
print b

#在字典中选择
d = {x:randint(60,100) for x in xrange(1,21)}
print d
s = {k:v for k,v in d.iteritems() if v>90}
print s

#集合解析
data = [1,5,-3,-8,7,6,-5,12]
s = set(data)
print s
d = { x for x in s if x%3==0}
print d