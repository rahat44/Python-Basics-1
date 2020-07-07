#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 20:21:39 2020

@author: smrahman
"""

import turtle
wn = turtle.Screen()

elan = turtle.Turtle()

distance = 50
for _ in range(20):
    elan.forward(distance)
    elan.right(68)
    distance = distance + 10
