#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 16:34:57 2020

@author: smrahman
"""


import turtle
wn = turtle.Screen()

elan = turtle.Turtle()

distance = 50
angle = 90
for _ in range(120):
    elan.forward(distance)
    elan.right(angle)
    distance = distance + 1
