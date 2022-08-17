# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 19:22:22 2022

@author: reddy.chandra
"""


'''range functions'''


for i in range(0,50):
    print(i,end=',')
    
    
    
for i in range(0,30+1):
    print(i)


print(list(range(-10)))
print(tuple(range(10)))
print(tuple(range(0,10,2)))
print(tuple(range(10,0,-1)))


squares=40
for i in range(40):
    print(i**2)
    
l=[i for i in range(10)]
print(l)

l=[i for i in range(60) if i % 8==0]
print(l)



import math
l=[math.cos(i) for i in range(60) if i % 4==0]
print(l)