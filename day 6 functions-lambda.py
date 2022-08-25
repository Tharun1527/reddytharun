# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 01:32:55 2022

@author: reddy.chandra
"""

'''lambda'''

fn=lambda x:x**2
print(fn)
print(type(fn))

y=fn(2)
print(y)
print(fn(3.5))

power=lambda x,y: x**y
print(power(2,4))

p=lambda x,y: [x for i in range(y)]
print(p(2,4))

p2=lambda x,y:([x for i in range(y)],x*y,x+y)
print(p2(2,4))

fn1=lambda x,y:x**2

y=fn1(2,3)
print(y)
print(fn1(3,4))
print((lambda x,y :x**y)(10,2))
print((lambda x,y :x+y)(100,50))

great=lambda x,y :x>y
print(great(2,3))
print(great(5,2))

fn=lambda x :x**2 if x>0 else x**4
print(fn(3))
print(fn(-2))


import random
fn=lambda x:[random.random() for i in range(x)]
print(fn(4))
