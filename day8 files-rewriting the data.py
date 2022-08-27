# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 14:24:04 2022

@author: reddy.chandra
"""

'''files'''
with open("files.txt",'w') as f1:
    f1.write("how are you")
    lines=["im good"]
    f1.writelines(lines)
    
    
with open ("files.txt")as f1 ,open("file2.txt",'a') as f2:
    print(f1.closed)
    print(f1.tell())
    print(f2.tell())
    f2.writelines(f1.readlines())
    print(f1.readlines())
    
    print(f1.closed)
    
    
f1=open("file2.txt") 
print(f1.read())
print(f1.readlines())
f1.close()

f3=open("file3.txt")
print(f3.readlines())
print(f3.readline(2))
