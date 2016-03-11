# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 09:26:32 2016

@author: abc
"""

def gensquares(N):
    for i in range(N):
        yield i ** 2

for i in gensquares(5):
    print i , ', ',
print
x = gensquares(5)
print x
print x.next()
print x.next()
print x.next()

def buildsquares(n):
    res = []
    for i in range(n):
        res.append(i**2)
        ##記得return要在外面，否則i=0時就斷掉回傳了
    return res

for x in buildsquares(5): print x, ',',
print
for x in [n**2 for n in range(5)]:
    print x, ',' ,
print
for x in map((lambda x:x**2), range(5)):
    if x == 4**2:
        print x
    else:
        print x, ',' , 