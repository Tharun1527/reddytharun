# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 22:06:30 2022

@author: reddy.chandra
"""

'''if condition'''


a=100
b=100

if a>b:
      print("a>b")
      a -= 900
elif a==b :
     print("a is equal to b")
     a -= 9
      
else:
      print("a<b")
      a -= 1
        
print(a)        
print("end") 

c=10
d=30

if c > d:
     print ("c>d")
     c -=1
     
if c<d:
     print("d greater than c")
     d += 1

print(d) 
print("end")    




e=500
f=300
if e>f:
    print("e is greater than f")
    e +=10
elif e<f :
      print("e <f")
if e==f:
    print("e ==f")
    e -= 20
    
print(e)

print("=========================")

if not e>f:
    print("@@@@")
else:
    print("#####")




## true value else condition
h= e if e>f else e<f
print(h)

name ="tharun"
location="chennai"
if name=="tharun" and location=="chennai":
    print("true")
    
if "t" in name:
    print("found")
else:
    print("not found")
