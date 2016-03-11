# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 09:51:30 2016

@author: abc
"""

D = {'a':1,'b':2,'c':3}
x = iter(D)
print D
print x
print x.next()
print x.next()
print x.next()

for key in D:
    print key, D[key]

print [x ** 2 for x in range(4)]
print (x ** 2 for x in range(4))

G = (x ** 2 for x in range(4))
print G.next()
print G.next()
print G.next()
print G.next()

for num in (x ** 2 for x in range(4)):
    print '%s, %s' % (num,num/2.0)

print sorted((x**2 for x in range(4)), reverse=True)

import math
print map(math.sqrt, (x**2 for x in range(4)))
