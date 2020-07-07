#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 02:48:13 2020

@author: smrahman
"""

n = input("Please enter your name: ")
print("Hello", n)

# Here is a program that turns a number of seconds into more human 
# readable counts of hours, minutes, and seconds. 

str_seconds = input("Please enter the number of seconds you wish to convert")
total_secs = int(str_seconds)

hours = total_secs // 3600
secs_still_remaining = total_secs % 3600
minutes =  secs_still_remaining // 60
secs_finally_remaining = secs_still_remaining  % 60

print("Hrs=", hours, "mins=", minutes, "secs=", secs_finally_remaining)

# What is printed when the following statements execute? Ans: <class 'str'>
n = input("Please enter your age: ")
# user types in 18
print(type(n))