# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 14:14:00 2022

@author: reddy.chandra
"""
'''finding length'''
num=123459
length=0

while num>0:
    num//=10
    length +=1
    print("number of digits=",length)
    
    
x,y=0,10
while (x<y): x+=1; print(x*2)

'''remove negative elements from a list'''
l=list(range(-10,10,2))
print(l)

l.append(-50)

idx=0
while idx<len(l):
    if l[idx]<0:
         del l[idx]
    else:
        idx+=1
print(l)