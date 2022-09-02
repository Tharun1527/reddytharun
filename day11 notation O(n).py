# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 01:46:58 2022

@author: reddy.chandra
"""

'''time complexity
O(n)
'''

def prime1(n):
    
    num_iterations=0
    
    
    for i in range(2,n):
        num_iterations+=1
        if n%i == 0:
            print("{} is not a prime".format(n))
            break
        else:
            print("{} is prime".format(n))
        print("iterations",num_iterations)
         
def prime2(n):
    
    num_iterations =0

    for i in range (2,n//2):
        num_iterations +=1
        if n%i ==0:
            print("{} is not prime".format(n))
            break
        else:
            print("{} is prime".format(n))
            
            print("iterations",num_iterations)
        
        
prime1(3)
prime1(4)
prime1(30)
prime1(53)
prime1(101)
prime1(1013)


for i in range(30):
    print('*'* 10)
    print(i)
    print("prime1")
    prime1((2**i)-1)
    print("prime2")
    prime2((2**i)-1)
    
