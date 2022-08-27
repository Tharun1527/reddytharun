# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 00:25:43 2022

@author: reddy.chandra
"""
'''writing the data into the csv files'''

import csv

data=[[1,'Tharun','hyderabad'],
      [2,'ascc','chennai'],
      [3,'vadfv','banglore'],
      [4,'sadcc','pune']]
with open("2nd file.csv","w") as f:
    writer=csv.writer(f)
    
    '''for row in data:
        writer.writerow(row)'''
        
    writer.writerows(data)
        