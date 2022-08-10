# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 16:40:35 2022

@author: reddy.chandra
"""

'''shallow copy'''

a=(1,23,24,25,[50,100,1000,7000],('n','b'))
b=a
print(b)

import copy
b=copy.deepcopy(a)
print(a)
print(b)
b[4][0]=9000
