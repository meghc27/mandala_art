# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 15:44:34 2022

@author: MEGHA
"""


import turtle
from math import pi, cos, tan, sin, sqrt
from designs import *

def deg2rad(d):
    return d *  pi/180


def layer23(turt, col1, col2):
    
    
    turt.right(10.5)
            
    turt.penup()
    turt.forward(100)
    
    turt.pendown()
    
    outer3(turt, col1, col2, 5, fill = True)