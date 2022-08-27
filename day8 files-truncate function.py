# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 22:54:04 2022

@author: reddy.chandra
"""

'''truncate'''
with open("files.txt","a")as f1:
    for i in range(100):
        f1.write("line"+"\n")
        
with open("files.txt","w") as f2:
   f2.truncate()
 #   print(f2.tell())
  #  f2.seek(1)
   # print(f2.tell())
    #f2.write("hi")
