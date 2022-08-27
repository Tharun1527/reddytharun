# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 01:08:16 2022

@author: reddy.chandra
"""

'''jason files'''
'''javascript object notation '''
'''acessing the json file'''


import json

with open('jason.txt') as f:
    
    details=json.load(f)
    print(details)
    print(details["address"]["colony"])
    print(details["name"])