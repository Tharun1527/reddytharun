# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 15:03:33 2022

@author: reddy.chandra
"""

'''binary search tree'''
 
import sys
sys.setrecursionlimit(100)

class node :
    
    
    def __init__(self,data):
        self.__left=None
        self.__right=None
        self.__data=data
        
    def get_left_child(self):
        return self.__left
        
    def set_left_child(self,left):
        self.__left=left
        
    def get_rightchild(self):
        return self.__right
    
    def set_right_cjild(self,right):
        self.__right=right
        
    def get_data(self):
        return self.__data
    
    def set_data(self,data):
        self.__data=data
        
    def print_tree(self):
        if self.__left:
            self.__left.print_tree()
            
        print(self.__data)
        
        
        if self._right:
            self.__right.print_tree()
            
            
    def insert(head,node):
        if head == None:
            return node
        
        if node.get_data()<=head.get_data():
            head.set_left_child(insert(head.get_left_child(),node))
            
        else:
            head.set_right_child(insert(head))