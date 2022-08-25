# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 20:08:30 2022

@author: reddy.chandra
"""

'''Recursion'''
import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(100)
print(sys.getrecursionlimit())






def fn(n):
    print("begin",n)
    print(n)
    if n<=0:
        print("end",n)
        return
    else:
      fn(n-1)
      print("end",n)
      
fn(10)

def fn2(n):
    print("begin",n)
    print(n)
    if n>0:
        print("end",n)
        fn2(n-1)
        print("end",n)
      
fn2(5)
