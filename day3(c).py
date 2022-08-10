# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 23:31:28 2022

@author: reddy.chandra
"""

'''
tuples
'''
a=(1,2,'a','b',2+4j,True,'c','c','c')
print(a)
print(type(a))
'''a.append('c')'''
print(a[0])
print(a[0:])
print(a[::-1])
'''a.reverse()'''
print(a[::-2])
print(len(a))
print(a.index('a'))
print(a.index('b'))
print(a.count('c'))
l1=(1,2,3,4,5,8,9,['e','f'])
l1[7].append('g')
print(l1)
print(a.index(2))
print("number of times c count is {}".format(a.count('c')))
l1[7].reverse())
print(l1[7])
l1=("e",True,False)
print(l1.index(False))
l2=[1,4,6]
l3=(3,l2,5)
print(l3)
print('h' in l1)
