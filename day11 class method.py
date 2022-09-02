# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 16:18:33 2022

@author: reddy.chandra
"""

'''class method'''


class customer4:
    
    __savings_rate=.04
    
    def __init__(self,name,amount):
        self.__name=name
        self.__amount=amount
    
    
    @property
    def name(self):
        """
        get name

        Returns
        -------
        None.

        """
        print("get name")
        return self.__name 
    
    @name.setter
    def name(self,name):
       print("set name",name)
       self.__name=name
     
    def print_intrest(self):
       print("intrest =",(self.__amount *self.__savings_rate))
       
    @property
    def amount(self):
       return self.__amount
   
    @amount.setter
    def ac_type(self,amount):
       print("set amount",amount)
       self.__amount=amount
       
       
    @classmethod
    
    def get_savings_rate(cls):
        
        return cls.__savings_rate
    
    @classmethod
    def set_savings_rate(cls,rate):
       cls._savings_rate=rate
       
       
c=customer4("nadal",1000)
print(c.name,c.amount,customer4.get_savings_rate())
print(c.name,c.print_intrest())