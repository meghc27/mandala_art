import turtle
from turtle_math import deg2rad, arc
from math import pi, sin, cos, tan

def outer1(radial, turt, col,  width, offset = 0):
    turt.pencolor(col)
    turt.width(width)
    for _ in range(18):
        
        
        R = radial * sin(deg2rad(10))
        forw = deg2rad(R)
        
        turt.forward(forw / 2)
        
        for _ in range(29):
            turt.right(1)
            turt.forward(forw)
       
        turt.right(1)
            
        turt.forward(R * tan(deg2rad(60)) + forw/2)
        turt.right(120)
        turt.forward(R * tan(deg2rad(60)) + forw/2)
        
        for _ in range(29):
            turt.right(1)
            turt.forward(forw)
    
        turt.right(1)    
        turt.forward(forw / 2)
        
        turt.left(160)
        
def outer1wpetals(radial, lengths, turt, col1, col2, offset = 0):
    turt.penup()
    turt.left(offset)
    turt.forward(radial)
    turt.left(90)
    
    tr = turtle.tracer()
    
    for _ in range(18):
        turt.pencolor(col1)
    
        turt.width(3)
        
        turt.fillcolor(col2)
    
        turt.begin_fill()
        arc(turt, 20, radial, 'l')
        
            
        turt.pendown()
        
        R = radial * sin(deg2rad(10))
        forw = deg2rad(R)
        turt.right(100)
        
        arc(turt, 30, R)
            
        turt.forward(R * tan(deg2rad(60)) + forw/2)
        turt.right(120)
        turt.forward(R * tan(deg2rad(60)) + forw/2)
        
        arc(turt, 30, R)
            
        turt.end_fill()
        
        turt.right(100)
        
        turt.penup()


        arc(turt, 10,radial, 'l')    
        
        turt.width(1)
        turt.pencolor(0,0,0)
        turt.fillcolor(col1)
        
        turt.begin_fill()
    
        turt.pendown()
        
        turtle.tracer(0)
        petal1(turt, (0,0,0), len(lengths), lengths, col1)
        turt.end_fill()
        turtle.tracer(tr)
        
        turt.right(180)
        
        turt.penup()
        
        arc(turt, 10, radial, 'l')
    
    
def outer1wsidepetals(radial, lengths, turt, col1, col2, offset = 0):
    turt.penup()
    turt.left(offset)
    turt.forward(radial)
    turt.left(90)
    
    tr = turtle.tracer()
    
    for _ in range(18):
        turt.pencolor(col1)
    
        turt.width(3)
        
        turt.fillcolor(col2)
    
        turt.begin_fill()
        arc(turt, 20, radial, 'l')
        
            
        turt.pendown()
        
        R = radial * sin(deg2rad(10))
        forw = deg2rad(R)
        turt.right(100)
        
        arc(turt, 30, R)
            
        turt.forward(R * tan(deg2rad(60)) + forw/2)
        turt.right(120)
        turt.forward(R * tan(deg2rad(60)) + forw/2)
        
        arc(turt, 30, R)
            
        turt.end_fill()
        
        turt.right(100)
        
        turt.penup()


        arc(turt,3,radial, 'l')    
        
        turt.width(1)
        turt.pencolor(0,0,0)
        turt.fillcolor(col1)
        
        turt.begin_fill()
    
        turt.pendown()
        
        turtle.tracer(0)
        petal1(turt, (0,0,0), len(lengths), lengths, col1)
        turt.end_fill()
        turtle.tracer(tr)
        
        turt.left(60)
        
        turt.penup()
        
        arc(turt, 17, radial, 'l')

def outer2(turt, base=400, R1 = 70, R2 = 50, a1 = 70, a2 = 20, offset = 0, width = 4):
    
    '''
    This is an outline layer that combines an inward arc, an outward arc and a triangle.
    '''
    
    a3 = 100 + a2 - a1
    theta = a1 - 10
    x = 2 * R2 * sin(deg2rad(a2/2))
 
    s = base * tan(deg2rad(10)) - R1 * (1 - cos(deg2rad(theta))) - x * sin(deg2rad(theta - a2/2))
    S3 = s / cos(deg2rad(a3)) 
    
    # print(a3,x,s,S3)
    
    turt.left(offset)
    turt.penup()
    turt.forward(base)
    turt.pendown()
    turt.width(width)
    
    for _ in range(18):
        arc(turt, a1, R1, 'r')
        arc(turt, a2, R2, 'l')
        turt.forward(S3)
        turt.right(2*a3)
        turt.forward(S3)
        arc(turt, a2, R2, 'l')
        arc(turt, a1, R1, 'r')
        turt.right(180)
        
    return turt.pos()

def outer3(turt, col1, col2, width, fill = False):
        
    turt.pencolor(col1)
    turt.width(width)
    turt.fillcolor(col2)
    
    s1 = 50
    R = (100 + s1) * cos(deg2rad(80))
    
    l = R/tan(deg2rad(50))  
   
    for _ in range(18):
        if fill:
            turt.begin_fill() 
        turt.forward(s1)
        
        arc(turt, 60, R)
        turt.forward(l)
        turt.right(80)
        turt.forward(l)
        
        arc(turt, 60, R)
        
        turt.forward(s1)
        turt.right(180)
        if fill:
            turt.end_fill() 

def outer3wveins(turt, col1, col2, width, fill = False):
        
    turt.pencolor(col1)
    turt.width(width)
    turt.fillcolor(col2)
    
    s1 = 50
    R = (100 + s1) * cos(deg2rad(80))
    
    l = R/tan(deg2rad(50))  
   
    for _ in range(18):
        if fill:
            turt.begin_fill() 
        turt.forward(s1)
        
        arc(turt, 60, R)
        turt.forward(l)
        turt.right(80)
        turt.forward(l)
        
        arc(turt, 60, R)
        
        turt.forward(s1)
        turt.right(180)
        if fill:
            turt.end_fill() 

def petal1(turt, pencol, num_petals, length, fillcol = [0,0,0], angle = 20, width = 1):
    
    '''
    This is an assortment of simple petals.
    '''
    turt.pencolor(pencol)
    turt.fillcolor(fillcol)
    turt.width(width)

    if type(length) == list:
        if len(length) != num_petals:
            raise NameError("LengthDimensionalityError: length should either be a single number or a list of numbers equal to the number of petals")
        
        turt.begin_fill()
        for i in range(num_petals):
            move = length[i] / cos(deg2rad(angle/2))
            r = length[i] * tan(deg2rad(angle/2))
            
            turt.forward(move)
            turt.right(angle/2)
                
            arc(turt, 180, r)
            
            turt.right(angle/2)
            turt.forward(move)
            turt.right(180)
        turt.end_fill()
    
    else:
        move = length / cos(deg2rad(angle/2))
        r = length * tan(deg2rad(angle/2))
        turt.begin_fill()
        for i in range(num_petals):
            turt.forward(move)
            turt.right(angle/2)
                
            arc(turt, 180, r)
            
            turt.right(10/2)
            turt.forward(move)
            turt.right(180)
        turt.end_fill()
        
    
            
def petal2(turt, col, r1, a1 = 80, orientation = 'r'):
    turt.pencolor(col)
    turt.fillcolor(col)
    turt.begin_fill()
    r2 = r1 - r1*cos(deg2rad(80))
    
    r3 = (r1 - r2) / 2
    
    orientations = ['r', 'l']
       
    arc(turt, a1, r1, orientation)
    turt.right(90 - a1)
    
    arc(turt, 180, r3, orientation)
    
    arc(turt, 90, r2, orientations[not orientations.index(orientation)])    
    
    turt.end_fill()
    return turt.pos()    