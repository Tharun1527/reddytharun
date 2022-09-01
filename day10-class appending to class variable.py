# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 20:20:16 2022

@author: reddy.chandra
"""

class city:
     branches=[]
def __init__(self,name):
       self.name=name
       
location=city('chennai')
location.branches.append('hyderabad')

print(location.__dict__)     