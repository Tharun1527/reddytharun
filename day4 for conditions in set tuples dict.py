# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 12:14:19 2022

@author: reddy.chandra
"""

'''for  conditions in set tuples dict'''


t=(1,2,3,"hello")

for i in t:
    print(i)

s={1,2,3,4,5,6}
for set in s:
    print(set,end=' ')
    
d={"asdf":2,"fdve":4,"juyr":6}
for dic in d:
    print(dic,d[dic])
    
a={"asdf":2,"fdve":4,"juyr":6}
for c in a.items():
    print(c)
    
    
st="MphASis"
if st[4].isupper():
    print("correct")
else:
    print("wrong")
    
    
