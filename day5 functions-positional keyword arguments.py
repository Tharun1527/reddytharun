# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 13:03:12 2022

@author: reddy.chandra
"""

'''
fuctions
'''

def details(name, age, company):
   
    print("*"* 10)
    print(name)
    print(age)
    print(company)
    if age>20:
        print("age is greater than 20")
    else:
        print("cannot work")
        
details("tarun",23,"mphasis")
details(name="cahndra",age=15,company="hcl")
print("*"*10) 

details("dsade",30,"qcsdc")
details("brgbv",age=20,company="vefw")
#details("csdc",age=44,"DCSFD")
#it takes the positional argument first and keyword argument second
