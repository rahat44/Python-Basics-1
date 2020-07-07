#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 14:35:48 2020

@author: smrahman
"""


print(3.14, int(3.14))
print(3.9999, int(3.9999))       # This doesn't round to the closest int!
print(3.0, int(3.0))
print(-3.999, int(-3.999))        # Note that the result is closer to zero

print("2345", int("2345"))        # parse a string to produce an int
print(17, int(17))                # int even works on integers
#print(int("23bottles"))           # you have to use str instead of int

print(str("23bottles"))

print(float("123.45"))
print(type(float("123.45")))

print(str(17))
print(str(123.45))
print(type(str(123.45)))




