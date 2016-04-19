# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 14:25:15 2016

@author: abc
"""

mylist = [1,2,4,7,10,22,-1]
print [n for n in mylist if n > 0 and n < 10]

##generator expressions
pos = (n for n in mylist if n > 0)
for x in pos:
    print x

values = ['2','1','9','-7','10','-','4','N/A','5']
def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False
##filter創建iterator
ivals = list(filter(is_int,values))
print ivals

import math
print [math.sqrt(n) for n in mylist if n > 0]
##用else取代不適的值
#mylist = [-10,1,2,4,7,10,22,-1]
print [n if n > 0 else 0 for n in mylist]

addresses = ['A1','A2','A3','A4','A5','A6','A7']
counts = [0,5,6,7,9,10,4]

from itertools import compress
more5 = [n>5 for n in counts]
print more5
print list(compress(addresses,more5))