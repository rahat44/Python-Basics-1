#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 21:12:50 2020

@author: smrahman
"""

print(1 + 1 + (2 * 3))
print(len("hello"))

print("Program")

y = 3.14
x = len("hello")
print(x)
print(y)

print("Program")
print(2 * len("hello") + len("goodbye"))

print("Program")

def square(a):
    return a * a
	
def sub(a, b):
    return a - b

a = 2
b = 1

print(square(b + 3))
print(square(b + square(a)))
print(sub(square(b), square(a)))