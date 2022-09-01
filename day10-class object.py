# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 12:24:45 2022

@author: reddy.chandra
"""
class computer:
    
    
   def __init__(self,cpu,ram):
       self.cpu=cpu
       self.ram=ram
       

   def config(self):
       print("the  is",self.cpu,self.ram)

   def get(self):
       return self.cpu,self.ram

comp1=computer("i5",'16 gb ram')
comp2=computer("reyzen",'8 gb ram')
#comp3=computer()
#computer.config(comp1)
#computer.config(comp2)
print(comp1.cpu)
print(comp1.ram)
print(comp2.cpu)
print(comp2.ram)
comp1.config()
comp2.config()
#comp3.config( )
print(comp1.__dict__)
print(comp2.__dict__)