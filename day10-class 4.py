# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 13:03:28 2022

@author: reddy.chandra
"""

class bank:
    
    def __init__(self,name,ho):
        self.name=name
        self.ho=ho
        
sbi=bank("SBI",'CHENNAI')

print(sbi.__dict__)


sbi.ho="bengaluru"
print(sbi.__dict__)

sbi._bank_ho='mumbai'
print(sbi.__dict__)

sbi._bank_ho="hyderabad"
print(sbi.__dict__)