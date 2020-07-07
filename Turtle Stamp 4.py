#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 16:33:09 2020

@author: smrahman
"""

import turtle
wn = turtle.Screen()
amee = turtle.Turtle()
amee.shape("turtle")
amee.penup()
for size in range(10):
    amee.forward(20)    #distance between turtles
    amee.stamp()
wn.exitonclick()