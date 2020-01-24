# -*- coding: utf-8 -*-
# Exercise 3.2.4
# This code is used to print a specific string four times
# created by Tianle Xu on 1/17 and modified on 1/24
# modify do_twice function
def do_twice(f, x):
    f(x)
    f(x)
 # define print_twice function   
def print_twice(x):
    print(x)
    print(x)
d = 'spam'
do_twice(print_twice, d)
