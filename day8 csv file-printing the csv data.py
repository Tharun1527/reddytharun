# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 23:56:04 2022

@author: reddy.chandra
"""
'''csv file printing'''

import csv

with open("first.csv")as f1:
    lines=csv.reader(f1)
    
    for line in lines:
        print (line)