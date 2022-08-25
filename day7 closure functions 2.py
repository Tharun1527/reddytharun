# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 10:09:21 2022

@author: reddy.chandra
"""

'''
closure'''

def create_cart(customer):
    cart=[]
    
    def add_to_cart(item):
        cart.append(item)
        print(item,"added for" ,customer)
        print(customer,"\n",cart)
        return cart
    return add_to_cart
    
john=create_cart("john")
marie=create_cart("marie")
john("bread")
john(["bread","jam"])
marie("apple")
marie(["mango","grapes"])

print(john("Rice"))