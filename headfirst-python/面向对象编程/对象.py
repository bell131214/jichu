# -*- coding: utf-8 -*-
# class Student(object):
#     def __init__(self,name,score):
#         self._name=name
#         self._score=score
#
#     # def print_score(self):
#     #     print '%s: %s'%(self._name,self._score)
#
#     def get_grade(self):
#         if self.score>=90:
#             return 'A'
#         elif self.score>=60:
#             return 'B'
#         else:
#             return 'C'



# batr = Student('aaa',59)
# # batr.print_score()
# print batr.score
# batr.score=80
# print batr.score
# # print batr.get_grade()

class Animal(object):
    def run(self):
        print 'Animal is running....'

class Dog(Animal):
    def run(self):
        print 'Dog is running...'
    def eat(self):
        print 'Eating meat....'


dog = Dog()
print dog.run()
print dog.eat()
