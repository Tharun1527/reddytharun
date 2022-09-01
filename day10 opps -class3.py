# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 10:48:52 2022

@author: reddy.chandra
"""
class Items:
    
    price_step=1.02
    
    def __init__(self,name,price):
        self.name=name
        self.price=price 
     
    def inc_price(self):
        self.price=self.price*Items.price_step
        
    def dec_price(self):
        self.price=self.price/Items.price_step
  

i1=Items('rice',30)
print(i1.price_step)
print(Items.price_step)
print(i1.price)
i1.inc_price()
print(i1.price)
i1.dec_price()
print(i1.price)
Items.price_step=2.0
i2=Items("dal",110)
print("dal price step",i2.price_step)
i2.inc_price()
print(i2.price)