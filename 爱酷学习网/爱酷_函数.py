# -*- coding: utf-8 -*-
# a = 200
# b = 300
# def add():
#     c = a + b
#     print c
#
# add()
# a = 100
# def fun():
#     if False:
#         print "good"
#     print a
# fun()
# fun()
# fun()
# fun()
# fun()
# fun()

# def fun(x):
#         print x
# s = raw_input('input:')
# fun(s)

# def fun(x,y):
#     if x == y:
#         print 'x','=','y'
#     else:
#         print 'x','!=','y'
# s1 = raw_input('input1:')
# s2 = raw_input('input2:')
# fun(s1,s2)

# def fun(x=3,y='奶油'):
#     print "生成一个",x,"元",y,"口味的冰激凌"
# s1 = raw_input('input1:')
# s2 = raw_input('input2:')
# fun(10)
# fun(y='巧克力')
# fun(20,'水果')

#全局变量和局部变量
# def fun():
#     a = 100
#     print a
# fun()
# print "&"*20
# print a

# globalint = 9
# def myAdd():
#     localint = 3
#     print globalint
#     print localint
#
# myAdd()
# print globalint
# print localint

# x = 'i am aa'
# def fun():
#     global y
#     x = 100
#     y = 200
#     global x
#     print x
# print x
# fun()
# print x
# print y

# def f(x,y):
#     print 'welecome'
#     return x+y
# f(2,3)
# z = f(2,3)
# print z

# def f(x,y):
#     if x<y:
#         return -1
#     print "hello world"
# f(4,1)  #条件不成立不执行return，执行print---结果是hello
# f(4,6)  #条件成立，执行return，结果是none，不执行print，
# 一旦执行了return，就不执行后面的代码---结果啥都没有

# def f(x,*args):#可以传入任意数量的参数
#     print x
#     print args
#
# f(1)
# f(1,2,3,4,5,6,7)

# def f(x,*args,**kwargs):#可以传入任意数量的参数
#     print x
#     print args
#     print kwargs
#
# f(2,6,5,8,y=3,s=4)

# g = lambda x,y:x*y
# print g(2,5)

# l = range(1,7)
# print l
#
# def f(x,y):
#     return x*y
# print reduce(f,l)
# l = range(1,7)
# f = lambda x,y:x*y
# print reduce(lambda x,y:x*y,l)

import switch
print switch.add(2,3)


