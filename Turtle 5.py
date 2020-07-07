#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 17:21:25 2020

@author: smrahman
"""

import turtle
wn = turtle.Screen()             # Set up the window and its attributes
wn.bgcolor("red")


tess = turtle.Turtle()           # create tess and set his pen width
tess.color("orangered")  
tess.pensize(5)

alex = turtle.Turtle()           # create alex
alex.pensize(4)
alex.color("maroon")            # set his color

tess.forward(80)                 # Let tess draw an equilateral triangle
tess.left(120)
tess.forward(80)
tess.left(120)
tess.forward(80)
tess.left(120)                   # complete the triangle

tess.right(180)                  # turn tess around
tess.forward(80)                 # move her away from the origin so we can see alex

alex.forward(50)                 # make alex draw a square
alex.left(90)
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)

wn.exitonclick()
