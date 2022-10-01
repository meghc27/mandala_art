# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 22:14:00 2022

@author: MEGHA
"""

import turtle
from math import pi, cos, tan, sin
from turtle_math import arc
from designs import *

def deg2rad(d):
    return d *  pi/180

def arc20(R):
    return pi * R / 9


def layer31(turt, col1, col2):
    
    radial = 205
    
    tr = turtle.tracer()
    lengths = [23,24,26,31,39,31,26,24,23]
    outer1wpetals(205, lengths, turt, col1, col2)
   
     
    turt.right(90) 
    
    turt.forward(10)
    turt.pendown()
    turt.right(10) 
    outer1(215, turt, col2, 1)
      
    turt.left(10)
        
    radial = 225
    turt.penup()
    
    turt.forward(10)
    turt.pendown()
    
    turt.right(10) 
    
    
    outer1(225, turt, col1, 3)
        
    turt.left(10)
        
    
    radial = 260
    turt.width(1)
    turt.penup()
    
    turt.forward(35)
    
    # lengths = [39,31,26,31,39]
    lengths = [34,35,36,35,34]
    
    turt.left(50)
    
    for _ in range(18):
                
        turt.pendown()
        turtle.tracer(0)
        petal1(turt, col2, 5, lengths)
        turtle.tracer(tr)
        turt.penup()
        turt.right(40)
        
        arc(turt, 20, radial)
            
    
        turt.left(140) 
        
    
