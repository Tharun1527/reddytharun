# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 13:31:07 2022

@author: reddy.chandra
"""

"""celsius to farenheit"""

celcius=range(-200,200,10)
farenht=[(9/5)*x+ 32 for x in celcius]
print(celcius)
print(farenht)

dict=dict(zip(celcius,farenht))
print(dict)