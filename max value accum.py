#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 15 23:40:07 2020

@author: smrahman
"""

nums = [9, 3, 8, 11, 5, 29, 100]
best_num = 0
for n in nums:
    if n > best_num:
        best_num = n
print(best_num)


