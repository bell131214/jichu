# -*- coding: utf-8 -*-
import os
filename = raw_input('请输入文件名：')
try:
    f = open(filename)
    print hello
except IOError,msg:  #IOError 异常的类型，要写对
    print '文件不存在' #对异常的处理函数
except NameError,msg:
    print '内部变量调用有问题'  #有异常不执行后面代码hello，直接到except捕获异常
finally:
    f.close()  #必须执行的字句



