# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 22:28:24 2022

@author: reddy.chandra
"""


'''polymorphesium'''
class  account:
    def __init__(self,balance):
        self._balance=balance
        print("opening balance",self._balance)

        def deposit(self,amount):
            self._balance+=amount
            print("deposit",amount)
            print("balance",self._balance)
            
        def withdraw(self,amount):
            self._amount-=amount
            
            print("withdraw",amount)
            print("balance",self._balance)
            
class curentaccount(account):
    
    def _init_(self,balance):
        super()._init_(balance)
        
    def withdraw(self,amount):
        if amount>20000:
            print("not alllowed")
            
        else:
            super().withdraw(amount)
print("account")
a1=account(10000)
#a1=deposit(1000)#a1.withdraw(500)

print("curent account")
c1=curentaccount(10000)
c1.deposit(1000)
c1.withdraw(500)
c1.withdraw(2500)

         
        
        
    
            

