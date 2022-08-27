# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 22:33:12 2022

@author: reddy.chandra
"""
import os
with open("files.txt",'w')as f1:
    print(os.stat("files.txt").st_size)
    for i in range(50):
        f1.write("line" +str(i)+ "\n")
        
with open("files.txt",'a') as f2:
      print(os.stat("files.txt").st_size)
      for i in  range(30):
          f2.write("line"+str(i)+"\n")
          