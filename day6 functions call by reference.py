# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 01:18:59 2022

@author: reddy.chandra
"""

'''call by reference'''

fruits=['apple','mango']
def fn(fruits):
    fruits.append('grapes')
    return fruits

print(fruits)
print(id(fruits))
print(fn(fruits))
print(fruits)
print(id(fruits))