# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 14:25:20 2022

@author: reddy.chandra
"""

'''quick sort'''

def partition(in_list,start_idx,end_idx):
    curr_idx=start_idx
    pivot=in_list[end_idx]
    
    for i in range(start_idx,end_idx):
        if in_list[i]<=pivot:
            in_list[i],in_list[curr_idx]=\
            in_list[curr_idx],in_list[i]
            
            curr_idx +=1
            
            
    in_list = [curr_idx],in_list[end_idx]=\
        in_list[end_idx],in_list[curr_idx]
        
        
    return curr_idx

def quick_sort(in_list,start_idx,end_idx):
    if start_idx > = end_idx:
    return 
 
    part_idx=partition(in_list,start_idx,end_idx)
    
    print("element {} is in its right place".format(in_list[part_idx]))
    print(in_list)
    
    
    quick_sort(in_list,start_idx,part_idx-1)
    quick_sort(in_list,part_idx +1, end_idx)
    
l= [5,4,3,2]

print(l)
quick_sort(l,0,len(l)-1)
print(l)

