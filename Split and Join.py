#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  8 18:17:09 2020

@author: smrahman
"""

song = "The rain in Spain..."
wds = song.split()
print(wds)

song = "The rain in Spain..."
wds = song.split('ai')
print(wds)


wds = ["red", "blue", "green"]
glue = ';'
s = glue.join(wds)
print(s)
print(wds)

print("***".join(wds))
print("".join(wds)) #empty str
