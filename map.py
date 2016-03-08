# -*- coding: utf-8 -*-
"""
Created on Tue Mar 08 16:18:40 2016

@author: abc
"""

counters = [1,2,3,4]
def inc(x): 
    return x + 10

print map(inc, counters)
print map((lambda x: x + 3), counters)
print counters
new_counters = map(inc, counters)
print new_counters

##3**4
print(pow(3, 4))
print map(pow, [1,2,3],[2,3,4])
print map(pow, (1,2,3),(2,3,4))