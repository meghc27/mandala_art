import turtle
from math import pi, cos, tan, sin, sqrt
from mandala_art.designs.turtle_math import deg2rad, arc
from mandala_art.designs.designs import *

def layer41(turt, col1, col2):
    
    
    turt.pencolor(col1)
    outer2(turt, base = 308, offset = 10)
    
    turt.pencolor(col2)
    turt.penup()
    turt.left(90)
    arc(turt,10,308,'l')
    turt.right(90)
    
    for _ in range(18):
        spirals(turt, col2)
        turt.left(90)
        arc(turt,20,308,'l')
        turt.right(90)
        
    turt.penup()
    turt.forward(25)
    
    for _ in range(18):
        turt.left(50)
        turt.pendown()
        petal1dotted(turt, col2, 5, 30)    
        turt.right(40)
        turt.penup()
        arc(turt, 20, 308+25)
        turt.left(90)
        
    

def layer42(turt, col1, col2):
    turt.penup()
    turt.left(10)
    turt.forward(310)
    turt.pendown()
    outer3(turt, col1, col2, 3, s1 = 22, base = 315)
    
    turt.forward(15)
    turt.left(90)
    turt.penup()
    for _ in range(18):
        arc(turt,10,325,'l')
        turt.pendown()
        # turt.right(40)
        petal1dotted(turt, col2, 4, [30,40,50,40])
        turt.left(80)
        turt.penup()
        arc(turt,10,325,'l')
    
    turt.right(90)
    turt.forward(35)
    turt.left(90)
    for _ in range(18):
        
        arc(turt,6,360,'l')
        h = turt.heading()
        
        x = turt.xcor()
        y = turt.ycor()
        
        turt.left(120)
        turt.pendown()
        turt.fillcolor(col2)
        turt.begin_fill()
        arc(turt,100,40)
        arc(turt,200,15)
        arc(turt,60,20, 'l')
        turt.goto(x,y)
        turt.end_fill()
        turt.left(135)
        turt.forward(4)
        turt.width(5)
        turt.dot()
        turt.width(1)
        turt.goto(x,y)
        turt.seth(h)
        turt.penup()
        arc(turt,14,360,'l')