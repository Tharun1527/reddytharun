# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 07:32:49 2022

@author: reddy.chandra
"""

'''
lambda
'''
def calculate(operation, *args):
    return operation(*args)

print(calculate(lambda x: x**2, 2))
print(calculate(lambda x,y:x+y,5,5))
print(calculate(lambda x,y:x*y,10,10))


from math import sin,pi,cos
print((lambda x: sin(x))(pi/2))




fn=lambda x:x<10
print(list(filter(fn,[i for i in range(20)])))

