# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 11:57:49 2022

@author: reddy.chandra
"""

'''lists as stacks'''

stack=[]

for i in range(1,11):
    stack.append(i)
    
print(stack)
while len(stack)>0:
    print(stack.pop(),end =" ")