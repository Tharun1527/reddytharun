# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 19:00:00 2022

@author: reddy.chandra
"""
'''exceptions on existing file'''
import sys 

try:
    f=open("file46.txt")
except:
    print("not found")
    print(sys.exc_info())
    print(sys.exc_info()[0].__name__)
else:
    print("^"*20)
    print(f.read())
    print("^"*20)
#finally:
   # f.close()
    #print("closing")
    