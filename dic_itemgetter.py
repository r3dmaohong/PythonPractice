# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 14:49:37 2016

@author: abc
"""

rows = [
{'fname':'a','lname':'b','uid':1},
{'fname':'c','lname':'d','uid':2},
{'fname':'e','lname':'f','uid':5},
{'fname':'g','lname':'h','uid':4},
{'fname':'i','lname':'j','uid':3},
]

from operator import itemgetter

rows_by_fname = sorted(rows,key=itemgetter('fname'))
rows_by_uid = sorted(rows,key=itemgetter('uid'))

print rows_by_fname
print rows_by_uid

print sorted(rows,key=itemgetter('uid','fname'))
print sorted(rows,key=lambda r:(r['uid'],r['fname']))

print max(rows)
print max(rows,key=itemgetter('uid'))
print min(rows,key=itemgetter('uid'))