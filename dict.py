# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 11:50:27 2016

@author: abc
"""
##
##weired
##
from collections import defaultdict
pairs = {"A":1,"B":2}
##[{'A',1},{'B',2},{'C',3},{'D',4}]
##第一種方法較為簡潔
d = defaultdict(list)
for key, value in pairs:
    d[key].append(value)
print(d)
##
d={}
for key, value in pairs:
    if key not in d:
        d[key]=[]
    d[key].append(value)
print(d)


##
##
##
from collections import OrderedDict
d = OrderedDict()
d["A"] = 1
d["B"] = 2
d["C"] = 3
d["D"] = 4

for key in d:
    print(key,d[key])

import json
print json.dumps(d)