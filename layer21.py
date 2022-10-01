# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 22:15:53 2022

@author: MEGHA
"""


import turtle
from math import pi, cos, tan, sin, sqrt
from designs import petal2

def deg2rad(d):
    return d *  pi/180


def petals(turt, col1, col2):
    turt.pendown()
    
    petal2(turt, col1, 25, 80)
    
    turt.left(90)
    turt.penup()
    
    for _ in range(5):
        turt.forward(deg2rad(100))
        turt.right(1)
    turt.pendown()
    turt.left(90)
    
    petal2(turt, col2, 15, 80)
    
    turt.left(90)
    turt.penup()
    
    for _ in range(15):
        turt.forward(deg2rad(100))
        turt.right(1)
    turt.pendown()
    turt.left(90)
    
    
def dots(turt, col1, col2):
    turt.penup()
    turt.width(4)
    turt.pencolor(col2)
    turt.fillcolor(col1)
    
    l = 155
    
    def little_circles():
        forw=0.3
        turt.forward(forw/4)
        
        for _ in range(359):
            turt.right(1)
            turt.forward(forw/2)
            
        turt.right(1)
        turt.forward(forw/4)

    for _ in range(18):
        
        turt.forward(l)
        turt.left(90)
        
        turt.pendown()
        turt.begin_fill()
        little_circles()
        turt.end_fill()
        
        turt.penup()
        turt.left(90)
        turt.forward(l)
        turt.right(160)


def layer21(turt, col1, col2):
    turt.width(4)
    turt.pencolor(col1)
    move = 140 / cos(deg2rad(20))
    r = 140 * tan(deg2rad(20))
    forw = deg2rad(r)
    turt.penup()
    
    for _ in range(9):

        turt.forward(move)
        turt.left(20)
        turt.pendown()
    
        turt.forward(forw/2)
        for _ in range(179):
            turt.left(1)
            turt.forward(forw)

        turt.left(1)
        turt.forward(forw/2)
        turt.penup()
        turt.left(20)
        turt.forward(move)
        turt.left(180)
    
    turt.left(20)
    
    for _ in range(9):

        turt.forward(move)
        turt.left(20)
        turt.pendown()
    
        turt.forward(forw/2)
        for _ in range(179):
            turt.left(1)
            turt.forward(forw)

        turt.left(1)
        turt.forward(forw/2)
        turt.penup()
        turt.left(20)
        turt.forward(move)
        turt.left(180)
    
    turt.left(10)
    turt.width(2)
    turt.pencolor(col2)
    move = 110 / cos(deg2rad(20))
    r = 110 * tan(deg2rad(20))
    forw = deg2rad(r)
    turt.penup()
    
    for _ in range(9):

        turt.forward(move)
        turt.left(20)
        turt.pendown()
    
        turt.forward(forw/2)
        for _ in range(179):
            turt.left(1)
            turt.forward(forw)

        turt.left(1)
        turt.forward(forw/2)
        turt.penup()
        turt.left(20)
        turt.forward(move)
        turt.left(180)
    
    turt.left(20)
    
    for _ in range(9):

        turt.forward(move)
        turt.left(20)
        turt.pendown()
    
        turt.forward(forw/2)
        for _ in range(179):
            turt.left(1)
            turt.forward(forw)

        turt.left(1)
        turt.forward(forw/2)
        turt.penup()
        turt.left(20)
        turt.forward(move)
        turt.left(180)
    
    dots(turt, col1, col2)
    
    
    turt.right(2)
    turt.forward(100)
    
    turt.width(1)
    
    for _ in range(18):
        petals(turt, col1, col2)
        
    