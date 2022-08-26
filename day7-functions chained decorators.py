# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 15:14:26 2022

@author: reddy.chandra
"""

'''chained decorators'''

def dash_highlighter(func):
    
    def highlight():
        print("-"*20)
        func()
        print("-"*20)
        
    return highlight

def caret_highliter(func):
    
    def highlight():
        print("^"*20)
        func()
        print("^"*20)
    return highlight
#@caret_highliter
#@caret_highliter
@dash_highlighter
@dash_highlighter
@caret_highliter
def print_message():
    print("hello")
    
        
print_message()