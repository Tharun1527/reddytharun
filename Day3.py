# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 15:42:21 2022

@author: reddy.chandra
"""

l1=['a',1,3.5,3+2j]
print(l1)
print(l1[0])
print(l1[3])


l1.append('tharun')
print(l1)
l1.append(1234)
l1.pop(0)
print(l1)
l1.pop(0)
l1.insert(0,'hi')
l1.insert(1,'this is')
l1.remove(1234)
l1.remove('this is')

l2=[1,2,3,4,'chandra']
'''l1.extend(l2)'''
print(l1)
l2.append('tharun')
l1.append(['tharun','chandra'])
print(l1)
print(l1[4])
print(l2[4][1])
l1.append('sfcdsdd')
print(l1)
l1.insert(5,'asdf')
l1.insert(7,'csdvfv')
l1.insert(3,123453)
l1.remove('asdf')
l1.pop()
l1.pop(6)
l1[5].append('reddy')
l1[5].insert(3,'is feeling good')
l1[5].pop(2)
l1[5].remove('chandra')
print(l1[5][1])
print(l1[5][0])
print(l1.reverse())
print(l1)




a=['m','p','h','a','s','i','s']
print("".join(a))
print(type(a))
print(l1[::-1])
print(l1[::1])
print(l1[:1])
print(l2[:2])
print(reversed(a))
print("////".join(reversed(a)))
print("?/?".join(a))
print(a,sep=";;;;;")
print(a,end="::::")
print(a.reverse())
print(a)
