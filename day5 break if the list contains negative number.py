# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 14:14:01 2022

@author: reddy.chandra
"""

'''while break'''
'''break if the elements have -ve numbers'''

l=[1,2,3,4,5,6,-100]
idx=0
while idx <len(l):
     if l[idx]<0:
         print("negative number is there")
         break
     else:
         pass
     idx+=1
else:
   print("no negative number present")
     