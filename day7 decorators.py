# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 10:34:04 2022

@author: reddy.chandra
"""

'''decorators'''


'''def print_info(name):
    print("*"* 20)
    print("hello",name)
    print("*"*20)
    
print_info("mphasis")'''


def make_high_light(func):
    def hight_light(*args):
        print("*"*20)
        func(*args)
        print("*"*20)
    return hight_light

#a=make_high_light("hello")
#print(a)
import datetime

@make_high_light 
def print_message():
    
    print("hello world")
    print(datetime.datetime.now())
@make_high_light 
def print_message2(msg2):
    print("new message",msg2)
    
print_message()
print_message2("how are you")
print_message2("i am fine")
