# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 13:45:02 2022

@author: MEGHA
"""

"""
Each layer has a radius of 100 counts

"""
import turtle
import random
from math import pi, cos, tan
from bright import bright_color_gen

turtle.colormode(255)
turtle.bgcolor(0,0,0)
turtle.tracer(5)


def deg2rad(d):
    return d * pi/180


def layer1(turt, num = random.randint(1,3), col1 = bright_color_gen(), col2 = bright_color_gen()):
    
    if num == 1:
        from layer11 import layer11
        layer11(turt, col1, col2)
    
    elif num == 2:
        from layer12 import layer12
        layer12(turt, col1, col2)
        
    elif num == 3:
        from layer13 import layer13
        layer13(turt, col1, col2)
    
def layer2(turt, num = random.randint(1,2), col1 = bright_color_gen(), col2 = bright_color_gen()):
    
    if num == 1:
        from layer21 import layer21
        layer21(turt, col1, col2)
        
    elif num == 2:
        from layer22 import layer22
        layer22(turt, col1, col2)
        
    elif num == 3:
        from layer23 import layer23
        layer23(turt, col1, col2)

    
def layer3(turt, num = random.randint(1,3), col1 = bright_color_gen(), col2 = bright_color_gen()):
    
    if num == 1:
        from layer31 import layer31
        layer31(turt, col1, col2)
        
    elif num == 2:
        from layer32 import layer32
        layer32(turt, col1, col2)
    
def layer4(turt, col1 = bright_color_gen(), col2 = bright_color_gen()):
    
    from layer4 import layer41
    layer41(turt, col1, col2)

    
try:
    # t1 = turtle.Turtle()
    # t1.right(90)
    # t1.forward(400)
    # t1.left(90)
    # t1.pencolor(255, 255, 255)
    # t1.circle(400)
    
    # t1 = turtle.Turtle()
    # t1.right(90)
    # t1.forward(175)
    # t1.left(90)
    # t1.pencolor(255, 255, 255)
    # t1.circle(175)
    
    t1 = turtle.Turtle()
    layer1(t1)
    t1.hideturtle()
    
    t2 = turtle.Turtle()
    layer2(t2,3)
    t2.hideturtle()
    
    t3 = turtle.Turtle()
    layer3(t3)
    t3.hideturtle()
    
    t4 = turtle.Turtle()
    layer4(t4)
    t4.hideturtle()
    
    turtle.hideturtle()
    
    turtle.done()
    turtle.bye()
    
except Exception as e:
    print(e)