# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 01:26:06 2022

@author: reddy.chandra
"""

'''return function'''

def cal(operator="+"):
    def add(a,b):
        return a+b
    def sub(a,b):
        return a-b
    
    d={}
    d['+']=add 
    d['-']=sub
    return d[operator]
    
fn=cal('-')
print(fn)
print(type(fn))
print(fn(200,300))