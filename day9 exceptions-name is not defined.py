# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 18:22:10 2022

@author: reddy.chandra
"""

'''exceptions'''

import sys

asds=10
try:
    print(asds)
except:
    print("define the value ")
    print(sys.exc_info()[1])
finally:
       print("Finally") 