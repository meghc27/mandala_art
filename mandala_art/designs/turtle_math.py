# """
import turtle
from math import pi

def deg2rad(d):
    return d *  pi/180

def arc(turt, angle, radius, direction = 'r'):

    if direction not in ['r', 'l']:
        raise NameError("InvalidDirectionError: accepted values are 'r' for right and 'l' for left")
    
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

    
