# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 14:11:19 2016

@author: abc
"""

class super:
    def hello(self):
        self.data1 = 'spam'
class sub(super):
    def hola(self):
        self.data2 = 'eggs'
    
x = sub()
y = sub()
x.hello()
print x.__dict__
x.hola()
print x.__dict__
print y.__dict__
print sub.__dict__
print super.__dict__

print '==================='
print '==================='

print x.data1
print x.__dict__['data1']

x.data3 = 'toast'
print x.__dict__

print x.data3
x.__dict__['data3'] = 'ham'
print x.data3

print x.__dict__
print x.__dict__.keys()
print dir(x)
print dir(super)
print dir(sub)