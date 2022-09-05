# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 12:06:24 2022

@author: reddy.chandra
"""

'''selection sort'''

def selection_sort(in_list):
    length = len(in_list)
    
    for i in range(length):
        min_val_index=i
      
        for j in range(i +1,length):
            if in_list[min_val_index]>in_list[j]:
                min_val_index=j

        in_list[i],in_list[min_val_index]=in_list[min_val_index],in_list[i]
        
        print("sorted till",i)
        print(in_list)
    
    print("sorted list")
    print(in_list)
    
    
l=[1,3,4,2,5]
print(l)
selection_sort(l)

'''l=[i for i in range(10,0,-1)]
print(l)
selection_sort(l)'''
