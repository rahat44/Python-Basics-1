#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  9 03:07:26 2020

@author: smrahman
"""

import turtle            # set up alex
wn = turtle.Screen()
alex = turtle.Turtle()

for aColor in ["yellow", "red", "purple", "blue"]:
    alex.color(aColor)
    alex.forward(50)
    alex.left(90)

wn.exitonclick()
