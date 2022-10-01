import turtle
from math import pi, cos, tan, sin

def deg2rad(d):
    return d *  pi/180

def arc20(R):
    return pi * R / 9


def layer11(turt, col1, col2):
    turt.width(1)
    turt.pencolor(col1)
    
    for _ in range(18):
       
        for _ in range(360):
            forw = pi * 90 / 360
            turt.forward(forw)
            turt.left(1)
            # t.circle(50)
        
        turt.left(20)
        
    turt.width(2)
    turt.pencolor(col2)    
    turt.left(10)
    
    for _ in range(9):
        for _ in range(360):
            forw = pi * 50 / 360
            turt.forward(forw)
            turt.left(1)
            # t.circle(50)
        
        turt.left(40)
