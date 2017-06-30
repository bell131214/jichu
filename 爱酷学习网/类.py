#coding:utf8
# class Test:
#     first = 123
#     second = 456  #类的二个类的属性
#     def f(self):  #类的方法
#         return 'test'
#
# milo = Test()#实例化一个对象
# print milo.f()#调用类的方法
# print milo.first#调用类的属性
#
# l = [1,2,3,4,56,7]
# l.append(20)
# help(list.append)

class Ren:
    name = "人"
    high = "身高"
    wight = "体重"
    __money = "我有十块钱"#内部调用
    def run(self):
        print "跑步"
        print self.name#访问自己的属性，必须是self访问
    def say(self):
        print self.__money
if __name__=='__main':
        # p = file()#也是一个类
        zhangsan = Ren() #对象的句柄--区分不同的对象，变量的名字不一样+属性和方法
        zhangsan.name = "张三"
        zhangsan.money = "一百万"
        print Ren.name
        print zhangsan.name
        print zhangsan.run()

