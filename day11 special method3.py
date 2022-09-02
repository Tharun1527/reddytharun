# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 14:35:33 2022

@author: reddy.chandra
"""

class Attendees :
     def __init__(self,session):
         self.__session=session
         self.__attendees=set()
         
     def add_attendee(self,name):
         self.__attendees.add(name)
         print(self.__attendees)
         
     def __len__(self):
        return len(self.__attendees)
 
        
p=Attendees("python")
p.add_attendee("A")
p.add_attendee("b")
p.add_attendee("C")


 