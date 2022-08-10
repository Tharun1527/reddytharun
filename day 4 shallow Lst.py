# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 12:57:08 2022

@author: reddy.chandra
"""

'''
shallow copy
'''
a=[1,2,3,4,5,[9,10,11],[12,13,14]]
b=a
print(b)
print(a)
print(id(a))
print(id(b))

b.append(6)
print(b)



b=a.copy()
print(b)
a.append(7)
print(a)
b[5][0]=100
b[5][1]=200
print(b)

import copy
b=a
b=copy.deepcopy(a)
print(a)
b[5][0]=100
print(b)

