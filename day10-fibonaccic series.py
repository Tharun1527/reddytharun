# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 22:17:45 2022

@author: reddy.chandra
"""

'''fibonacci series'''

def fib(n):
    a,b= 0,1
    
    while b<n:
        print(b)
        a,b=b,a+b
        
# generate and return fibonacci series up to n

def fib2(n):
    result=[]
    a,b=0,1
    
    while b<n:
        result.append(b)
        a,b=b,a+b
        
        return result