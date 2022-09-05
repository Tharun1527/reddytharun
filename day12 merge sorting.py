# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 14:09:29 2022

@author: reddy.chandra
"""

'''merge sort'''

def merge(in_list,l,m,r):
    n1=m-l+1
    n2=r-m
    print("n1",n1)
    print("n2",n2)
    
    L=[0]*(n1)
    R=[0]*(n2)
    
    
    i=0
    j=0
    k=l
    
    while i <n1 and j<n2:
        if L[i]<= R[j]:
            in_list[k]=L[i]
            i+=1
            
        else:
            in_list[k]=R[j]
            j+=1
        k+=1
        
    while i<n1:
        in_list[k]=L[i]
        i+=1
    
        
    while j<n2:
        in_list[k]=R[j]
        j+=1
        k+=1
        
def merge_sort(in_list,l,r):
    
    if l<r:
        
        mid=(l+r)//2
        
        merge_sort (in_list,l,mid)
        merge_sort (in_list,mid+1, r)
        merge(in_list,l,mid,r)
        
l=[5,4,3,2,100,0]
print(l)
merge_sort(l,0,len(l)-1)
print(l)