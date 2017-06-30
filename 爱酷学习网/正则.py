# -*- coding: utf-8 -*-
import re
# s = r'abc'
# print re.findall(s,'abcaaaabcaaaaaaaaa')

# s = "top tip tqp twp tep"
# res = r"t[^io]p"
# print re.findall(res,s)

# r = r"^abc"
# print re.findall(r,'abc')
#
# r = r"\^abc"
# print re.findall(r,'^abc')

#下面二个r性质一样
# r = r"[0-9]"
# r = r"\d"
# print re.findall(r,'1234567890')

#电话号码规定位数的匹配
# s = 010-12345678
# r =r"^010-\d\d\d\d\d\d\d\d"#^首行匹配，然后是八位
# r =r"^010-\d{8}" #重复的次数
# print re.findall(r,'010-78945622')
#
# r =r"010-a{8}"
# print re.findall(r,'010-aaaaaaaa')

# r = r"ab*"
# print re.findall(r,'a')
# print re.findall(r,'ab')
# print re.findall(r,'abbbbbb')

# r = r"ab+"
# print re.findall(r,'ab')
# print re.findall(r,'abbc')

# r =r"010-?\d{8}$"
# print re.findall(r,'010-12345678')
# print re.findall(r,'010--12345678')

# print re.findall(r,'a')

r = r"a{1,3}"
print re.findall(r,'a')
print re.findall(r,'aa')
print re.findall(r,'aaa')
print re.findall(r,'aaaaa')