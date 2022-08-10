# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 17:28:11 2022

@author: reddy.chandra
"""

a={"tharun":[1,2,3],"abcd":"ABCD"}
print(a)
b=a
print(b)
b=a.copy()
b["abcd"]
a["tharun"]=[3,2,1]
print(a)
print(b)

import copy
b=copy.deepcopy(a)
a["abcd"]=[321]
print(b)
print(a)
