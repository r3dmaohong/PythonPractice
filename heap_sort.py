# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 10:26:03 2016

@author: abc
"""

nums = [1,8,4,6,7,44,6,5,-55]
import heapq
heap = list(nums)
print(heap)
heapq.heapify(heap)
print(heap)
print(heapq.heappop(heap))
print(heap)
print(min(heap))
print(max(heap))
print(sorted(nums))
print(heap[0])