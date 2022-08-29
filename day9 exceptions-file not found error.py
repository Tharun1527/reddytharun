# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 18:36:10 2022

@author: reddy.chandra
"""


import sys



try:
    f= open("sfdcad.txt")
    
#except:
 #   print("sdccffv")
    
except FileNotFoundError:
    print("file not found error")
    print("aan error occured----",sys.exc_info()[0].__name__)
    
except OSError:
    print("an error occured")