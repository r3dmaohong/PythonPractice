# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 14:03:47 2016

@author: abc
"""

prices = {
    "A":1,
    "B":2,
    "C":3
}

min_price = min(zip(prices.values(),prices.keys()))
print min_price
print max(zip(prices.values(),prices.keys()))
print max(zip(prices.keys(),prices.values()))
print max(prices)
print max(prices.values())
print max(prices,key=lambda k:prices[k])

prices_sorted = sorted(zip(prices.values(),prices.keys()))
print prices_sorted
