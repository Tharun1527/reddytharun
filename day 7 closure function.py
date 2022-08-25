# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 10:00:41 2022

@author: reddy.chandra
"""

'''closure'''


def fn1(x):
    def fn2():
        print("Hello",x)
    
    return fn2

f=fn1("mphasis")
f()
fn1("ABCD")()
#del fn1


f()
f2=fn1("bengaluru")
f()
f2()
