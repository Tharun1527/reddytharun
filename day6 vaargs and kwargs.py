# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 00:54:04 2022

@author: reddy.chandra
"""

'''varargs and kwargs'''

def print_info(*args,**kwargs):
    print(args)
    print(kwargs)
    
print_info("A","B",name='mphasis',loc="bengaluru")