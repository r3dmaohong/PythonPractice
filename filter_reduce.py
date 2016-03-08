# -*- coding: utf-8 -*-
"""
Created on Tue Mar 08 16:31:59 2016

@author: abc
"""

print filter((lambda x: x > 0), range(-5,5))
print [x for x in range(-5,5) if x > 0]
##
print reduce((lambda x, y: x + y), [1, 2, 3, 4])
print reduce((lambda x, y: x * y), [1, 2, 3, 4])

print [x ** 2 for x in range(10) if x % 2 == 0 ]
print map((lambda x: x**2), filter((lambda x: x % 2 == 0), range(10)))

##等於兩層迴圈
print [x + y for x in [0, 1, 2] for y in [100, 200, 300]]
print [x + y for x in 'spam' for y in 'SPAM']


print [(x,y) for x in range(5) if x % 2 == 0 for y in range(5) if y % 2 == 1 ]