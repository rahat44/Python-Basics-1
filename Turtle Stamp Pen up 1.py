#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 15:49:25 2020

@author: smrahman
"""

import turtle
wn = turtle.Screen()
rahat = turtle.Turtle()
rahat.shape("turtle")
rahat.speed(7)
rahat.penup()
for size in range(10):
    rahat.forward(50)
    rahat.stamp()
    rahat.forward(-50)
    rahat.right(36)
wn.exitonclick() 
   
