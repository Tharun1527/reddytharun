# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 12:43:38 2022

@author: reddy.chandra
"""

'''insertion sort'''

def insertion_sort(in_list):
    length=len(in_list)
    for i in range(length -1):
        for j in  range(i +1,0,-1):
    
            if in_list[j]<in_list[j-1]:
                in_list[j],in_list[j-1]=in_list[j-1],in_list[j]
        print("sorted till",i)
        print(in_list)
         
    print("sorted list")
    print(in_list)
    
l=[1,3,4,2,4]
print(l)
insertion_sort(l)
    
    