# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 01:16:45 2022

@author: reddy.chandra
"""

'''
sets
'''
s={1,2}
print(s)
print(type(s))
s.add('a')
s.add(3)

'''s.append(3)'''
'''s.add(3)'''
print(s)
s1={'a','b','c'}
'''s.add(s1)'''
s1={1,2,3,4,5}
s2={2,3,5,6,7,8}
print(s1.intersection(s2))
print(s1.union(s2))
print(s1.difference(s2))
print(s2.difference(s1))
print(1 in s1)
print(3 in s)
print(6 in s2)
s2= set(s1)
print(s1)
s2= list(s1)
print(s2)
j= list(set(s))
print(j)

