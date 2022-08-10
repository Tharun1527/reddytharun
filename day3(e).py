# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 02:06:56 2022

@author: reddy.chandra
"""

'''
dictionaries
'''
w={}
print(w)
print(type(w))

w={"asdf":2,"wergt":50,"kuyl":80}
print(w)
w["kuyl"]=30

print(w)
print(w.values())
w["tharun"]=23
print(w)
print(w.keys())
print(list(w.values()))
name=["arun","chandra"]
age=[23,25]
details=dict(zip(name,age))
print(details)
a=100
b=300
print(a,b, sep=':::')
a=10,20
print(a,b,sep="////")
print(w.get("kuyl"))
w.pop("tharun")
print(w)
print(w.pop("asdf"))
print(w)
print(details.items())
print(list(details.items()))
print(tuple(details.items()))
