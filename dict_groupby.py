# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 17:42:51 2016

@author: abc
"""

rows = [
{'address':'address1','date':'07/01/2016'},
{'address':'address2','date':'07/01/2016'},
{'address':'address3','date':'08/01/2016'},
{'address':'address4','date':'08/01/2016'},
{'address':'address5','date':'08/01/2016'},
{'address':'address6','date':'09/01/2016'},
]

from operator import itemgetter
from itertools import groupby

rows.sort(key=itemgetter('date'))

for date,items in groupby(rows,key=itemgetter('date')):
    print(date)
    for i in items:
        print '   ',i

from collections import defaultdict
rows_by_date = defaultdict(list)
for row in rows:
    rows_by_date[row['date']].append(row)
print rows_by_date
for r in rows_by_date['07/01/2016']:
    print(r)