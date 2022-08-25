# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 11:39:14 2022

@author: reddy.chandra
"""

'''functions'''

p=print
p("helll")


def print_hello():
    print("Hello!!!")
    
print_hello()

def print_func(name,adress):
     print("my name is ",name,"im from ",adress)
     print_func("tharun chandra","warangal")
     
     
     
     

def cal_int(principal,rate,duration):
    if rate<=0:
        print("no intreset")
        return principal
    
    intrest= principal*rate/ 1000*duration
    
    return intrest   
p=100000 
r=0
d=2
cal_int(p,r,d)
