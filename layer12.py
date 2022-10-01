# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 22:10:36 2022

@author: MEGHA
"""


import turtle
from math import pi, cos, tan, sin

def deg2rad(d):
    return d *  pi/180

def arc20(R):
    return pi * R / 9

def layer12(turt, col1, col2):
    turt.width(3)
    turt.pencolor(col1)
    move = 80 / cos(deg2rad(10))
    r = 80 * tan(deg2rad(10))
    forw = deg2rad(r)
    
    
    for _ in range(18):
        turt.forward(move)
        turt.left(10)
    
        turt.forward(forw/2)
        for _ in range(179):
            turt.left(1)
            turt.forward(forw)

        turt.left(1)
        turt.forward(forw/2)

        turt.left(10)
        turt.forward(move)
        turt.left(180)
    
    turt.width(2)
    turt.pencolor(col2)
    turt.left(10)
    turt.fillcolor(col1)
    
    def little_circles():
        turt.forward(forw/4)
        
        for _ in range(359):
            turt.right(1)
            turt.forward(forw/2)
            
        turt.right(1)
        turt.forward(forw/4)

    for _ in range(18):
        turt.forward(80-r/2)
        turt.left(90)
        
        turt.begin_fill()
        little_circles()
        turt.end_fill()
        
        turt.left(90)
        turt.forward(80-r/2)
        turt.right(160)
