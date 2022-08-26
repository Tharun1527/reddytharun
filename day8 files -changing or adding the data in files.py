# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 23:48:59 2022

@author: reddy.chandra
"""
'''changing or adding the data in files'''

f3= open("file2.txt","w")
print(f3.fileno())
print(f3.tell())
print(f3.closed)
    
f3.seek(15)
print(f3.tell())
f3.write("hi my name is tharun")
f3.write("mphasis is the best place to work")
f3.write("323")
print(f3.closed)
data=(f3.read())
print(data)
lines=['1','2','3']
f3.writelines(lines)
print(f3.mode)
