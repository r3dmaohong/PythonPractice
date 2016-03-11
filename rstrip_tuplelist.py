# -*- coding: utf-8 -*-
"""
Created on Tue Mar 08 17:46:36 2016

@author: abc
"""

print ['aaa\n','bbb\n']
print [line.rstrip() for line in ['aaa\n','bbb\n']]
##傳回值
print line
##產生值
print map((lambda line: line.rstrip()),['aaa\n','bbb\n'])

listoftuple = [('bob',35,'mrg'),('mel',31,'dev')]
##傳回值
print [age for (nm,age,job) in listoftuple]
print age
print nm
#產生值
print map((lambda (nm,age,job):age), listoftuple)

