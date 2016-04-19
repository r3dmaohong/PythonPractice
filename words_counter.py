# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 11:50:44 2016

@author: abc
"""

words=['yo','ho','ho','ho','ho','ho','ho','hi','hi','hi','hi','hi','hi','hi','hi'
,'hello','hello','hello','hello','hello','hello','hello','hello','hello']

from collections import Counter
word_counts = Counter(words)
top_three = word_counts.most_common(3)
print top_three
print word_counts['yo']

morewords=['hi','hooo']
word_counts.update(morewords)
print word_counts.most_common(3)

b = Counter(morewords)
##可以相加相減
c  = word_counts + b
print c
d = word_counts - b
print d
