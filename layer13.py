# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 03:05:52 2022

@author: MEGHA
"""


import turtle
from math import pi, cos, tan, sin

def deg2rad(d):
    return d *  pi/180

def arc20(R):
    return pi * R / 9

def layer13(turt, col1, col2):
    turt.width(3)
    turt.pencolor(col1)
    turt.fillcolor(col2)
    turt.begin_fill()
    for _ in range(18):
        s1 = 65 / cos(deg2rad(15))
        s2 = 2 * sin(deg2rad(15)) * s1
        turt.forward(s1)
        turt.left(45)
        turt.forward(s2)
        turt.left(120)
        turt.forward(s2)
        turt.left(45)
        turt.forward(s1)
        turt.left(170)
    
    turt.end_fill()
    
    turt.right(5)
    
    turt.width(1)
    
    def little_diamonds():
        turt.left(30)
        turt.fillcolor(col1)

        turt.begin_fill()        
        for _ in range(2):
            turt.forward(s2/4)
            turt.right(60)
            turt.forward(s2/4)
            turt.right(120)
        
        turt.end_fill()
        
    for _ in range(18):
        turt.penup()
        turt.forward(70)
        turt.pendown()
        little_diamonds()
        turt.left(150)   
        turt.penup()
        turt.forward(70)
        turt.right(160)

    