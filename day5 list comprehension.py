# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 00:21:06 2022

@author: reddy.chandra
"""

'''list comprehension'''
def odd(num):
    if num%2==1:
        return True
    else:
        return False
l=[i for i in range(100)if odd(i)]
print(l)
l=[(i,i*i) for i in range(100)if odd(i)]
print(l)

for k,i in enumerate(range(0,30,2)):
    print(k,i)