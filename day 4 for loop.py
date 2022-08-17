# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 12:01:53 2022

@author: reddy.chandra
"""

'''for loop'''
'''counting text lower or upper'''


numbers=[1,2,3,4,5,6,7,8,9,10]

for output in numbers:
    if output > 7:
        break
    if output==5:
        continue
    print(output)






a=[1,2,3,4]
print(a)

for i in a:
     print(i*i)

b="THaRuN23"
print(b)

lower=0
upper=0
other=0
for c in b:
    print(c)
    
    if c.islower( ):
        lower += 1
        
    elif c.isupper( ):
        upper +=1
        
    else:
            other +=1
            
print("lower={}".format(lower))
print("upper={}".format(upper))
print("other={}".format(other))      

'''even numbers'''

c=int(input("enter the number "))


if (c % 2 == 0):
    
    print("{} is an even number".format(c))
    
else:
    print("{} is not an even mumber".format(c) )
print(c)






print(3!=4)
print("tharun"=="tharun")






