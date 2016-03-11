# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 15:53:20 2016

@author: abc
"""

def saver(x=[]):
    x.append(1)
    print x

saver([2])
saver([2])
saver([2])
##沒給引數反而每次呼叫都會拉長，預設值會紀錄住?
saver()
saver()
saver()

print '=====分隔線====='

def saver(x=None):
    if x is None:
        x = []
    x.append(1)
    print x

saver([2])
saver()
saver()
print '印saver',
x =  saver()
##用print 的無用，因沒回傳值
print x

list = [1,2]
list.append(3)
print list
##這樣會有問題，因為append是程序
list = list.append(4)
print list