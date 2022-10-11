import turtle
from mandala_art.designs.turtle_math import deg2rad, arc
from math import pi, sin, cos, tan
import numpy as np

turtle.colormode(255)

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
    # print(tuple(map(lambda x: int(x), list(turtle.bgcolor()))))
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
        turt.pencolor(tuple(map(lambda x: int(x), list(turtle.bgcolor()))))
        turt.fillcolor(col1)
        
        turt.begin_fill()
    
        turt.pendown()
        
        turtle.tracer(0)
        petal1dotted(turt, tuple(map(lambda x: int(x), list(turtle.bgcolor()))), len(lengths), lengths, col1)
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
    # print(tuple(map(lambda x: int(x), list(turtle.bgcolor()))))
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
        turt.pencolor(tuple(map(lambda x: int(x), list(turtle.bgcolor()))))
        turt.fillcolor(col1)
        
        turt.begin_fill()
    
        turt.pendown()
        turtle.tracer(0)
        petal1dotted(turt, (tuple(map(lambda x: int(x), list(turtle.bgcolor())))), len(lengths), lengths, col1)
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

def outer3(turt, col1, col2, width, fill = False, s1 = 50, ap = 50, base = 100):
        
    turt.pencolor(col1)
    turt.width(width)
    turt.fillcolor(col2)
    
    R = (base + s1) * cos(deg2rad(80))
    
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


def petal1(turt, pencol, num_petals, length, fillcol = np.array(turtle.bgcolor()).astype(int), angle = 20, width = 1):
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
            
            turt.right(angle/2)
            turt.forward(move)
            turt.right(180)
        turt.end_fill()
        
def petal1dotted(turt, pencol, num_petals, length, fillcol = (tuple(map(lambda x: int(x), list(turtle.bgcolor())))), angle = 20, width = 1):
    
    '''
    This is an assortment of simple petals.
    '''
    turt.pencolor(pencol)
    turt.fillcolor(fillcol)
    turt.width(width)
    turt.pendown()

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
            
            turt.right(180 - angle/2)
            for _ in range(3):
                turt.forward(length[i] / 6)
                turt.penup()
                turt.forward(length[i] / 6)
                turt.pendown()
            turt.penup()
            turt.backward(length[i])
            turt.pendown()
            turt.right(angle/2)
        turt.end_fill()
    
    else:
        move = length / cos(deg2rad(angle/2))
        r = length * tan(deg2rad(angle/2))
        turt.begin_fill()
        for i in range(num_petals):
            turt.forward(move)
            turt.right(angle/2)
                
            arc(turt, 180, r)
            
            turt.right(angle/2)
            turt.forward(move)
            turt.right(180 - angle/2)
            for _ in range(3):
                turt.forward(length / 6)
                turt.penup()
                turt.forward(length / 6)
                turt.pendown()
            turt.penup()
            turt.backward(length)
            turt.pendown()
            turt.right(angle/2)
        turt.end_fill()
    
            
def petal2(turt, col, r1, a1 = 80, orientation = 'r'):
    turt.pencolor(col)
    turt.fillcolor(col)
    turt.begin_fill()
    r2 = r1 - r1*cos(deg2rad(80))
    
    r3 = (r1 - r2) / 2
    
    orientations = ['r', 'l']
       
    arc(turt, a1, r1, orientation)
    
    if orientation == 'r':
        turt.right(90 - a1)
    
    else:
        turt.left(90 - a1)
    
    arc(turt, 180, r3, orientation)
    
    arc(turt, 90, r2, orientations[not orientations.index(orientation)])    
    
    turt.end_fill()
    return turt.pos()  


def spirals(turt, col, r1 = 30, a1 = 60, r2 = 15, a2 = 210, r3 = 10, a3 = 90, rp = 10, ap = 90):
    x = turt.xcor()
    y = turt.ycor()
    h = turt.heading()
    
    turt.pendown()
    turt.width(1)
    arc(turt,a1,r1,'l')
    arc(turt,a2,r2,'l')
    arc(turt,a3,r3,'l')
    petal2(turt, col, rp, ap, orientation = 'l')
    
    turt.penup()
    turt.setx(x)
    turt.sety(y)
    turt.seth(h)
    turt.pendown()
    arc(turt,a1,r1,'r')
    arc(turt,a2,r2,'r')
    arc(turt,a3,r3,'r')
    petal2(turt, col, rp, ap, orientation = 'r')
    
    turt.penup()
    turt.setx(x)
    turt.sety(y)
    turt.seth(h)
        
def twisted_petals(turt, R, th, num, x, y, a = 245, direction = 'l', width = 1):
    r = 2 * R * sin(deg2rad(th/2)) * tan(deg2rad(10))
    turt.width(width)
    for i in range(num):
        arc(turt, th, R, 'l')
        arc(turt, 150, r, 'l')
        if i != num-1:
            turt.penup()
        
        turt.goto(x,y)
        turt.right(a - th)
        turt.pendown()
        
        
def little_diamonds(turt, s, pencol, fillcol):
    turt.left(30)
    turt.color(pencol)
    turt.fillcolor(fillcol)

    turt.begin_fill()        
    for _ in range(2):
        turt.forward(s/4)
        turt.right(60)
        turt.forward(s/4)
        turt.right(120)
    
    turt.end_fill()

def dots1(turt, col1, col2):
    turt.penup()
    turt.width(2)
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
        
        
def dots2(turt):
    
    def little_circles():
        arc(turt, 360, 4)
        # forw=deg2rad(8)
        # turt.forward(forw/4)
        
        # for _ in range(359):
        #     turt.right(1)
        #     turt.forward(forw/2)
            
        # turt.right(1)
        # turt.forward(forw/4)

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

def petal3(turt, col1, col2):
    
    r1 = 20
    f1 = deg2rad(r1)
    
    arc(turt, 80, r1)

    turt.right(180)
    
    arc(turt, 80, r1, 'l')
    turt.left(180)
    arc(turt, 80, r1, 'l')

    turt.right(180)
    
    arc(turt, 80, r1)
    turt.left(180)
    

def petal4(turt, col1, col2):
    turt.pendown()
    
    petal2(turt, col1, 25, 80)
    
    turt.left(90)
    turt.penup()
    
    arc(turt,5,100)
    # for _ in range(5):
    #     turt.forward(deg2rad(100))
    #     turt.right(1)
    turt.pendown()
    turt.left(90)
    
    petal2(turt, col2, 15, 80)
    
    turt.left(90)
    turt.penup()
    arc(turt,15,100)
    # for _ in range(15):
    #     turt.forward(deg2rad(100))
    #     turt.right(1)
    turt.pendown()
    turt.left(90)
    
def flower(turt, r, move):
    turt.penup()
    turt.forward(move)
    
    for _ in range(9):

        turt.left(20)
        turt.pendown()
    
        arc(turt, 180, r, 'l')
        turt.penup()
        # turt.left(20)
        # turt.forward(move)
        turt.left(200)

def flower2(turt, r, move):
    flower(turt, r, move)
    
    turt.right(180)
    turt.forward(move)
    turt.right(160)
    
    flower(turt, r, move)
    
    turt.right(180)
    turt.forward(move)
