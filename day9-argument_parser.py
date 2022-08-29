# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 16:52:10 2022

@author: reddy.chandra
"""
'''argument list'''

import argparse

parser=argparse.ArgumentParser()
parser.add_argument('---display')

args= parser.parse_args()

print(args._get_args())
print(args.display)