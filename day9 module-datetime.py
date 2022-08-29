# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 23:17:13 2022

@author: reddy.chandra
"""

'''modules'''


import datetime
import time


print(datetime.datetime.now())
print(datetime.date.today())
print(datetime.datetime.now().strftime("%Y-%m-%d  %H:%S:%f"))

a=datetime.datetime.now()
time.sleep(5)
b=datetime.datetime.now()
diff=a-b
print(diff)