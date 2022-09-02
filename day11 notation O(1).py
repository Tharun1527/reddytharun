# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 01:22:47 2022

@author: reddy.chandra
"""

'''time complexity
O(1)
'''
def addition(a,b):
    
    num_iterations=0
    
    total=a+b
    num_iterations +=1
    
    print('*'*10)
    print("sum",total)
    print("iterations",num_iterations)
    
addition(1,2)
addition(19,20)
addition(10,2.32553)