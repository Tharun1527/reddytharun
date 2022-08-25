# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 10:59:15 2022

@author: reddy.chandra
"""

'''sum using while and for'''
l=[1,2,3,4,5]
total=0
idx=0
while idx<len(l):
    total += l[idx]
    idx+=1
print(total)


toatal=0
for i in l:
        toatal+=i
        print(toatal)
        
        
        
print(sum(l))