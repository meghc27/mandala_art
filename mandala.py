"""
This is the main file
"""

import turtle
from turtle import *
import random
from mandala_art.designs.bright import bright_color_gen
import numpy as np

def layer1(turt, num = random.randint(1,4), col1 = bright_color_gen(), col2 = bright_color_gen()):
    
    if num == 1:
        from mandala_art.layers.layer1 import layer11
        layer11(turt, col1, col2)
    
    elif num == 2:
        from mandala_art.layers.layer1 import layer12
        layer12(turt, col1, col2)
        
    elif num == 3:
        from mandala_art.layers.layer1 import layer13
        layer13(turt, col1, col2)
    
    elif num == 4:
        from mandala_art.layers.layer1 import layer14
        layer14(turt, col1, col2)
        
        
def layer2(turt, num = random.randint(1,2), col1 = bright_color_gen(), col2 = bright_color_gen()):
    
    if num == 1:
        from mandala_art.layers.layer2 import layer21
        layer21(turt, col1, col2)
        
    elif num == 2:
        from mandala_art.layers.layer2 import layer22
        layer22(turt, col1, col2)
        
    
def layer3(turt, num = random.randint(1,3), col1 = bright_color_gen(), col2 = bright_color_gen()):
    
    if num == 1:
        from mandala_art.layers.layer3 import layer31
        layer31(turt, col1, col2)
        
    elif num == 2:
        from mandala_art.layers.layer3 import layer32
        layer32(turt, col1, col2)
        
    elif num == 3:
        from mandala_art.layers.layer3 import layer33
        layer33(turt, col1, col2)
    
def layer4(turt, num = random.randint(1,2), col1 = bright_color_gen(), col2 = bright_color_gen()):
    
   if num == 1:
       from mandala_art.layers.layer4 import layer41
       layer41(turt, col1, col2)
       
   elif num == 2:
       from mandala_art.layers.layer4 import layer42
       layer42(turt, col1, col2)


def generate(color_scheme = 'colorful', bgcolor = 'black',
             screensize = 550, fcolor = bright_color_gen(),
             color1 = bright_color_gen(), color2 = bright_color_gen(),
             animate = True):
    turtle.colormode(255)
    if bgcolor == 'black' or bgcolor == 'Black':
        turtle.bgcolor(0,0,0)
    elif bgcolor == 'red' or bgcolor == 'Red':
        turtle.bgcolor(255,0,0)
    elif bgcolor == 'green' or bgcolor == 'Green':
        turtle.bgcolor(0,255,0)
    elif bgcolor == 'blue' or bgcolor == 'Blue':
        turtle.bgcolor(0,0,255)
    elif type(bgcolor) == tuple and len(bgcolor) == 3 and bgcolor[0]<256 and bgcolor[1]<256 and bgcolor[2]<256:
        turtle.bgcolor(bgcolor)
    else:
        raise NameError("bgcolor must be either 'black', 'white', 'red, 'green' or 'blue' or a tuple of three numbers between 0-255")
        
    if animate:
        turtle.tracer(7)
    else:
        turtle.tracer(0)
        
    screen = Screen()
    screen.setup(600, 600)
    screen.setworldcoordinates(-410,-410,410,410)
    
    if color_scheme == 'colorful' or color_scheme == 'Colorful':
        try:
            t1 = turtle.Turtle()
            layer1(t1, random.randint(1,4), bright_color_gen(), bright_color_gen())
            t1.hideturtle()
            
            t2 = turtle.Turtle()
            layer2(t2, random.randint(1,2), bright_color_gen(), bright_color_gen())
            t2.hideturtle()
            
            t3 = turtle.Turtle()
            layer3(t3, random.randint(1,3), bright_color_gen(), bright_color_gen())
            t3.hideturtle()
            
            t4 = turtle.Turtle()
            layer4(t4, random.randint(1,2), bright_color_gen(), bright_color_gen())
            t4.hideturtle()
            
            turtle.done()
            turtle.bye()
            
        except Exception as e:
            print(e)
        
    if color_scheme == 'b&w' or color_scheme == 'B&W':
       turtle.bgcolor(0,0,0)
       try:
           t1 = turtle.Turtle()
           layer1(t1, random.randint(1,4), col1 = (255,255,255), col2=(125,125,125))
           t1.hideturtle()
           
           t2 = turtle.Turtle()
           layer2(t2, random.randint(1,2), col2 = (255,255,255), col1=(125,125,125))
           t2.hideturtle()
           
           t3 = turtle.Turtle()
           layer3(t3,random.randint(1,3), col1 = (255,255,255), col2=(125,125,125))
           t3.hideturtle()
           
           t4 = turtle.Turtle()
           layer4(t4, random.randint(1,2), col2 = (255,255,255), col1=(125,125,125))
           t4.hideturtle()
           
           
           turtle.hideturtle()
           
           turtle.done()
           turtle.bye()
           
           
       except Exception as e:
           print(e) 
    
    if color_scheme == 'sepia' or color_scheme == 'Sepia':
       turtle.bgcolor(112,66,20)
       try:
           t1 = turtle.Turtle()
           layer1(t1, random.randint(1,4), col1 = (255,255,255), col2=(255,255,255))
           t1.hideturtle()
           
           t2 = turtle.Turtle()
           layer2(t2,random.randint(1,2), col2 = (255,255,255), col1=(255,255,255))
           t2.hideturtle()
           
           t3 = turtle.Turtle()
           layer3(t3, random.randint(1,3), col1 = (255,255,255), col2=(255,255,255))
           t3.hideturtle()
           
           t4 = turtle.Turtle()
           layer4(t4, random.randint(1,2), col2 = (255,255,255), col1=(255,255,255))
           t4.hideturtle()
           
           
           turtle.hideturtle()
           
           turtle.done()
           turtle.bye()
            
       except Exception as e:
            print(e)
        
    
    if color_scheme == 'monochrome' or color_scheme == 'Monochrome':
        try:
            t1 = turtle.Turtle()
            layer1(t1, random.randint(1,4), col1 = fcolor, col2 = fcolor)
            t1.hideturtle()
            
            t2 = turtle.Turtle()
            layer2(t2, random.randint(1,2), col1 = fcolor, col2 = fcolor)
            t2.hideturtle()
            
            t3 = turtle.Turtle()
            layer3(t3, random.randint(1,3), col1 = fcolor, col2 = fcolor)
            t3.hideturtle()
            
            t4 = turtle.Turtle()
            layer4(t4, random.randint(1,2), col1 = fcolor, col2 = fcolor)
            t4.hideturtle()
            
            
            turtle.hideturtle()
            
            turtle.done()
            turtle.bye()
            
        except Exception as e:
            print(e)
            
    if color_scheme == 'bicolor' or color_scheme == 'Bicolor':
        try:
            t1 = turtle.Turtle()
            layer1(t1, random.randint(1,4), col1 = color1, col2 = color2)
            t1.hideturtle()
            
            t2 = turtle.Turtle()
            layer2(t2, random.randint(1,2), col1 = color1, col2 = color2)
            t2.hideturtle()
            
            t3 = turtle.Turtle()
            layer3(t3, random.randint(1,3), col1 = color1, col2 = color2)
            t3.hideturtle()
            
            t4 = turtle.Turtle()
            layer4(t4, random.randint(1,2), col1 = color1, col2 = color2)
            t4.hideturtle()
            
        
            turtle.done()
            turtle.bye()
            
        except Exception as e:
            print(e)
            
       
def multiple(num_mandalas=10, screensize = 550):
    turtle.colormode(255)
    turtle.bgcolor(0,0,0)
    screen = Screen()
    screen.setup(screensize, screensize)
    screen.setworldcoordinates(-410,-410,410,410)
    
    try:
        for i in range(num_mandalas):
            turtle.tracer(5)
            
            t1 = turtle.Turtle()
            layer1(t1, random.randint(1,4), bright_color_gen(), bright_color_gen())
            t1.hideturtle()
            
            t2 = turtle.Turtle()
            layer2(t2, random.randint(1,2), bright_color_gen(), bright_color_gen())
            t2.hideturtle()
            
            t3 = turtle.Turtle()
            layer3(t3, random.randint(1,3), bright_color_gen(), bright_color_gen())
            t3.hideturtle()
            
            t4 = turtle.Turtle()
            layer4(t4, random.randint(1,2), bright_color_gen(), bright_color_gen())
            t4.hideturtle()
            if i == num_mandalas-1:
                continue
            t4.color(0,0,0)
            turtle.tracer(1)
            t4.circle(50)
            screen.clear()
            turtle.bgcolor(0,0,0)
            turtle.colormode(255)
            turtle.hideturtle()
            
        turtle.done()
        turtle.bye()
        
    except Exception as e:
        print(e)


def custom(l1, color11, color12, l2, color21, color22,
           l3, color31, color32, l4, color41, color42,
           bgcolor=(0,0,0), screensize = 550, animate = True):
    try:
        
        if animate:
            turtle.tracer(5)
        else:
            turtle.tracer(0)
        
        turtle.colormode(255)
        turtle.bgcolor(bgcolor)
        screen = Screen()
        screen.setup(screensize, screensize)
        screen.setworldcoordinates(-410,-410,410,410)
        
        t1 = turtle.Turtle()
        layer1(t1, l1, color11, color12)
        t1.hideturtle()
        
        t2 = turtle.Turtle()
        layer2(t2, l2, color21, color22)
        t2.hideturtle()
        
        t3 = turtle.Turtle()
        layer3(t3, l3, color31, color32)
        t3.hideturtle()
        
        t4 = turtle.Turtle()
        layer4(t4, l4, color41, color42)
        t4.hideturtle()
        
        turtle.done()
        turtle.bye()
        
    except Exception as e:
        print(e)