# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 14:40:46 2022

@author: reddy.chandra
"""

'''validation with decorator'''

from math import pi

def validate(func):
    
   def cal(r):
     if r<=0:
        raise ValueError("the radius must be greater than 0")
        
        return func(r)
     
   return cal 

@validate
def area(r):
    return pi * r * r

print("the area is " ,area(0))
