# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 17:02:25 2016

@author: wjhong
"""

def bubble(x):  
##冒泡排序，x是列表，n是列表長度  
    n = len(x)
    for i in range(n):
        for j in range(n-1):
            if x[j]>x[j+1]:
                t = x[j]  
                x[j] = x[j+1]  
                x[j+1] = t  
        return x                  
print bubble([1,10,2,5,41,25,3,48])
print len([1,10,2,5,41,25,3,48])