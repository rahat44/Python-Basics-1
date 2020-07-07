#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 23:35:22 2020

@author: smrahman
"""

#right angle

import turtle
 
board = turtle.Turtle()
 
board.forward(100) # draw base
 
board.left(90)
board.forward(100)
 
board.left(135) # angle (180-135)=45
board.forward(141.42) #use pythagorus 141.42
 
turtle.done()