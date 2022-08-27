# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 00:01:32 2022

@author: reddy.chandra
"""
'''csv to dict'''
import csv

with open("first.csv")as f1:
    lines=csv.DictReader(f1)
    ages=[]
    for line in lines:
        print(dict(line))
        print("Name is" , dict(line)[' name'])
        ages.append(int(dict(line)['age']))

print(ages)
print(sum(ages))