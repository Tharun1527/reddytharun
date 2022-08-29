# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 19:54:33 2022

@author: reddy.chandra
"""

import argparse

parser=argparse.ArgumentParser(description='add integers')

parser.add_argument('-x',
                     '--first-arg',
                      required=True,
                      help='first integer')
parser.add_argument('-y',
                    '--second integer',
                    required=True,
                    help='seconf integer')
print(parser.parser.parse_args())
args=vars(parser.parse_args())
print(args)
x=int(args['first_arg'])
y= int(args['second_arg'])
print("sum=",(x+y))