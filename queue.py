# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 11:01:10 2016

@author: abc
"""

import heapq

class PriorityQueue:
    def __init__(self):
        self.queue = []
        self._index = 0
    def push(self,item,priority):
        ##利用tuple塞入排序
        heapq.heappush(self.queue,(-priority,self._index,item))
        self._index += 1 
    def pop(self):
        ##-1是選顯示ITEM -3為Priority
        return heapq.heappop(self.queue)[-1]
    def __repr__(self):
        return format(self.queue)

class Item:
    def __init__(self,name):
        self.name = name
    ##顯示方式
    def __repr__(self):
        return 'item({!r})'.format(self.name)

q= PriorityQueue()
print(q)
q.push(Item('foo'),1)
print(q)
q.push(Item('foo5'),5)
print(q)
q.push(Item('foo4'),4)
q.push(Item('foo1'),1)
print(q)
print(q.pop())
print(heapq.heappop(q.queue)[-1])
print(q.pop())
print(q.pop())

##有priority才能比較
##priority還要擺前面!?
print( (1,Item('foo5')) > (1,Item('foo')))
##增加index 當priority
print((1,1,Item('A')) > (1,2,Item('B')))