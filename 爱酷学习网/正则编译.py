# -*- coding: utf-8 -*-
import re
r1 = r"\d{3,4}-?\d{8}"
# print re.findall(r1,"010-12345678")
# print re.findall(r1,"010-1234567")

#正则表达式编辑
# r1 = r"\d{3,4}-?\d{8}"
# p_tel = re.compile(r1)
# print p_tel
# print p_tel.findall('010-12345677')
#
# csvt_re = re.compile(r'csvt',re.I)#大小写都可以
# print csvt_re.findall('CsVT')

# r1 = r"csvt.net"
# print re.findall('csvt/nnet',re.S)

# s = '''
# hello csct
# csvt hello
# hello csvt hello
# csvt hehe
# '''
# r = r"^csvt"
# print re.findall(r,s)
# print re.findall(r,s,re.M)#多行匹配

# email = r"\w{3}@\w+(\.com|\.cn)"
# print re.match(email,'zzz@csvt.com')
# print re.match(email,'zzz@csvt.cn')

s = "hhhssj snjx hello src=csvt yes jdscdbh jdsjd src=123 yes cdjs src=234 yes hello src=pynhj yes kdjs"
r1 = r"hello src=(.+) yes"

print re.findall(r1,s)