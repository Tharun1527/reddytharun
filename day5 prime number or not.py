# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 09:24:32 2022

@author: reddy.chandra
"""
'''checking prime number or not'''


num=int(input("enter the number"))
j= int(num/2)

print(num,j)

prime=False
if num == 2:
 print("{}is a prime number".format(num))    
else:
     for a in range(3,j):
         if (num% a)==0:
             break
         else:
             prime= True
             
     if prime==True:
        print("{} it is prime number".format(num))
     else:
        print("{}is not a prime number".format(num))
        
        
n=int(input("enter the number"))
for i in range(2,n):
    if (num%i)==0:
        print("{} it is not a prime number".format(n))
        break
    else:
        print("{} it is a prime number".format(n))