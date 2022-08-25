# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 18:37:01 2022

@author: reddy.chandra
"""

'''functions'''

import datetime

def current_timestamp():
    print(datetime.datetime.now())
    """
    this function is used to prin the current date and time
    """
    
current_timestamp()

for i in range(10):
    current_timestamp()
  
print(current_timestamp.__doc__)
currenttim=current_timestamp
print(currenttim)

name="canon"
model="R5"
def camera():
    print("this camera {} is made by {}".format(model,name))
camera()

pc_camera=camera
pc_camera()
model='R6'
pc_camera()
