# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 10:26:36 2022

@author: MEGHA
"""


import turtle
from math import pi, cos, tan, sin, sqrt
from designs import *

def deg2rad(d):
    return d *  pi/180



def inner(turt, col1, col2, deg):
    turt.width(1)
    turt.pendown()
    
    s1_new = cos(deg2rad(10)) / cos(deg2rad(10 - deg)) * 150
    R = s1_new * cos(deg2rad(80 + deg))
    
    s1 = s1_new - 100
    

    l = R/tan(deg2rad(50)) 
    forw = deg2rad(R)
 
    for _ in range(18):
        
        turt.fillcolor(col2)
        turt.begin_fill()
        turt.forward(s1)
        turt.forward(forw/2)
        
        for _ in range(59-deg):
            turt.right(1)
            turt.forward(forw)
            
        turt.right(1)
        turt.forward(forw/2)
        
        turt.forward(l)
        turt.right(80)
        turt.forward(l)
        
        turt.forward(forw/2)
        
        for _ in range(59-deg):
            turt.right(1)
            turt.forward(forw)
            
        turt.right(1)
        turt.forward(forw/2)
        
        turt.forward(s1)
        turt.end_fill()
        
        turt.left(90)
        turt.penup()
        turt.forward(deg2rad(100)/2)
        for _ in range(deg*2-1):
            turt.right(1)
            turt.forward(deg2rad(100))
            
        turt.right(1)
        turt.forward(deg2rad(100)/2)
        turt.pendown()
        
        turt.left(90)
        
        
def petals(turt, col1, col2):
    
    r1 = 20
    f1 = deg2rad(r1)
    
    turt.forward(f1/2)
    for _ in range(79):
        turt.right(1)
        turt.forward(f1)
        
    turt.right(1)
    turt.forward(f1/2)
    
    turt.right(180)
    
    turt.forward(f1/2)
    for _ in range(79):
        turt.left(1)
        turt.forward(f1)
        
    turt.left(1)
    turt.forward(f1/2)
    
    turt.left(180)
    
    turt.forward(f1/2)
    for _ in range(79):
        turt.left(1)
        turt.forward(f1)
        
    turt.left(1)
    turt.forward(f1/2)
    
    turt.left(180)
    
    turt.forward(f1/2)
    for _ in range(79):
        turt.right(1)
        turt.forward(f1)
        
    turt.right(1)
    turt.forward(f1/2)
    
    turt.right(180)
    
def petals2(turt, col1, col2):
    
    r1 = 20
    f1 = deg2rad(r1)
    
    turt.right(20)
    
    turt.forward(f1/2)
    for _ in range(69):
        turt.right(1)
        turt.forward(f1)
        
    turt.right(1)
    turt.forward(f1/2)
    
    turt.right(180)
    
    turt.forward(f1/2)
    for _ in range(69):
        turt.left(1)
        turt.forward(f1)
        
    turt.left(1)
    turt.forward(f1/2)
    
    turt.right(140)
    
    turt.forward(f1/2)
    for _ in range(69):
        turt.left(1)
        turt.forward(f1)
        
    turt.left(1)
    turt.forward(f1/2)
    
    turt.right(180)
    
    turt.forward(f1/2)
    for _ in range(69):
        turt.right(1)
        turt.forward(f1)
        
    turt.right(1)
    turt.forward(f1/2)
    
    turt.right(20)
    
    
def dots(turt):
    
    def little_circles():
        forw=deg2rad(8)
        turt.forward(forw/4)
        
        for _ in range(359):
            turt.right(1)
            turt.forward(forw/2)
            
        turt.right(1)
        turt.forward(forw/4)

    for _ in range(18):
        
        turt.pendown()
        turt.begin_fill()
        little_circles()
        turt.end_fill()
        
        turt.penup()
        turt.forward(deg2rad(190/2))
        turt.left(1)
    
        for _ in range(19):
            turt.forward(deg2rad(190))
            turt.left(1)
            
        turt.forward(deg2rad(190/2))

def layer22(turt, col1, col2):
            
    turt.right(10.5)
            
    turt.penup()
    turt.forward(100)
    
    
    turt.pendown()
    
    outer3(turt)
    
    turt.right(90)
    turt.penup()
    deg = 4
    
    # turt.forward(deg2rad(100)/2)
    # for _ in range(deg - 1):               
    #     turt.right(1)
    #     turt.forward(deg2rad(100))
    
    # turt.right(1)
    # turt.forward(deg2rad(100)/2)
 
    for _ in range(deg):               
        turt.right(1)
        turt.forward(deg2rad(100))
    
    turt.left(90)

    inner(turt, col1, col2, deg)
    turt.penup()
    turt.right(90)
    turt.forward(deg2rad(100)/2)
    for _ in range(10 - deg - 1):               
        turt.right(1)
        turt.forward(deg2rad(100))
    
    turt.right(1)
    turt.forward(deg2rad(100)/2)
    turt.left(90)
    
    turt.forward(65)
    turt.right(130)
    turt.pendown()
    turt.fillcolor(0,0,0)
    
    lengths = [20,27,50,27,20]
   
    for _ in range(18):
        turt.begin_fill()
        for i in range(5):
            move = lengths[i] / cos(deg2rad(10))
            r = lengths[i] * tan(deg2rad(10))
            forw = deg2rad(r)    
            
            turt.forward(move)
            turt.right(10)
                
            turt.forward(forw/2)
            for _ in range(179):
                turt.right(1)
                turt.forward(forw)
    
            turt.right(1)
            turt.forward(forw/2)
    
            turt.right(10)
            turt.forward(move)
            turt.right(180)
        turt.end_fill()
        
        turt.right(40)
        
        turt.penup()
        
        turt.forward(deg2rad(165/2))
        turt.left(1)

        for _ in range(19):
            turt.forward(deg2rad(165))
            turt.left(1)
            
        turt.forward(deg2rad(165/2))
        
            
        turt.left(140)  
        turt.pendown()
        
    turt.left(130)
    turt.penup()
    turt.forward(5)
    turt.left(90)
    turt.pencolor(col2)
    turt.fillcolor(col2)

    turt.forward(deg2rad(170/2))
    turt.left(1)

    for _ in range(9):
        turt.forward(deg2rad(170))
        turt.left(1)
        
    turt.forward(deg2rad(170/2))
    turt.right(90)
    
    turt.pendown()
    # turt.right(45)
    
    # turtle.tracer(1)
    
    turt.width(3)

    for _ in range(18):    
        petals(turt, col1, col2)
        turt.right(90)
        
        turt.penup()
        
        turt.forward(deg2rad(170/2))
        turt.right(1)
    
        for _ in range(19):
            turt.forward(deg2rad(170))
            turt.right(1)
            
        turt.forward(deg2rad(170/2))
        turt.left(90)
        
        turt.pendown()
        
         
    turt.penup()
    turt.forward(20)
    turt.left(90)
    
    turt.pencolor(col1)
    turt.fillcolor(col1)

    
    dots(turt)
        