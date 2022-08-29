# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 00:25:53 2022

@author: reddy.chandra
"""

'''modules'''
import os

print(os.getcwd())
print(os.path.dirname.__doc__)


print(os.listdir())
#os.mkdir("afafg")
#os.rename("afafg","tharun")
#os.rmdir("tharun")
print(os.path.isdir(os.getcwd()))
print(os.path.isfile(os.getcwd()))