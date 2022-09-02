# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 01:13:56 2022

@author: reddy.chandra
"""

'''static method'''

class customer:
     
     @staticmethod
     def split_name(name):
         return name.split(',')
     
     def __init__(self,name):
            self.__name=name
            
     def get_name(self):
            return self.__name
        
a=customer("federer,roger")
print(customer.split_name(a.get_name()))
