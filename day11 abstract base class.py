# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 16:46:05 2022

@author: reddy.chandra
"""

'''abstract classes'''
'''abstract base class'''

from abc import ABC,abstractmethod

class vehicle(ABC):
 
      @abstractmethod
      def wheels(self):
          pass
      def print_info(Self):
          print("this is a vechicle")
        
class car(vehicle):
    def wheels(self):
        print("cars have four wheels")
          
#v=vehicle()
#v.wheels()
#v.print_info()
      

c=car()
c.wheels()
c.print_info()