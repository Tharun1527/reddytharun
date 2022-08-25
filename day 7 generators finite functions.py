# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 09:32:40 2022

@author: reddy.chandra
"""

'''generators
finite series'''

def gen_even_numbers_limit(limit):
    
    
    for i in range(0,limit +1,2):
        yield  i
def gen_even_number_count(count):
    
   i=0
   while i <count:
    i+=1
    yield i*2
g=gen_even_numbers_limit(10)
for i in g:
    print(i)
g2=gen_even_number_count(10)
print([i for i in g2])
print([i for i in gen_even_number_count(20)])
print(list(gen_even_number_count(2)))
print(tuple(gen_even_number_count(2)))
print(set(gen_even_number_count(2)))