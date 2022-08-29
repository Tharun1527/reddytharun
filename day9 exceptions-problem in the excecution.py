# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 14:51:50 2022

@author: reddy.chandra
"""

'''exceptions'''

import sys
def add():
    print("in add1")
    a=2+"2"
    print("in add2")   

try:
   # a=2+"4"
    #print(a)
    add()
    print("all is fine")
except:
    print("problem with execution")
    print(sys.exc_info())
    print(sys.exc_info()[1])