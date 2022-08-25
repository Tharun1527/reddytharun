# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 00:59:47 2022

@author: reddy.chandra
"""

'''calculate total expenses'''

salary=10000
total_expenses=0
savings=0

def rent_expenses():
    global total_expenses
    total_expenses +=1000
    
def food_expenses():
    global total_expenses
    total_expenses +=2000
    
def travel_expenses():
    global total_expenses
    total_expenses=3000
    
def saving():
    global salary,total_expenses,savings
    savings= salary- total_expenses
def calculate_savings():
    rent_expenses()
    food_expenses()
    travel_expenses()
    saving()
    
print(salary)
print("init expenses",total_expenses)
calculate_savings()
print("final expenses", total_expenses)
print("savings",savings)