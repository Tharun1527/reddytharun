# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 22:51:31 2022

@author: reddy.chandra
"""

''' repr and str'''

class account:
     def __init__(self,name,balance):
         self.__name=name
         self.__balance = balance
         self.__txn_count=1
         print("account opening balances is ",balance)

     def deposit(self,amount):
         self.__amount+=amount
         self.__txn_count+=1
         
         print("deposit{},current bal {}".format(amount,self.__balance))
     def withdraw(self,amount):
         self.__balance -=amount
         self.__txn_count +=1
         
         print("withdraw {} as balance is{}".format(amount,self.__balance))
         
     def __repr__(self):
        return"{} has{} as balance. number of transactions is {}".format(self.__name__,self.__balance__)
        
     def __str__ (self):
        return "{}has {} as balnce".format(self.__name,self.__balance)
    
a=account('john',10000)
a.deposit(1000)
a.deposit(1000)
a.withdraw(1500)

print(a)
a.withdraw(2500)
print(a)
print('*'*10)
print(repr(a))
print('*'*10)
b=repr(a)
print(b)    