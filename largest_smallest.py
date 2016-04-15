# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 10:16:07 2016

@author: abc
"""

import heapq

nums = [1,8,3,7,-5,18,23,5]
print(heapq.nlargest(3,nums))
print(heapq.nsmallest(2,nums))

protfolio =[
{'name':'IBM','share':100,'price':91.1},
{'name':'A','share':1,'price':4.1},
{'name':'B','share':50,'price':121.1},
{'name':'C','share':10,'price':3.1},
{'name':'D','share':70,'price':16.1},
]

print(heapq.nsmallest(3,protfolio,key=lambda s:s['price']))
print("\n")
print(heapq.nlargest(3,protfolio,key=lambda s:s['price']))