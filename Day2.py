# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 14:15:12 2022

@author: reddy.chandra
"""

a=(complex(2,8))
print(a)
print(a+4)
print(a*5)
print(a/5)

"precedence"

print(3-4*2)
print((3-4)*2)
print((2+4)*4)
print(2+4*4)
print((2+4*3+7))
print((2+4)*(3+7))


L2=['reddy','chandra','tharun']
print(L2)
print(type(L2))
L3=['asds',123,2+4j]
print(L3)
print(L3[1])
print(L3[0])
print(type(L3[0]))
print(type(L3[1]))
print(type(L3[2]))
L3.append(3.5)
print(L3)
L2.append('mphasis')
print(L2)
