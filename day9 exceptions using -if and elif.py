# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 19:13:59 2022

@author: reddy.chandra
"""
'''exception by if and elif'''

a=0
if a<0:
    raise Exception("value should be greater than 0")
try:
    if a<10:
        raise Exception("value should be greater than 10")
    elif a<100:
       raise Exception ("value should be greater than 100 ")
except Exception as e:
    print("caught:",e)
    
print("end")