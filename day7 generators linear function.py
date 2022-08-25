# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 09:56:19 2022

@author: reddy.chandra
"""
'''generators  
linear function'''

def gen_linear():
    x=0 
    m=2
    c=3
    while True:
        x+=1
        yield (m*x)+c
g=gen_linear()
for i in range(1,10):
    print(i,next(g))
  