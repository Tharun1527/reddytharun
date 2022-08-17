# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 09:49:35 2022

@author: reddy.chandra
"""

import datetime

start=10
end=20

print("Begin at {}".format(datetime.datetime.now()))
for num in range(start,end):
    j=int(num/2)
    
    prime= False
    if num==2:
        print("{} is a pime number".format(num))
    else:
        for a in range(2,j):
            if(num % a)== 0:
                break
        else:
            prime== True
        if prime==True:
            print("{} is a prime number".format(num))
        else:
            print("{}is not a prime number".format(num))
else:
    print("Generation complete")
print("end at{}".format(datetime.datetime.now()))