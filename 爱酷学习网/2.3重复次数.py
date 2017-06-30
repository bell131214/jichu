# -*- coding: utf-8 -*-
from random import randint
data = [randint(0,20) for _ in xrange(30)]
print data
#统计最终的结果应该是字典 c = {2:5,8:6}
c = dict.fromkeys(data,0)
print c
for x in data:
    c[x] +=1

print c

