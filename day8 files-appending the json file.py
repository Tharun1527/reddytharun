# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 12:08:07 2022

@author: reddy.chandra
"""
'''appendening the json file'''
import json
import datetime
d={}
d['customer']='chandra'
d['adrs']='chennai'
d['product']='mobile'
d['price']=20000
d['buyed on']=str(datetime.datetime.now())



file_str=json.dumps(d)
print(file_str)



with open("jason.txt","a") as f:
 json.dump(d,f,indent=4,separators=("*","$$"))

 
 
 
 print(f.closed)