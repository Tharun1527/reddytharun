# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 01:35:04 2022

@author: reddy.chandra
"""
'''classes'''


class bank():
    name="NAME"
    
    def __init__(self):
        print("intializing")
        self.ho="bengaluru"
    def get_ho(self):
        return self.ho

sbi= bank()

print(sbi.__doc__)
print(sbi.__dict__)
print(sbi.name)
print(sbi.get_ho())
print (sbi.ho)
bank.name = "SBI"
print(sbi.__dict__)
sbi.ho="mumbai"
print(sbi.ho)

rbi=bank()
print(rbi.name)