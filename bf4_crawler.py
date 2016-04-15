# -*- coding: utf-8 -*-
"""
Created on Thu Apr 07 15:47:14 2016

@author: abc
"""

#coding=utf-8

import requests
from bs4 import BeautifulSoup
import lxml

#送出GET請求到遠端伺服器，伺服器接受請求後回傳<Response [200]>，代表請求成功
res = requests.get("http://yanlong4869.blogspot.tw/2015/09/python-crawler.html")
#print res.text

#經過BeautifulSoup內lxml編輯器解析的結果
##soup = BeautifulSoup(res.text,'lxml')
soup = BeautifulSoup(res.text)
#印出網頁內容
# print soup 
#print soup

#使用select選取特定元素
#title = soup.select('#h3')[0].text
##content = soup.select('span')[0].text
for item in soup.select('span'):
    print item.text.strip()

##post
##www.thsrc.com.tw/tw/TimeTable/SearchResult
payload = {
'StartStation':'977abb69-413a-4ccf-a109-0272c24fd490',
'EndStation':'3301e395-46b8-47aa-aa37-139e15708779',
'SearchDate':'2016/04/08',
'SearchTime':'16:00',
'SearchWay':'DepartureInMandarin'
#'RestTime:
#'EarlyOrLater:
}

res = requests.post("http://www.thsrc.com.tw/tw/TimeTable/SearchResult", data = payload)
##print res.text
soup = BeautifulSoup(res.text)

for item in soup.select('tr'):
    print item.text.strip()