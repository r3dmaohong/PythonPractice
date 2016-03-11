# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 17:50:28 2016

@author: wjhong
"""

z1=[1,2,3]
z2=[4,5,6]
result=zip(z1,z2)
print result

z3=[4,5,6,7]
result=zip(z1,z3)
print result

##解壓縮
print zip(*result)

a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print [ [row[col] for row in a] for col in range(len(a[0]))]

a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print map(list,zip(*a))

x=[1,2,3]
y=['a','b','c']
print zip(x,y)

x=[1,2,3]
y=['a','b','c']
print zip(*zip(x,y))

def add(x,y):
    return x+y
     
##add為自己加自己?
print map(str, range(5))
print map(lambda x:x+x,range(5)) 
print map(lambda x:x+1,range(10)) 


print reduce(add,range(10))        
 #1+2+3+...+9
 
print reduce(lambda x,y:x*y,range(1,3),5)           #lambda 函數，5是初始值， 1*2*5

def div(n):
    return n%2
print filter(div,range(5))  #返回div輸出的不等於0的真值

print filter(lambda x : x%2,range(10))        #lambda 函數返回奇數，返回列表

print filter(lambda x : not x%2,range(10))

def fin(n):return n!='z'                #過濾'z' 函數，出现z则返回False
print filter(fin,'zhoujy')  

print filter(lambda x : x !='z','zhoujy')     #labmda返回True值



def add_factorial(n):
    empty_list=[]           #聲明一個空列表，存各個階乘的結果，方便這些結果相加
    for i in map(lambda x:x+1,range(n)):    #用傳進來的變量(n)來生成一个列表，用map讓列表都+1，eg：range(5) => [1,2,3,4,5]
        a=reduce(lambda x,y:x*y,map(lambda x:x+1,range(i)))   #生成階乘，用map去掉列表中的0
        empty_list.append(a)            #把階乘結果append到空的列表中
    return empty_list
if __name__ == '__main__':
    import sys

try:
    n = input("Enter a Number(int) : ")
    result=add_factorial(n)   #傳入變量
    print reduce(lambda x,y:x+y,result)      #階乘結果相加
except (NameError,TypeError):
    print "That's not a Number!"
    

def is_prime(start,stop):
    stop  = stop+1     #包含列表右边的值
    prime = filter(lambda x : not [x%i for i in range(2,x) if x%i == 0],range(start,stop))   #取出質數,x从range(start,stop) 取的數
    print prime
if __name__ == '__main__':
    try :
        start = input("Enter a start Number :")
    except :
        start = 2   #开始值默认2
    try :
        stop  = input("Enter a stop  Number :")
    except :
        stop  = 0   #停止數，默认0，即不返回任何值
    is_prime(start,stop)

def prime(n):
    for s in range(2,n):
        if n % s == 0:
            return False
    return True

print filter(prime, range(100,201))