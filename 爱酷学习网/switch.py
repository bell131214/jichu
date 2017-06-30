# -*- coding: utf-8 -*-
from __future__ import division
def add(x,y):
    return x+y

def jian(x,y):
    return x-y

def cheng(x,y):
    return x*y

def chu(x,y):
    return x/y
# def operator(x,o,y):
#     if o=="+":
#        print add(x,y)
#     elif o=="-":
#         print jian(x,y)
#     elif o=="*":
#        print cheng(x,y)
#     elif o=="/":
#        print chu(x,y)
#     else:
#         pass
#
# operator(2,"/",4)

# print add(2,8)
# print jian
# operator = {"+":add,"-":jian,"*":cheng,"/":chu}
# print operator["+"](3,5)

# s = [5,69,7,8,5,2,6,8,8,7,4,45,69,89]
# print max(s)
# print min(s)
# print len(s)
# print divmod(5,2)

# s = "hello world"
# print s.capitalize()

# def f(x):
#     if x>5:
#         return True
# print f(10)
# print f(3)
# s = range(10)
# print filter(f,s)

# s = range(10)
# def f(x):
#     if x%2==0:
#         return True
# print filter(f,s)

# name = ['milo','zou','tom']
# age = [20,30,40]
# tel = ['122','155','186']
# print zip(name,age,tel)
# print map(None,name,age,tel)
#
# s = range(101)
# print reduce(lambda x,y:x+y,s)