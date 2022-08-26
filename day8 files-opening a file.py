# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 19:08:50 2022

@author: reddy.chandra
"""
'''files'''

with open('files.txt') as f:
    print(f.fileno())
    print(f.tell())
    print(f.closed)
    data=f.read(20)
    print(data)
    print(f.tell())
    f.seek(10)
    print(f.tell())
    data=f.read()
    print(data)
    print(f.tell())

print(f.closed)


f2=open('file2.txt')
print(f2.fileno())
print(f2.tell())
data=f2.read()
print(data)
f2.seek(0)
print(f2.tell())
data=f2.read()
print(data)
print(f2.closed)
f2.close()
print(f2.closed)
data=f2.readline( )
print(data)
data=f2.readlines()
print(data)
for line in data:
    print("2nd char is",line[2])
print(data)