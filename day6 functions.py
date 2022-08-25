# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 19:14:19 2022

@author: reddy.chandra
"""

'''functions *args and **kwargs'''

def my_print(*args):
    print("Hello")
    print(args)
    
my_print('hello2')

def my_print2(args,name):
    print(args)
    print(name)


def my_print3(*name3,**company):
    print(name3)
    print(company)

def my_print4(*name4,**location):
    print(name4)
    print(location)
    

    
    
my_print('hello2')
my_print2(name='tharun',args='how are you')   
my_print3(name="chandra",company="mphasis")
my_print4(name4='reddy',location='chennai')
