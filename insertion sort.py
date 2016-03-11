# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 17:02:25 2016

@author: wjhong
"""

def insert(x):
    n = len(x)
    i = 1
    while i<n-1:
        key = x[i]
        j = i-1
        while j>=0 and key<x[j]:
            x[j+1]= x[j]
            j -= 1
        x[j+1] = key
        i += 1
    return x
print insert([1,10,2,5,41,25,3,48])
