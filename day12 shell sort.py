# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 12:53:29 2022

@author: reddy.chandra
"""

'''
shell sort'''

def shell_sort(in_list):
    
    length= len(in_list)
    gap =length // 2
    
    print('gap=',gap)
    
    while gap > 0:
        for i in  range (gap,length):
            temp =in_list[i]
            
            j=i
            
            while j>=gap and in_list[j -gap]>temp:
                in_list[j]=in_list[j-gap]
                j -=gap
                
            in_list[j]=temp
            
            print("gap",gap)
            print(in_list)
            
        gap=gap // 2
        
l=[2,5,3,6,4,7]
print(l)
print(shell_sort(l))


l=[ i for i in range(5,-5,-1)]
print(l)
#print(shell_sort(1))