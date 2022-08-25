# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 08:19:30 2022

@author: reddy.chandra
"""

'''
generator functions'''

def gen ():
    yield 1
    
    yield 2
    
    yield 3

g=gen    
print(g)
#print(next(g()))
for i in g():
    print(i)
    
def s1(x):
    for i in range(10):
        yield x**i
g=s1(2)
for i in g:
    print(i)

print(list(s1(10)))