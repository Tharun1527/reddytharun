# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 11:15:23 2022

@author: reddy.chandra
"""

'''time complexity

O(m)*O(n)'''

def find_prime(start,end):
    num_iterations =0
    for i in range(start,end):
        
        for j in range(2, i//2):
            num_iterations +=1
            if i%j==0:
                break
        else:
            print(i)
            
    print("iterations",num_iterations)
    
find_prime(11,20)
find_prime(21,30)
find_prime(111,120)
find_prime(121,130)