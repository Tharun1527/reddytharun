# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 14:21:02 2022

@author: reddy.chandra
"""

class myclass:
    
    def __init__(self,number):
        self.__number=number
        
    def __add__(self,other):
        return self.__number +other.__number
    
    def __sub__(self,other):
        return self.__number -other.__number
    def __mul__(self,other):
        return self.__Number *other.__number 
    def __floordiv__(self,other):
        return self.__number//other.__number
       
    
a=myclass(10)
b=myclass(5)


print("add",a+b)
print("sub",a-b)
print("fd",a//b)