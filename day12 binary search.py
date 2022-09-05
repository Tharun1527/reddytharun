# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 14:41:21 2022

@author: reddy.chandra
"""

'''binary search'''

def binary_search(in_list,key):
    
    min_idx=0
    max_idx=len (in_list)-1
    
    while min_idx <= max_idx:
        mid =(min_idx + max_idx)//2
        
        if in_list[mid]==key:
            return mid
        elif in_list[mid]<key:
            min_idx=mid+1
        else:
            max_idx= mid -1
            
    return -1

l=[1,2,3,4,5,6,11,12,13,14,15]
print(binary_search(1,1))
print(binary_search(1,5))

      