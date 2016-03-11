# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 10:35:04 2016

@author: abc
"""

x = 99
def selector():
    import __main__
    print __main__.x
    x = 88
    print x
selector()
