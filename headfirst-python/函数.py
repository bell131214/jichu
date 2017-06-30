# -*- coding: utf-8 -*-
# def my_abs(x):
#     if not isinstance(x,(int,float)):
#         raise TabError('bad opreand type')
#     if x >=0:
#         return x
#     else:
#         return -x
#
# # print my_abs(-10)
# print my_abs('a')


# def power(x):
#     return x*x
# print power(10)

# def power(x, n=2):
#     s = 1
#     while n > 0:
#         n = n - 1
#         s = s * x
#     return s
# print power(5,3)
# print power(5)


# def enroll(name,gender,age=6):
#     print 'name:',name
#     print 'gender:',gender
#     print 'age:',age
#
# print enroll('zfl','A')

# def add(x,y,f):
#     return f(x)+f(y)
# print add(-10,6,abs)


# def f(x):
#     return x*x
# print map(f,[1,2,3,4,5,6])

# def f(x,y):
#     return x+y
# print f(1,2)
# print reduce(f,[1,2,3,4,5,6])

# def fn(x,y):
#     return x*10+y
# print reduce(fn,[1,3,5,7,9])
#
# print map(str.capitalize,map(str.lower,['adam', 'LISA', 'barT']))

# def is_odd(n):
#     return n%2==1
# print filter(is_odd,[1,2,3,4,5,6,7,8,9,10])

# print sorted([36,1,9,7,14,22])
# print sorted(['bob', 'about', 'Zoo', 'Credit'])

# def cmp(s1,s2):
#     u1 = s1.upper()
#     u2 = s2.upper()
#     if u1<u2:
#         return -1
#     if u1>u2:
#         return 1
#     return 0
# print sorted(['bob', 'about', 'Zoo', 'Credit'],cmp())


def sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax
