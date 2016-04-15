# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 14:25:02 2016

@author: abc
"""

a = {
    'A':1,
    'B':2,
    'C':3
}

b = {
    'D':4,
    'B':2,
    'E':5
}

print a.keys()# & b.keys()
print b.keys()
#a.items() - b.items()
print {key:a[key] for key in a.keys() - {"A","C"}}