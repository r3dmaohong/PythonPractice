# -*- coding: utf-8 -*-
"""
Created on Tue Mar 08 17:46:36 2016

@author: abc
"""

print ['aaa\n','bbb\n']
print [line.rstrip() for line in ['aaa\n','bbb\n']]
print map((lambda line: line.rstrip()),['aaa\n','bbb\n'])


