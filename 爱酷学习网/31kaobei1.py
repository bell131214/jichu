# -*- coding: utf-8 -*-
a = [1,2,3,'a','b','c']
b = a
print a
print b
print id(a)
print id(b)
print a.append('d')
print a
print b
print b.append(4)
print a
print b