# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 17:45:03 2016

@author: wjhong
"""

a='abcd'
print '.'.join(a)   
print '|'.join(['a','b','c'])
#可以把['a','b','c']看做是 a='abcd';下面同理
print '.'.join({'a':1,'b':2,'c':3,'d':4})

s='a b c'
print s.split(' ')
print s.split('x')
st='hello world'
print st.split('o')
print st.split('o',1)
