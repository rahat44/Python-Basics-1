#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 15 16:14:20 2020

@author: smrahman
"""

# 4. A palindrome is a phrase that, if reversed, would read the exact same.
# Write code that checks if p_phrase is a palindrome by reversing it and then checking if the reversed version is equal to the original.
# Assign the reversed version of p_phrase to the variable r_phrase so that we can check your work.

p_phrase = "was it a car or a cat I saw"
r_phrase = p_phrase[::-1]
print(r_phrase)
