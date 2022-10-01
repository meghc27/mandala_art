# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 17:59:11 2022

@author: MEGHA
"""


import turtle
from math import pi

def deg2rad(d):
    return d *  pi/180

def arc(turt, angle, radius, direction = 'r'):

    if direction not in ['r', 'l']:
        raise NameError('Invalid direction, accepted values: r for right and l for left')
    
    forw = deg2rad(radius)
    
    turt.forward(forw/2)
    
    if direction == 'r':
        for _ in range(angle-1):
            turt.right(1)
            turt.forward(forw)
            
        turt.right(1)
        turt.forward(forw/2)
        
    if direction == 'l':
        for _ in range(angle-1):
            turt.left(1)
            turt.forward(forw)
            
        turt.left(1)
        turt.forward(forw/2)

    
            

try:
    t = turtle.Turtle()
    
    R1 = 50
    R2 = 40
    S3 = 10
    a1 = 80
    a3 = 70
    a2 = a3 + a1 - 100
    
    t.left(100)
    arc(t, a1, R1, 'r')
    arc(t, a2, R2, 'l')
    t.forward(S3)
    t.right(2*a3)
    t.forward(S3)
    arc(t, a2, R2, 'l')
    arc(t, a1, R1, 'r')
    
    turtle.done()
    turtle.bye()
    
    
    
except Exception as e:
    print(e)