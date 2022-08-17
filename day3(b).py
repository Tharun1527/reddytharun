# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 18:53:56 2022

@author: reddy.chandra
"""

'''
list slicing
'''
l1=[1,2,3,4,5,6]
print(l1[::-1])
print(l1[::7])
print(l1[0:len(l1):2])
print(l1[2:-1])
print(l1[2:-3])

print(l1[1:2])
print(l1[:1])
print(l1[:2])
print(l1[1:5])
print(l1[1:])
print(l1[0:])
print(l1[::-1])
print(l1[::1])
print(l1[1:2])
print(l1[0:-2])
print(l1[0:-1])
print(l1[2:-4])
print(l1[2:-1])
print(l1[::2])
print(l1[::3])
print([l1[::-3]])
l1.append([7,8])
print(l1)
print(l1[6])
print(l1[6][0:])
print(l1[6][1])
print(l1[6][0])
print(l1[::-1])
l1.pop()
l1.remove(6)
print(l1)
print(l1[0:len(l1):2])
print(l1[0:len(l1):1])
print(l1[len(l1)::-1])
l1.append([6,7])
print(l1[5][len([5])::-1])
print(l1[5][len([5])::2])
l1[5].reverse()
print(l1)
print(l1[5])
