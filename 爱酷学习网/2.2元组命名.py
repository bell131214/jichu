# -*- coding: utf-8 -*-
from collections import namedtuple
#枚举
# NAME,AGE,SEX,EMAIL = xrange(4)
# student = ('ling',28,'male','110@qq.com')
#
# print student[NAME]
# if student[AGE]>=18:
#     print student[AGE]

#标准库
Student = namedtuple('Student',['name','age','sex','emali'])
s1 = Student('ling',28,'male','110@qq.com')
print s1
# s2 = Student('ling',28,'male','110@qq.com')
# print s2
print s1.name