# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 14:48:50 2022

@author: reddy.chandra
"""

'''properties'''

class customer:
    
    def set__name(self,name):
        print("set name",name)
        self.__name=name
        
    def get_name(self):
        print("get name")
        return self.__name
    
    name=property(get_name,set__name)

c=customer()
c.set__name("tharun")
print(c.get_name())
print()

c.name="chandra"
print(c.name)