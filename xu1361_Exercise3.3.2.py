#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 2020
Modified on Fri Jan 24 2020
@author: xu1361
"""
# This code aims to draw a 4 by 4 grid

# Define do_twice function
def do_twice(f):
    f()
    f()
    
# Define do_four function
def do_four(f):
    do_twice(f)
    do_twice(f)
    
# Define the function to draw the row
def line1():
    print('+ - - - -', end = ' ')
    
# Define the function to draw the column
def line2():
    print('|        ', end = ' ')
def row1():
    do_four(line1)
    print('+')
def row2():
    do_four(line2)
    print('|')
    
# Define print_fourth function
def print_fourth(f):
    do_twice(f)
    do_twice(f)
def grid_part():
    row1()
    print_fourth(row2)
def grid():
    do_four(grid_part)
    row1()
    
grid()