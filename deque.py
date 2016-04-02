# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 22:08:10 2016

@author: mao
"""

from collections import deque

def search(lines, pattern, history = 5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)

##判斷是否在原檔執行
"""if __name__ == '__main__':
    with open('test.txt) as f:
        for line, prevlines in search(f, 'python', 5):
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('-'*20)
            """

##examples
q = deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)
print(q)

q.append(4)
print(q)
print(q[-1])

q.appendleft(5)
print(q)
q.pop()
print(q)
q.popleft()
print(q)