# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 14:37:23 2016

@author: abc
"""

def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

a = [1,5,8,3,1,8,-1]
print list(dedupe(a))
print set(a)

def dedupe_dict(items,key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)
b = [{"x":1,"y":2},{"x":1,"y":3},{"x":1,"y":2},{"x":2,"y":4}]
print list(dedupe_dict(b, key=lambda d:(d["x"],d["y"])))
print list(dedupe_dict(b, key=lambda d:d["x"]))