# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 08:28:11 2022

@author: reddy.chandra
"""
'''swaping the data from one file to another file'''


with open("file3.txt")as f1 , open("file2.txt",'w') as f2:
    f2.writelines(f1.readlines())
'''w will erase the previous data add the new data which we add
it will write the data only'''
    
with open("file2.txt",'w') as f3:
    print(f3.tell())
    f3.write('hii tis is tharun')
    
'''a it will append the data to from one file to another files it works as copy'''

with open("file3.txt") as f1,open("file2.txt",'a') as f2:
    print(f2.tell())
    f2.writelines(f1.readlines())
    