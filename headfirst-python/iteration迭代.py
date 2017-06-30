# -*- coding: utf-8 -*-
# for ch in 'ABC':
#     print ch

# d = {'a': 1, 'b': 2, 'c': 3}
# for key in d:
#     print key
#
# for x,y in [(1,1),(2,4),(3,8)]:
#     print x,y
#
#
# for i,value in enumerate(['a','s','d']):
#     print i,value

# L = []
# for x in range(1,11):
#     L.append(x*x)
#
# print L


# L = [x*x for x in range(10)]
# print L

g = (x*x for x in range(10))
print g
for n in g:
    print n

# import os
# print [d for d in os.listdir('.')]


