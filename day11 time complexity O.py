# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 02:56:51 2022

@author: reddy.chandra
"""

'''time complexity'''


'''o(n*n)'''


'''print pairs of list'''

def print_pairs(data):
    num_iterations=0
    n=len(data)
    
    for i in range(n):
        for j in range(n):
            num_iterations+=1
            print("[{} {}]".format(data[i],data[j]),end="")
            
        print()
        
    print("number of iterations", num_iterations)
print_pairs([1,2])
print_pairs([1,2,3])
print_pairs([1,2,3,4])