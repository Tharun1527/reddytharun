# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 11:16:57 2022

@author: reddy.chandra
"""

'''multiplication table'''

for i in range(1,21):
    print("multiplication table for {}".format(i))
    for j in range(1,11):
        print("{:2d}*{:2d}={:3d}".format(i,j,(i*j)))
        
        print()