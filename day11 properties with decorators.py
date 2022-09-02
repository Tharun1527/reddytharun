# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 15:04:29 2022

@author: reddy.chandra
"""

'''properties using decorators'''

class customer2:
    
    def __init__(self,name):
        self.__name=name
        
    @property
    def name(self):
        print("get name")
        return self.__name 
    
    @name.setter 
    def name(self,name):
        print("set name",name)
        self.__name=name
        
    @name.deleter
    def name(self):
        print("delete")
        del self.__name 
        
c=customer2("tharun")
print(c.name)
c.name='federer'
del c.name
print(c.name)

    