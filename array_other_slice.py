# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 11:33:58 2016

@author: abc
"""

items = [0,1,2,3,4,5,6,7,9]
a = slice(2,4)
print items[2:4]
print items[a]

items[a] = [10,11]
print items
del items[a]
print items

b = slice(5,50,2)
print b.start
print b.stop
print b.step

s = "helloworld"
##依照物件作slice的size的設定
print b.indices(len(s))
##米字號才能跑欸
for i in range(*b.indices(len(s))):
    print(s[i])
