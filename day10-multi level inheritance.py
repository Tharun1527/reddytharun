# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 22:17:59 2022

@author: reddy.chandra
"""
'''multi level inheritance'''

class vechile:
    v_type="vechile"
    
class disel(vechile):
    f_type="disel"
    
class bus(vechile):
    w_count=6
help(bus)   
a=bus()
print(a.w_count)
print(a.f_type)
print(a.v_type)
