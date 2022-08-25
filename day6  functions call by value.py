# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 01:14:03 2022

@author: reddy.chandra
"""

'''call by value'''

a=1000
def fn(a):
    print("inner",id(a))
    a= a+1
    print("inner2",id(a))
    a= a+1
    return a
fn(a)
print(a)

b=fn(a)
print(b)