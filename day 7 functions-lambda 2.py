# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 01:45:39 2022

@author: reddy.chandra
"""

'''
return functions'''

add=lambda x,y :x+y
sub=lambda x,y :x-y
mul= lambda x,y:x*y
power=lambda x,y:x**y

def calculator(operator =" "):
    
    d={}
    d['+']=add
    d['-']=sub
    d['*']=mul
    d['**']=power

    
    return d[operator]


fn=calculator('-')
print(fn(10,200))
fn=calculator('+')
print(fn(10,30))
fn=calculator('*')
print(fn(5,2))
fn=calculator('**')
print(fn(10,2))
